# Bíblia Etíope Tewahedo — Português Brasileiro

Projeto documental para produção de uma edição digital da tradição bíblica Ortodoxa Etíope Tewahedo em português brasileiro.

O princípio central do projeto é a **rastreabilidade**: cada identificação, texto, tradução, variante, referência, imagem e decisão editorial deverá possuir origem documental verificável.

## Objetivos

- Preservação da estrutura textual e canônica.
- Tradução própria e documentada para PT-BR.
- Organização canônica e cronológica.
- Referências acadêmicas, históricas e institucionais.
- Registro de variantes de nomenclatura e tradição.
- Ilustrações e mapas devidamente identificados e licenciados.
- PDF digital interativo e responsivo.
- Rastreabilidade completa das fontes.
- Validação automatizada.
- Controle de versões.
- Separação entre texto-fonte, tradução, tradição, hipótese e comentário editorial.

## Metodologia

```text
SPEC
  ↓
FONTES
  ↓
INVENTÁRIO
  ↓
ESTRUTURA
  ↓
CORPUS
  ↓
TRADUÇÃO
  ↓
REVISÃO
  ↓
VALIDAÇÃO
  ↓
QA
  ↓
BUILD

## Estado atual — auditoria documental

Atualização: 2026-09-02

### Marco concluído

Nova expansão da auditoria documental foi consolidada para as entradas OT-011 a OT-015.

- OT-011 — I Chronicles
- OT-012 — II Chronicles
- OT-013 — Jubilees
- OT-014 — 1 Enoch
- OT-015 — Ezra and Nehemiah

As cinco entradas foram classificadas como:

- LEVEL 2
- ACADEMICALLY_CORROBORATED

OT-011 e OT-012 são livros históricos padrão, sem disputa de identidade. OT-015 preserva o agrupamento institucional de Ezra e Nehemiah como unidade única, com nota explícita distinguindo-a de OT-016 (Ezra Sutu'el), já auditada — a recorrência do nome "Ezra" não deve ser tratada como identidade entre as duas entradas.

OT-013 (Jubileus) e OT-014 (1 Enoque) receberam tratamento mais aprofundado: ambas as obras sobrevivem de forma **completa apenas na versão etíope (Ge'ez)**, com edições críticas reais e verificadas — Charles 1895 e VanderKam 1989 para Jubileus; Charles 1906 e Knibb 1978 para 1 Enoque. Por isso `textual_source_available` foi atualizado para `AVAILABLE` nessas duas entradas (as demais permanecem `TO_BE_VERIFIED`). `rights_status` ficou `MIXED_TO_BE_VERIFIED`: as edições de Charles (1895/1906) são de domínio público; as edições modernas (VanderKam 1989, Knibb 1978) têm direitos autorais não verificados. Nenhuma das duas entradas foi elevada a LEVEL 3 nesta rodada — a existência de edição crítica não equivale, por si só, a verificação textual-crítica completa, que exigiria revisão dedicada.

Quatro novas fontes acadêmicas foram registradas em `docs/research/SOURCES_INITIAL.md`: SRC-0006 (Charles 1895, Jubileus), SRC-0007 (Charles 1906, Enoque), SRC-0008 (Knibb 1978, Enoque) e SRC-0009 (VanderKam 1989, Jubileus).

### Estado da auditoria

- Inventário canônico total: 81 entradas
- `textual_identity.json`: 54 entradas
- `documentary_audit.json`: 30 entradas
- Entradas auditadas: 30
- Entradas ainda pendentes em `textual_identity.json`: 24
- Entradas NT-001 a NT-027 ainda fora da camada atual de `textual_identity.json`

### Entradas já auditadas

NT-028 a NT-035; OT-001 a OT-015; OT-016; OT-020; OT-021; OT-025; OT-026; OT-045; OT-046.

### Próximo passo

Continuar a auditoria documental somente das entradas ainda pendentes, sem repetir as 30 entradas já consolidadas.

Lote natural seguinte: OT-017 a OT-019 (Tobit, Judith, Esther) e OT-022 a OT-024 (Job, Psalms, Proverbs), a confirmar contra o estado real do Git antes de iniciar. Proverbs (OT-024) exige atenção especial por sua relação com OT-025 (Tegsats/Reproof), já auditada como possível porção final de Proverbs na tradição etíope — a fronteira entre as duas entradas não deve ser presumida sem evidência adicional.

A próxima seleção deverá ser feita a partir do estado real do Git e dos arquivos do projeto.
