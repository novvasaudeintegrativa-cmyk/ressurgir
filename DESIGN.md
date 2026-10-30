# Design — Ressurgir

Sistema visual das páginas e painéis do lançamento Ressurgir. A cor principal é um verde vivo inspirado no verde da Kiwify, sobre neutros levemente esverdeados. A referência viva é o [painel-marketing.html](painel-marketing.html). Cores, tipografia, cards, barras, pills e tabela já estão implementados lá; os botões principal e fantasma estão definidos aqui para as próximas telas.

> O verde `#00C46E` é uma aproximação. Quando tivermos o código oficial da marca, troque só o token `--brand`.

## Princípios

1. **Verde é ação e progresso.** Use `--brand` para o que avança: botão principal, barra de progresso, item marcado, filtro ativo. Não use verde como decoração.
2. **Neutros com tom verde.** Fundo, bordas e trilhos puxam levemente para o verde. Nunca cinza puro.
3. **Estado tem forma.** Situação aparece como pill (cor + texto), nunca só como cor.
4. **Números alinhados.** Todo número em coluna usa a fonte mono com `tabular-nums`.
5. **Claro e escuro.** Toda cor vem de um token; o tema escuro só redefine os tokens.

---

## Cores

### Tokens

| Token | Claro | Escuro | Uso |
| --- | --- | --- | --- |
| `--brand` | `#00C46E` | `#00C46E` | Fundos de destaque: cabeçalho, botão principal, barras, checkbox |
| `--brand-ink` | `#04281A` | `#04281A` | Texto **sobre** `--brand` |
| `--accent` | `#00874B` | `#2FD98A` | Texto e ícones verdes sobre o fundo (links, número de destaque) |
| `--accent-soft` | `#DCF5E8` | `#123526` | Hover de itens, fundos suaves |
| `--bg` | `#F1F6F3` | `#0F1713` | Fundo da página |
| `--panel` | `#FFFFFF` | `#16211B` | Cards, tabelas, campos |
| `--ink` | `#14231B` | `#E5ECE7` | Texto principal |
| `--muted` | `#56695D` | `#9AABA0` | Texto secundário, rótulos |
| `--line` | `#D3E2D8` | `#283A30` | Bordas e divisórias |
| `--track` | `#E1ECE5` | `#233229` | Trilho de barras, pill neutra |

### Cores de estado

Separadas da cor da marca. Só para situação (meta, prazo, erro).

| Token | Claro | Escuro | Significado |
| --- | --- | --- | --- |
| `--good` | `#2E7D4F` | `#6CC592` | Dentro da meta, concluído |
| `--warn` | `#B7791F` | `#E0A84A` | Perto da meta, em andamento |
| `--bad` | `#B84A3A` | `#E57C6B` | Fora da meta, erro |

### Regras de contraste

- Texto sobre `--brand` é sempre `--brand-ink`. **Nunca branco**: branco sobre `#00C46E` não passa no contraste mínimo.
- Texto verde sobre fundo claro usa `--accent` (`#00874B`), não `--brand`.
- Pills de estado: fundo com 16–18% da cor e texto na cor cheia.

### Implementação

```css
:root {
  color-scheme: light;
  --bg: #f1f6f3; --panel: #ffffff; --ink: #14231b; --muted: #56695d; --line: #d3e2d8;
  --brand: #00c46e; --brand-ink: #04281a;
  --accent: #00874b; --accent-soft: #dcf5e8; --track: #e1ece5;
  --good: #2e7d4f; --warn: #b7791f; --bad: #b84a3a;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --bg: #0f1713; --panel: #16211b; --ink: #e5ece7; --muted: #9aaba0; --line: #283a30;
    --accent: #2fd98a; --accent-soft: #123526; --track: #233229;
    --good: #6cc592; --warn: #e0a84a; --bad: #e57c6b;
  }
}
:root[data-theme="dark"] { /* mesmos valores do bloco escuro acima */ }
```

---

## Tipografia

| Papel | Fonte | Token | Uso |
| --- | --- | --- | --- |
| Display | Bricolage Grotesque 500/700 | `--font-display` | Títulos, nomes de área |
| Texto | Figtree 400/500/600 | `--font-body` | Corpo, rótulos, botões |
| Dados | JetBrains Mono 400/600 | `--font-mono` | Números, valores, campos numéricos |

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Figtree:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
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

### Cabeçalho (faixa verde)

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
