# Design — Ressurgir

Sistema visual das páginas, painéis e posts de Instagram do lançamento Ressurgir. A linguagem vem da referência [GroundZero no Behance](https://www.behance.net/gallery/243007699/Social-Media-Consultoria-Empresarial): teal profundo em degradê, verde-água (menta) como destaque, creme alternando com o teal, tipografia geométrica leve com palavras-chave em negrito, botões em pílula e muito espaço vazio. Referências vivas: [index.html](index.html) e [painel-marketing.html](painel-marketing.html).

> As cores foram lidas à vista a partir das imagens da referência (não há código oficial). Para ajustar, altere só os tokens `--brand`, `--brand-strong`, `--brand-dark` e `--accent`.

## Princípios

1. **Menta é destaque e progresso.** Use `--brand` para o que avança ou precisa ser lido primeiro: palavra-chave, barra de progresso, botão sobre fundo escuro. Não use como decoração.
2. **Neutros esverdeados.** Fundo, bordas e trilhos puxam levemente para o teal, e o creme `--cream` quebra o ritmo. Nunca cinza puro.
6. **Leve contra negrito.** Texto em peso 300 e só a palavra que importa em 700 (e em menta ou teal), como nos posts da referência.
3. **Estado tem forma.** Situação aparece como pill (cor + texto), nunca só como cor.
4. **Números alinhados.** Todo número em coluna usa a fonte mono com `tabular-nums`.
5. **Claro e escuro.** Toda cor vem de um token; o tema escuro só redefine os tokens.

---

## Linguagem visual (referência GroundZero)

| Item | Valor |
| --- | --- |
| Fonte | Outfit para tudo (300 em títulos e textos de apoio, 700 nas palavras-chave, 600 em botões e títulos de card); JetBrains Mono só para números de tabela |
| Fundos | teal profundo em degradê (`#00454D` → `#007A78`) nas faixas de abertura e fechamento; creme `#FDEEE3` e branco nas faixas de conteúdo |
| Destaque | menta `#00DCC0` sobre teal profundo; `#00857F` sobre fundo claro |
| Botão sobre fundo escuro | pílula em degradê menta (`#00DCC0` → `#7AF0DC`) com texto `#00262C` |
| Botão sobre fundo claro | pílula `#00716F`, texto branco, hover `#005F5D`, pressionado `#004A49` |
| Cards | raio 12px, borda 1px `--line`, sombra suave só em vídeo e mockups |
| Gradiente mesh | menta e teal borrados sobre o teal profundo, com um toque de creme |
| Profundidade (pilares 5 a 12) | cartão em teal profundo `#00454D`, texto branco; superfície (1 a 4) em cartão branco sobre creme |
| Fotos | tratadas em duotone teal, nunca coloridas cruas |
| Moldura fina | contorno de 1px em menta em torno de mockups e fotos, e chips (pílulas de contorno) para rótulos como "Avaliação da Gestão" |

> Nesta linguagem a sombra é permitida só em vídeo e mockups. Nos painéis internos continua valendo "sem sombras".

---

## Gestalt

Princípios de percepção que organizam as telas. Em dúvida, aplique estes antes de adicionar borda, cor ou ícone.

| Princípio | Regra no projeto | Onde aparece |
| --- | --- | --- |
| Proximidade | Itens relacionados ficam a 8–12px; grupos distintos, a 28px ou mais | Título, slogan e texto da hero juntos, com mais espaço até o vídeo |
| Região comum | Quem pertence ao mesmo grupo divide o mesmo fundo e a mesma borda | Os pilares "Na superfície" e "Na profundidade" |
| Semelhança | Elementos de mesma função têm a mesma forma, tamanho e cor | Os 12 cards de pilar são idênticos; só o grupo muda o tom do fundo |
| Continuidade | Uma linha guia o olhar de um item ao próximo | Linha vertical ligando as etapas do método |
| Figura e fundo | Um único elemento em destaque por tela, sobre fundo calmo | Vídeo elevado na hero; botão principal em teal cheio |
| Simetria e alinhamento | Eixo central nas seções de abertura e de chamada; grades alinhadas à esquerda no resto | Hero, oferta e CTA centralizados; pilares em grade |
| Fechamento | Contêineres com borda sugerem unidade sem precisar de caixa pesada | Cards e tabela com 1px de borda e cantos arredondados |

---

## Cores

### Tokens

| Token | Claro | Escuro | Uso |
| --- | --- | --- | --- |
| `--brand` | `#00DCC0` | `#00DCC0` | Menta: destaques sem texto, palavras-chave sobre teal escuro, barras de progresso |
| `--brand-strong` | `#00716F` | `#00716F` | Fundo de botões e filtro ativo sobre fundo claro, sempre com texto branco |
| `--brand-dark` | `#00454D` | `#00454D` | Teal profundo: faixas de abertura e fechamento, cartões de destaque |
| `--brand-ink` | `#FFFFFF` | `#FFFFFF` | Texto sobre `--brand-strong` e `--brand-dark` |
| `--accent` | `#00857F` | `#5FE6D2` | Texto e ícones teal sobre o fundo claro (links, número de destaque) |
| `--accent-soft` | `#DFF6F2` | `#0F3A3A` | Hover de itens, fundos suaves |
| `--cream` | `#FDEEE3` | `#1A2A2B` | Faixa creme que quebra o ritmo teal e branco |
| `--bg` | `#FFFFFF` | `#071A1D` | Fundo da página |
| `--panel` | `#F1F8F7` | `#0E2528` | Cards, tabelas, campos |
| `--ink` | `#00262C` | `#E3F2F0` | Texto principal |
| `--muted` | `#4C6B6E` | `#9DB8B6` | Texto secundário, rótulos |
| `--line` | `#D6E6E3` | `#1F3B3E` | Bordas e divisórias |
| `--track` | `#DCEBE8` | `#173034` | Trilho de barras, pill neutra |

### Cores de estado

Separadas da cor da marca. Só para situação (meta, prazo, erro).

| Token | Claro | Escuro | Significado |
| --- | --- | --- | --- |
| `--good` | `#2E7D4F` | `#6CC592` | Dentro da meta, concluído |
| `--warn` | `#B7791F` | `#E0A84A` | Perto da meta, em andamento |
| `--bad` | `#B84A3A` | `#E57C6B` | Fora da meta, erro |

### Regras de contraste

- Texto branco só sobre `--brand-strong` (`#00716F`) ou `--brand-dark`. Branco sobre a menta `#00DCC0` não passa.
- Texto sobre a menta é sempre escuro (`#00262C`).
- Texto teal sobre fundo claro usa `--accent` (`#00857F`), não `--brand`. No tema escuro, `--accent` é `#5FE6D2`.
- Pills de estado: fundo com 16–18% da cor e texto na cor cheia.

### Implementação

```css
:root {
  color-scheme: light;
  --bg: #ffffff; --panel: #f1f8f7; --ink: #00262c; --muted: #4c6b6e; --line: #d6e6e3;
  --brand: #00dcc0; --brand-strong: #00716f; --brand-dark: #00454d; --brand-ink: #ffffff;
  --accent: #00857f; --accent-soft: #dff6f2; --cream: #fdeee3; --track: #dcebe8;
  --good: #2e7d4f; --warn: #b7791f; --bad: #b84a3a;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --bg: #071a1d; --panel: #0e2528; --ink: #e3f2f0; --muted: #9db8b6; --line: #1f3b3e;
    --accent: #5fe6d2; --accent-soft: #0f3a3a; --cream: #1a2a2b; --track: #173034;
    --good: #6cc592; --warn: #e0a84a; --bad: #e57c6b;
  }
}
:root[data-theme="dark"] { /* mesmos valores do bloco escuro acima */ }
```

---

## Tipografia

| Papel | Fonte | Token | Uso |
| --- | --- | --- | --- |
| Display e texto | Outfit 300/400/600/700 | `--font-display`, `--font-body` | Títulos (300 com palavras-chave em 700), corpo, rótulos, botões (600) |
| Dados | JetBrains Mono 400/600 | `--font-mono` | Números, valores, campos numéricos |

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
```

### Escala

| Nome | Tamanho / altura | Peso | Fonte | Exemplo |
| --- | --- | --- | --- | --- |
| Título da página | `clamp(26px, 4vw, 40px)` / 1.15 | 700 | Display | Nome do produto |
| Título de seção (h2) | 20px / 1.2 | 700 | Display | "Entregas por área" |
| Título de card | 16px / 1.3 | 600 | Display | "Tráfego pago" |
| Número grande | 28px / 1.1 | 600 | Mono | "64%" |
| Corpo | 15px / 1.5 | 400 | Texto | Parágrafos, itens |
| Secundário | 13–12.5px / 1.5 | 400 | Texto | Descrições, notas |
| Eyebrow | 12px, maiúsculas, `letter-spacing: .08em` | 600 | Texto | "PROGRESSO GERAL" |

Títulos usam `text-wrap: balance`. Linhas de texto corrido até ~65 caracteres.

---

## Espaçamento

Base de **4px**. Use só estes valores.

| Token sugerido | Valor | Uso típico |
| --- | --- | --- |
| `--space-1` | 4px | Entre rótulo e campo |
| `--space-2` | 8px | Entre botões, gap interno pequeno |
| `--space-3` | 12px | Gap de grades de cards, padding de campo |
| `--space-4` | 16px | Padding de card, margem lateral mínima |
| `--space-6` | 24px | Padding do cabeçalho |
| `--space-7` | 28px | Entre seções da página |
| `--space-8` | 32px | Padding lateral do cabeçalho em telas largas |

Regras:

- Espaço entre irmãos sempre com `gap` (flex/grid), não com `margin`.
- Margem lateral da página: no mínimo 16px, inclusive no celular.
- Largura máxima do conteúdo: **1180px**, centralizado.

## Raios

| Valor | Onde |
| --- | --- |
| 6px | Campos pequenos (meta na tabela), hover de item de lista |
| 8px | Botões, campos, selects |
| 10px | Cards, tabelas, blocos de resumo |
| 14px | Faixa do cabeçalho |
| 99px | Pills e barras de progresso |

## Bordas e sombras

- Borda padrão: `1px solid var(--line)`.
- **Sem sombras.** A separação vem da borda e do contraste `--panel` sobre `--bg`.
- Foco visível em tudo que é clicável: `outline: 2px solid var(--accent); outline-offset: 2px`.

---

## Componentes

### Botões

| Variante | Quando usar |
| --- | --- |
| Principal | A ação mais importante da tela (uma por área) |
| Secundário | Ações comuns: filtros, copiar, abrir/fechar |
| Fantasma | Ações discretas dentro de cards ou tabelas |
| Perigo | Apagar, zerar. Sempre pede um segundo clique de confirmação |

```css
.btn {
  display: inline-flex; align-items: center; gap: 8px;
  font: 500 13px/1 var(--font-body);
  padding: 8px 14px; border-radius: 8px; cursor: pointer;
  border: 1px solid var(--line); background: var(--panel); color: var(--ink);
}
.btn:hover { border-color: var(--muted); }
.btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.btn:disabled { opacity: .5; cursor: not-allowed; }

.btn-primary { background: var(--brand); border-color: var(--brand); color: var(--brand-ink); font-weight: 600; }
.btn-primary:hover { filter: brightness(.95); border-color: var(--brand); }

.btn-ghost { background: transparent; border-color: transparent; color: var(--accent); }
.btn-ghost:hover { background: var(--accent-soft); }

.btn-danger { color: var(--bad); }
.btn-danger:hover { border-color: var(--bad); }

/* Botão de filtro ativo (toggle) */
.btn[aria-pressed="true"] { background: var(--brand); border-color: var(--brand); color: var(--brand-ink); font-weight: 600; }
```

```html
<button class="btn btn-primary" type="button">Salvar</button>
<button class="btn" type="button">Copiar dados</button>
<button class="btn btn-ghost" type="button">Ver detalhes</button>
<button class="btn btn-danger" type="button">Zerar painel</button>
```

**Texto do botão:** verbo que diz o que acontece ("Copiar dados", "Zerar painel"), não "OK" ou "Enviar".

**Confirmação de ação destrutiva:** no primeiro clique o botão muda para "Clique de novo para zerar" por 4 segundos; só o segundo clique executa.

### Campos

```css
.field { display: grid; gap: 4px; font-size: 13px; color: var(--muted); }
.field input, .field select {
  width: 100%; min-width: 0;
  padding: 8px 10px; border: 1px solid var(--line); border-radius: 8px;
  background: var(--panel); color: var(--ink); font: inherit;
}
.field input[type="number"] { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }
.field input:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
```

```html
<label class="field" for="k-invest">Investimento (R$)
  <input id="k-invest" type="number" min="0" step="0.01" inputmode="decimal">
</label>
```

- Todo campo tem `<label>` e `id` próprio.
- Unidade no rótulo: "Investimento (R$)", não dentro do campo.
- Em grade: `grid-template-columns: repeat(auto-fit, minmax(160px, 1fr))`. O campo precisa de `width: 100%; min-width: 0` para não vazar da coluna.

### Título editável

Campo de texto com cara de título, usado onde o nome ainda pode mudar.

```css
.title-input {
  font: 700 clamp(26px, 4vw, 40px)/1.15 var(--font-display);
  background: transparent; border: 0; padding: 4px 0;
  border-bottom: 2px dashed color-mix(in srgb, currentColor 40%, transparent);
}
.title-input:focus { outline: none; border-bottom: 2px solid currentColor; }
```

Use com `<datalist>` quando houver opções sugeridas.

### Cabeçalho (faixa teal)

```css
.page-header {
  display: grid; gap: 6px;
  background: var(--brand); color: var(--brand-ink);
  border-radius: 14px; padding: 24px clamp(18px, 3vw, 32px);
}
```

Uma faixa por página, no topo. Contém eyebrow, título e uma linha de ajuda.

### Card de resumo (stat)

```css
.stat { display: grid; gap: 4px; align-content: start;
  background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 16px; }
.stat .val { font: 600 28px/1.1 var(--font-mono); font-variant-numeric: tabular-nums; }
```

Estrutura: eyebrow → número grande → barra ou linha secundária. Em grade `repeat(auto-fit, minmax(200px, 1fr))`, gap 12px.

### Barra de progresso

```css
.bar { height: 8px; background: var(--track); border-radius: 99px; overflow: hidden; }
.bar > span { display: block; height: 100%; background: var(--brand); border-radius: 99px; transition: width .3s; }
@media (prefers-reduced-motion: reduce) { .bar > span { transition: none; } }
```

Sempre acompanhada do número ("8 de 13 entregas · 62%").

### Pill de status

```css
.pill { display: inline-block; font-size: 12px; font-weight: 600; padding: 2px 10px;
  border-radius: 99px; background: var(--track); color: var(--muted); white-space: nowrap; }
.pill.good { background: color-mix(in srgb, var(--good) 16%, transparent); color: var(--good); }
.pill.warn { background: color-mix(in srgb, var(--warn) 18%, transparent); color: var(--warn); }
.pill.bad  { background: color-mix(in srgb, var(--bad) 16%, transparent);  color: var(--bad); }
```

| Pill | Texto padrão |
| --- | --- |
| neutra | Não iniciado · Sem dados · Sem meta |
| `good` | Concluído · Dentro da meta |
| `warn` | Em andamento · Perto da meta (até 15% da meta) |
| `bad` | Fora da meta |

### Card de área com checklist

Um `<details>` por área: o resumo mostra nome, pill, objetivo, barra e contagem; ao abrir aparece o checklist.

```css
.area { background: var(--panel); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
.area summary { list-style: none; cursor: pointer; padding: 16px; display: grid; gap: 10px; }
.area[open] summary { border-bottom: 1px solid var(--line); }
.area li label { display: flex; gap: 10px; padding: 6px 8px; border-radius: 6px; cursor: pointer; }
.area li label:hover { background: var(--accent-soft); }
.area li input { accent-color: var(--brand); width: 16px; height: 16px; }
.area li.done span { color: var(--muted); text-decoration: line-through; }
```

Grade: `repeat(auto-fill, minmax(330px, 1fr))`, gap 14px, uma coluna abaixo de 420px. Numeração (01, 02…) só quando a ordem tem significado.

### Tabela

```css
.table-wrap { overflow-x: auto; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; }
table { border-collapse: collapse; width: 100%; min-width: 620px; }
th, td { padding: 10px 14px; text-align: left; border-bottom: 1px solid var(--line); }
th { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); font-weight: 600; }
tr:last-child td { border-bottom: 0; }
```

- A tabela rola na horizontal dentro do próprio contêiner; a página nunca rola de lado.
- Colunas de valor em fonte mono. Valor ausente = `—`.

### Cabeçalho de seção

```html
<div class="section-head">
  <h2>Indicadores de mídia</h2>
  <span class="sub">Preencha os números do período.</span>
</div>
```

```css
.section-head { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 8px; margin-bottom: 12px; }
```

---

## Posts de Instagram

Mesma linguagem do site, aplicada em peças 1080 × 1350 px (feed 4:5) e 1080 × 1080 px. A referência é a série de consultoria empresarial do GroundZero.

### Anatomia

| Elemento | Regra |
| --- | --- |
| Fundo | Degradê teal profundo (`#00454D` → `#007A78`) com um brilho menta suave no canto; um post a cada três ou quatro usa fundo creme `#FDEEE3` com texto teal escuro |
| Logo | "Ressurgir:" centralizada no topo (ou no rodapé do texto), pequena, em branco com os dois pontos em menta |
| Título | Outfit 300 em branco, 56–72 px, até 3 linhas, centralizado; **a palavra-chave em 700 e menta** (ex.: "Os **12 pilares**") |
| Apoio | Outfit 300, 28–32 px, branco a 80%, no máximo 2 linhas |
| Rótulo | Chip de contorno de 1px em menta (pílula) acima do título, para o tema do post, ex.: "Terreno biológico" |
| Número-marca | Numeral gigante (ex.: "12") em teal 15% mais claro que o fundo, atrás do assunto, cortado pela borda |
| Imagem | Ilustração do projeto (Iceberg ou ícones dos pilares) ou foto em duotone teal, dentro de moldura fina de 1px em menta com cantos de 24 px |
| Chamada | Pílula em degradê menta (`#00DCC0` → `#7AF0DC`) com texto `#00262C`, ícone de link à esquerda e cursor desenhado na ponta: "Acesse o link da bio" |
| Margens | 96 px nas laterais e 120 px em cima e embaixo; nada fora dessa área |

### Variações

1. **Capa de carrossel:** título grande, chip, sem chamada; seta discreta "deslize" no canto inferior.
2. **Pilar:** ilustração do pilar centralizada, número do pilar em menta, nome do pilar em 700.
3. **Superfície x profundidade:** metade superior creme, metade inferior teal profundo, separadas por uma linha d'água pontilhada em menta.
4. **Chamada final:** fundo teal profundo, título curto e o botão em destaque. Uma única pílula preenchida por peça.

### Regras

- Um único destaque por peça: a palavra-chave em menta, **ou** a pílula, nunca vários concorrendo.
- Contraste: texto branco só sobre teal profundo; sobre menta, texto escuro.
- Sem rostos nem imagens esotéricas. A mulher do iceberg é a ilustração estilizada sem rosto.
- Texto em português, sem promessa de cura ou de resultado garantido. Incluir o aviso legal nas legendas, não na arte.
- Sempre a mesma ordem de leitura: chip, título, apoio, imagem, chamada (Gestalt de continuidade, de cima para baixo).

---

## Formatos de dados

| Tipo | Formato | Exemplo |
| --- | --- | --- |
| Dinheiro | `Intl.NumberFormat("pt-BR", {style:"currency", currency:"BRL"})` | R$ 12,50 |
| Percentual | até 2 casas + `%` | 1,85% |
| Multiplicador (ROAS) | até 2 casas + `x` | 3,2x |
| Sem valor | travessão | — |
| Hora | `toLocaleTimeString("pt-BR", {hour:"2-digit", minute:"2-digit"})` | 14:05 |

## Escrita

- Português direto, voz ativa, frases curtas.
- Nomes que o usuário reconhece: "Leads", "Vendas", "Investimento", não termos técnicos do sistema.
- Mensagens de estado dizem o que aconteceu: "Salvo neste navegador às 14:05.", "Dados copiados."
- Sem emoji como marcador.

## Responsivo e acessibilidade

- Funciona a partir de ~400px de largura: grades quebram para uma coluna.
- Nada com largura mínima maior que a tela, exceto tabelas dentro do contêiner com rolagem.
- Foco visível em todo controle; todo campo com rótulo.
- Respeitar `prefers-reduced-motion`.
- Verificar o contraste nos dois temas antes de publicar uma tela nova.
