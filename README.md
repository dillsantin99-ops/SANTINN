# Santin Automação e Tecnologia — Site institucional

Site de página única da SANTIN AUTOMAÇÃO LTDA (CNPJ 10.703.586/0001-04), seguindo o **Manual de Identidade Visual Santin**.

- `index.html` — o site completo (HTML + CSS + JavaScript, sem dependências)
- `assets/` — logotipos oficiais em SVG (vetor), extraídos do manual

## Identidade visual aplicada

| Elemento | Valor |
|---|---|
| Laranja (principal) | `#E26534` · RGB 226 101 52 · Pantone 7579 C |
| Laranja tons | `#EEA385`, `#F9E0D6` |
| Azul (principal) | `#365A68` · RGB 54 90 104 · Pantone 4161 C |
| Azul tons | `#8198A0`, `#CDD6D9` |
| Títulos | Comfortaa (Google Fonts) |
| Textos | Manrope (Google Fonts) |

Logotipos em `assets/`:

- `logo-horizontal.svg` (topo do site)
- `logo-principal.svg`
- `logo-sem-simbolo.svg`
- `simbolo.svg` (ícone da aba)
- versões `-branco.svg` de cada um, para fundos escuros

## Antes de publicar: preencha os dados de contato

Abra `index.html`, procure por `DADOS DE CONTATO` (perto do fim do arquivo) e troque os valores entre colchetes:

```js
const CONTATO = {
  whatsapp: "5548999998888",              // só números: 55 + DDD + número
  telefoneExibido: "(48) 99999-8888",
  email: "contato@seudominio.com.br",
  instagram: "santin.automacao",
  endereco: "Rua Exemplo, 123 — Cidade/UF",
  horario: "Seg. a sex., 8h às 18h"
};
```

O botão de WhatsApp, o formulário de orçamento, o e-mail, o Instagram, o endereço e o horário usam esses valores automaticamente.

## Obras realizadas e Manutenções executadas (fotos e documentos)

As duas seções são montadas automaticamente a partir de dois arquivos:

| Seção | Arquivo de dados | Pasta das fotos | Pasta dos documentos |
|---|---|---|---|
| Obras realizadas | `dados/obras.js` | `fotos/obras/` | `documentos/obras/` |
| Manutenções executadas | `dados/manutencoes.js` | `fotos/manutencoes/` | `documentos/manutencoes/` |

Para incluir um trabalho:

1. Envie as fotos (JPG, de preferência até 1600 px de largura) e os PDFs para as pastas acima.
2. No arquivo de dados, copie o modelo que está comentado e preencha:

```js
{
  titulo: "Automação da linha de envase",
  cliente: "Nome do cliente",        // opcional
  local: "Cidade/UF",                // opcional
  data: "2026-08",                   // ano-mês
  descricao: "Projeto, montagem do painel e programação do CLP.",
  servicos: ["Automação", "CLP"],
  fotos: ["fotos/obras/envase-1.jpg", "fotos/obras/envase-2.jpg"],
  documentos: [{ nome: "Relatório técnico", arquivo: "documentos/obras/envase.pdf" }]
},
```

A primeira foto vira a capa do cartão; clicando nela abre a galeria com todas as fotos. Enquanto não houver nenhum item, a seção mostra um aviso de "em breve".

> Atenção: tudo que for publicado no site fica público. Antes de subir laudos, ARTs ou relatórios, confira se o cliente autoriza e remova dados sensíveis.

## Publicar com GitHub Pages (grátis)

1. No GitHub, abra o repositório → **Settings** → **Pages**.
2. Em **Source**, escolha **Deploy from a branch**.
3. Selecione a branch **main** e a pasta **/ (root)** → **Save**.
4. Em 1–2 minutos o site fica no ar em `https://dillsantin99-ops.github.io/santinn/`.

Para usar um domínio próprio (ex.: `santinautomacao.com.br`), informe-o no campo **Custom domain** da mesma tela.

## O que tem no site

- Topo com logotipo horizontal e menu
- Herói: "Automatize sua produção com um processo confiável e seguro"
- Obras realizadas e Manutenções executadas, com galeria de fotos e documentos
- Serviços: projetos de automação, programação de CLP, NR-12, automação e controle, equipamentos e máquinas, manutenção e instalações
- Destaque NR-12: projeto, montagem e instalação
- Segurança: treinamentos NR-10, NR-35, NR-33 e NR-18 (PTA)
- Como trabalhamos (4 etapas)
- Contato com formulário que abre a mensagem pronta no WhatsApp
- Botão flutuante de WhatsApp
