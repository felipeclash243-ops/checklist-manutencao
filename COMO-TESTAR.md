# Como testar no celular (sem instalar nada)

O app roda dentro do próprio GitHub, usando o **Codespaces**.

1. No repositório do GitHub, clique no botão verde **Code** → aba **Codespaces** → **Create codespace on main**.
2. Espere de 2 a 4 minutos. O Codespaces instala o Python e as dependências e inicia o app sozinho.
3. No terminal, embaixo, aparece um quadro **APP DE CHECKLISTS RODANDO** com o **e-mail e a senha** de acesso.
4. Abra a aba **PORTAS** (ou **PORTS**), ao lado do terminal.
5. Na linha da porta **8000**, clique com o botão direito → **Visibilidade da porta** → **Pública**. Sem isso o celular pede login do GitHub.
6. Copie o endereço da coluna **Endereço encaminhado**, algo como `https://xxxx-8000.app.github.dev`, e abra no celular.
7. Entre com o e-mail e a senha do passo 3. Para instalar como app: menu do navegador → **Adicionar à tela inicial**.

**Observações**
- O link só funciona enquanto o Codespace estiver aberto. Depois de uns 30 minutos sem uso ele desliga sozinho. Para voltar, em **Code → Codespaces**, clique no Codespace que já existe; os dados continuam lá.
- Conta gratuita do GitHub: 60 horas por mês de Codespaces.
- Para uso de verdade na empresa, veja a seção **Deploy** do [README](README.md).
