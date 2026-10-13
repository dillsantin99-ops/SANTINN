# SANTIN AUTOMAÇÃO LTDA — Site institucional

Site de página única da SANTIN AUTOMAÇÃO LTDA (CNPJ 10.703.586/0001-04): manutenção elétrica, manutenção mecânica, automação industrial e instalações elétricas.

Tudo está em um único arquivo: `index.html` (HTML + CSS + JavaScript, sem dependências).

## Antes de publicar: preencha os dados de contato

Abra `index.html`, procure por `DADOS DE CONTATO` (perto do fim do arquivo) e troque os valores entre colchetes:

```js
const CONTATO = {
  whatsapp: "5548999998888",              // só números: 55 + DDD + número
  telefoneExibido: "(48) 99999-8888",
  email: "contato@seudominio.com.br",
  endereco: "Rua Exemplo, 123 — Cidade/UF"
};
```

O botão de WhatsApp, o formulário de orçamento, o e-mail e o endereço usam esses valores automaticamente.

## Publicar com GitHub Pages (grátis)

1. No GitHub, abra o repositório → **Settings** → **Pages**.
2. Em **Source**, escolha **Deploy from a branch**.
3. Selecione a branch **main** e a pasta **/ (root)** → **Save**.
4. Em 1–2 minutos o site fica no ar em `https://dillsantin99-ops.github.io/santinn/`.

Para usar um domínio próprio (ex.: `santinautomacao.com.br`), informe-o no campo **Custom domain** da mesma tela.

## O que tem no site

- Topo com menu e botão de orçamento
- Herói com chamada principal e WhatsApp
- Serviços: elétrica, mecânica, automação e instalações
- Segurança: treinamentos NR-10, NR-35, NR-33 e NR-18 (PTA)
- Como trabalhamos (4 etapas)
- Formas de atendimento: preventiva, corretiva e projetos
- Contato com formulário que abre a mensagem pronta no WhatsApp
- Botão flutuante de WhatsApp
