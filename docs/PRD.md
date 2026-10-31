# PRD — Painel de Marketing do lançamento Ressurgir

| | |
| --- | --- |
| Status | Rascunho v1 |
| Data | 30/10/2026 |
| Escopo | Painel de acompanhamento da entrega de marketing do lançamento |
| Referências | [painel-marketing.html](../painel-marketing.html), [DESIGN.md](../DESIGN.md) |

> Este PRD descreve o que o painel faz **hoje** (versão 1, já implementada) e o que ainda está em aberto. Trechos marcados como **A definir** não constam no código nem nos documentos do repositório e precisam de decisão.

## 1. Problema

O lançamento Ressurgir envolve dez frentes de marketing (estratégia, CRM, mídia paga, tracking, SEO, social, copy, páginas, vídeos) e duas plataformas de anúncio, em sequência. Sem um ponto único de acompanhamento, fica difícil saber o que já foi entregue, o que está atrasado e se os anúncios estão dentro da meta.

## 2. Objetivo

Dar a quem coordena o lançamento uma visão única, em uma tela, de:

1. quanto da entrega de marketing está concluído, por área;
2. em que fase o lançamento está;
3. se os indicadores de mídia paga estão dentro da meta.

### Métricas de sucesso

**A definir.** Sugestões para validar o painel: tempo para responder "o que falta?" abaixo de 10 segundos; atualização semanal do painel durante o lançamento; zero planilhas paralelas de acompanhamento.

## 3. Usuários

| Usuário | Uso principal |
| --- | --- |
| Coordenação do lançamento | Marca entregas, define a fase, revisa o progresso geral |
| Gestão de tráfego | Preenche investimento, leads, vendas e confere os indicadores contra as metas |
| Time de marketing (copy, social, vídeo, páginas) | Consulta o que falta na própria área |

**A definir:** quem exatamente usa o painel e se mais de uma pessoa o edita (ver seção 8).

## 4. Escopo

### Dentro (v1)

**4.1 Visão geral**
- Progresso geral em % e em barra.
- Contagem de entregas concluídas (ex.: 8 / 130) e de pendentes.
- Contagem de áreas concluídas (de 10) e indicação da área mais atrasada.
- Título do lançamento editável, refletido no título da aba do navegador.
- Fase atual, em lista: Planejamento → Estrutura (CRM, tracking, páginas) → Produção de conteúdo → Etapa 1 Meta Ads → Etapa 2 Google Ads → Carrinho aberto → Encerrado.

**4.2 Entregas por área**
Dez áreas, cada uma com objetivo, checklist, barra, contagem e status (Não iniciado, Em andamento, Concluído):

1. Planejamento estratégico
2. CRM e automação
3. Tráfego pago
4. Tracking e dados
5. Orgânico e SEO
6. Social media
7. Copywriting e comunicação
8. Landing pages
9. Página de vendas
10. Edição e produção de vídeos

Filtros: "Todas", "Pendentes" e "Abrir todas".

**4.3 Fases de mídia paga**
Checklists de implantação, com a mesma mecânica das áreas:
- **Etapa 1 — Meta Ads:** toda a aquisição começa no Facebook e Instagram.
- **Etapa 2 — Google Ads:** só depois que o Meta estiver rodando.

**4.4 Indicadores de mídia**
- Entradas do período: investimento, impressões, cliques, leads, vendas, faturamento.
- Calculados: CPL, CPA, CTR, CPC, conversão de leads e ROAS.
- Cada indicador tem meta editável e situação: sem meta, dentro da meta, perto da meta (até 15%) ou fora da meta.
- Regra de sentido: para custos, menor é melhor; para taxas e retorno, maior é melhor.

**4.5 Dados**
- Salvamento automático no navegador (`localStorage`), com a hora do último salvamento.
- "Copiar dados (JSON)" para exportar.
- "Zerar painel" com confirmação em dois cliques.

### Fora (v1)

- Contas de usuário e permissões.
- Sincronização entre pessoas ou dispositivos.
- Importação automática de dados do Meta Ads, Google Ads ou checkout.
- Responsáveis, prazos e datas por entrega.
- Histórico e comparação entre períodos.
- Notificações e alertas.

## 5. Requisitos funcionais

| # | Requisito | Situação |
| --- | --- | --- |
| RF1 | Marcar e desmarcar entregas; progresso recalculado na hora | Feito |
| RF2 | Status por área derivado da contagem de entregas | Feito |
| RF3 | Progresso geral considera as dez áreas e as duas fases de mídia | Feito |
| RF4 | Filtrar para ver apenas entregas pendentes | Feito |
| RF5 | Calcular os seis indicadores a partir das entradas, mostrando "—" quando faltar dado | Feito |
| RF6 | Comparar indicador com meta e mostrar situação em pill | Feito |
| RF7 | Persistir tudo no navegador a cada alteração | Feito |
| RF8 | Exportar os dados em JSON | Feito |
| RF9 | Zerar o painel com confirmação | Feito |
| RF10 | Metas iniciais sugeridas por indicador | **A definir** |

## 6. Requisitos não funcionais

- **Visual:** segue o [DESIGN.md](../DESIGN.md) (verde de marca, tokens, claro e escuro, sem sombras).
- **Acessibilidade:** foco visível, todo campo com rótulo, respeita `prefers-reduced-motion`, contraste verificado nos dois temas.
- **Responsivo:** funciona a partir de ~400px; a página nunca rola na horizontal.
- **Simplicidade técnica:** arquivo HTML único, sem build e sem servidor; abre direto no navegador.
- **Privacidade:** nenhum dado sai do navegador.
- **Idioma e formatos:** português do Brasil; moeda em R$, percentuais e multiplicadores conforme o DESIGN.md.

## 7. Fluxo principal

1. A pessoa abre o painel e dá nome ao lançamento.
2. Ao longo da preparação, marca as entregas de cada área e atualiza a fase.
3. Quando a mídia paga começa, preenche os números do período e define as metas.
4. Confere a situação de cada indicador e age onde estiver "Fora da meta".
5. Copia o JSON para guardar ou compartilhar um retrato do momento.

## 8. Riscos e questões em aberto

| # | Questão | Impacto |
| --- | --- | --- |
| 1 | Os dados ficam só no navegador de quem preencheu. Outra pessoa, outro computador ou limpeza de dados não enxerga nada. Mais de uma pessoa precisa editar? | Alto |
| 2 | Não há responsável nem prazo por entrega, então "atrasado" é só a área com menor progresso. | Médio |
| 3 | Os indicadores cobrem um período único. Para acompanhar semana a semana, falta histórico. | Médio |
| 4 | Quais são as metas de CPL, CPA, CTR, CPC, conversão e ROAS? | Médio |
| 5 | Datas do lançamento (início, abertura e fechamento do carrinho). | Médio |
| 6 | Produto, preço e público-alvo da Ressurgir não estão documentados no repositório. | Médio |
| 7 | O verde `#00C46E` é aproximado; falta o código oficial da marca. | Baixo |

## 9. Próximos passos sugeridos

1. Responder as questões 1, 4 e 5 acima.
2. Se houver mais de uma pessoa editando, decidir como compartilhar os dados (ex.: arquivo JSON versionado no repositório, ou um serviço de armazenamento).
3. Adicionar responsável e prazo por entrega, se a coordenação precisar cobrar atraso.
4. Registrar produto, oferta e público da Ressurgir em um documento próprio dentro de `docs/`.
