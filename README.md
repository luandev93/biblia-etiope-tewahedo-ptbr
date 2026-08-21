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

Atualização: 2026-08-21

### Marco concluído

A primeira expansão da auditoria documental foi consolidada para as entradas OT-001 a OT-005.

- OT-001 — Genesis
- OT-002 — Exodus
- OT-003 — Leviticus
- OT-004 — Numbers
- OT-005 — Deuteronomy

As cinco entradas foram classificadas como:

- LEVEL 2
- ACADEMICALLY_CORROBORATED

A classificação registra corroboração institucional e acadêmica, sem equivalência textual definitiva com outras tradições textuais.

Os campos `textual_source_available` e `rights_status` permanecem `TO_BE_VERIFIED`.

### Estado da auditoria

- Inventário canônico total: 81 entradas
- `textual_identity.json`: 54 entradas
- `documentary_audit.json`: 20 entradas
- Entradas auditadas: 20
- Entradas ainda pendentes em `textual_identity.json`: 34
- Entradas NT-001 a NT-027 ainda fora da camada atual de `textual_identity.json`

### Entradas já auditadas

NT-028 a NT-035; OT-001 a OT-005; OT-016; OT-020; OT-021; OT-025; OT-026; OT-045; OT-046.

### Próximo passo

Continuar a auditoria documental somente das entradas ainda pendentes, sem repetir as 20 entradas já consolidadas.

A próxima seleção deverá ser feita a partir do estado real do Git e dos arquivos do projeto.

