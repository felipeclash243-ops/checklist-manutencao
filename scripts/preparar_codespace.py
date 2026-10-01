"""Prepara e inicia o app automaticamente dentro do GitHub Codespaces.

- Na criação: gera o .env (SECRET_KEY e senha do Admin+ aleatórias),
  cria o banco, as áreas/unidades, o Admin+ e um checklist de exemplo.
- Ao abrir (--iniciar): mostra o login e sobe o servidor na porta 8000.
"""
import os
import secrets
import string
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENV = RAIZ / ".env"
ADMIN_EMAIL = "admin@checklist.teste"


def _gerar_senha() -> str:
    corpo = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
    return f"{corpo}#Aa1"


def _ler_env() -> dict:
    valores = {}
    for linha in ENV.read_text(encoding="utf-8").splitlines():
        if "=" in linha and not linha.lstrip().startswith("#"):
            chave, valor = linha.split("=", 1)
            valores[chave.strip()] = valor.strip()
    return valores


def preparar() -> None:
    if not ENV.exists():
        ENV.write_text(
            "\n".join(
                [
                    f"SECRET_KEY={secrets.token_hex(32)}",
                    "SESSION_COOKIE_SECURE=true",
                    # O Codespaces fica atrás de um proxy HTTPS do GitHub
                    "TRUST_PROXY=1",
                    "WTF_CSRF_SSL_STRICT=false",
                    f"ADMIN_EMAIL={ADMIN_EMAIL}",
                    "ADMIN_NAME=Administrador",
                    f"ADMIN_PASSWORD={_gerar_senha()}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    subprocess.run([sys.executable, "seed.py", "--exemplo"], cwd=RAIZ, check=True,
                   stdin=subprocess.DEVNULL)


def iniciar() -> None:
    if not ENV.exists():
        preparar()
    env = _ler_env()
    print("\n" + "=" * 60)
    print("  APP DE CHECKLISTS RODANDO")
    print("  Abra a aba PORTAS (PORTS) e clique no link da porta 8000.")
    print(f"  E-mail: {env.get('ADMIN_EMAIL')}")
    print(f"  Senha:  {env.get('ADMIN_PASSWORD')}")
    print("=" * 60 + "\n", flush=True)
    os.chdir(RAIZ)
    os.execvp(sys.executable, [sys.executable, "-m", "waitress", "--listen=0.0.0.0:8000",
                               "--threads=8", "wsgi:app"])


if __name__ == "__main__":
    iniciar() if "--iniciar" in sys.argv else preparar()
