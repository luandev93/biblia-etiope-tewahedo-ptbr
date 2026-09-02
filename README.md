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

Nova expansão da auditoria documental foi consolidada para as entradas OT-006 a OT-010.

- OT-006 — Joshua
- OT-007 — Judges
- OT-008 — Ruth
- OT-009 — I and II Samuel
- OT-010 — I and II Kings

As cinco entradas foram classificadas como:

- LEVEL 2
- ACADEMICALLY_CORROBORATED

São livros históricos padrão do inventário oficial da EOTC, sem disputa de identidade nominal ou textual entre as fontes consultadas (SRC-0001, SRC-0004). OT-009 e OT-010 preservam o agrupamento institucional de I/II Samuel e I/II Kings como unidades únicas de inventário, seguindo a mesma prática já adotada para outras entradas do inventário oficial.

A classificação registra corroboração institucional e acadêmica, sem equivalência textual definitiva com a forma etíope (Ge'ez).

Os campos `textual_source_available` e `rights_status` permanecem `TO_BE_VERIFIED`.

### Estado da auditoria

- Inventário canônico total: 81 entradas
- `textual_identity.json`: 54 entradas
- `documentary_audit.json`: 25 entradas
- Entradas auditadas: 25
- Entradas ainda pendentes em `textual_identity.json`: 29
- Entradas NT-001 a NT-027 ainda fora da camada atual de `textual_identity.json`

### Entradas já auditadas

NT-028 a NT-035; OT-001 a OT-010; OT-016; OT-020; OT-021; OT-025; OT-026; OT-045; OT-046.

### Próximo passo

Continuar a auditoria documental somente das entradas ainda pendentes, sem repetir as 25 entradas já consolidadas.

Lote natural seguinte: OT-011 a OT-015 (1 Chronicles, 2 Chronicles, Jubilees, 1 Enoch, Ezra-Nehemiah), a confirmar contra o estado real do Git antes de iniciar. Jubilees e 1 Enoch exigem tratamento mais cuidadoso que os livros históricos deste lote, por possuírem perfil documental e canônico distinto dos livros protocanônicos.

A próxima seleção deverá ser feita a partir do estado real do Git e dos arquivos do projeto.
