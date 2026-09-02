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

Nova expansão da auditoria documental foi consolidada para as entradas OT-036 a OT-044 — os últimos nove profetas menores.

- OT-036 — Joel
- OT-037 — Obadiah
- OT-038 — Jonah
- OT-039 — Nahum
- OT-040 — Habakkuk
- OT-041 — Zephaniah
- OT-042 — Haggai
- OT-043 — Zechariah
- OT-044 — Malachi

As nove entradas foram classificadas como:

- LEVEL 2
- ACADEMICALLY_CORROBORATED

Todas seguem o padrão simples já estabelecido, sem disputa de identidade nominal ou textual entre as fontes consultadas (SRC-0001, SRC-0004).

**MARCO IMPORTANTE**: com este lote, `documentary_audit.json` chega a 54 entradas — o mesmo total atualmente presente em `textual_identity.json`. Ou seja, toda a camada de identidade textual hoje registrada no projeto já foi auditada documentalmente. Não restam mais entradas OT ou NT pendentes dentro do conjunto que já possui `textual_identity.json`.

O que resta é o bloco **NT-001 a NT-027**, que está fora de `textual_identity.json` — isso não significa 27 registros a criar automaticamente. Antes de qualquer ação sobre esse bloco, é necessário entender a arquitetura de incorporação já usada pelo projeto (ver seção 13 do handoff original) e verificar contra o estado real do Git e dos arquivos.

### Estado da auditoria

- Inventário canônico total: 81 entradas
- `textual_identity.json`: 54 entradas
- `documentary_audit.json`: 54 entradas
- Entradas auditadas: 54
- Entradas ainda pendentes em `textual_identity.json`: 0
- Entradas NT-001 a NT-027 ainda fora da camada atual de `textual_identity.json`

### Entradas já auditadas

NT-028 a NT-035; OT-001 a OT-046 (todas as entradas OT atualmente presentes em `textual_identity.json`).

### Próximo passo

O próximo passo NÃO é criar automaticamente 27 registros para NT-001 a NT-027. Antes disso:

1. Confirmar contra o estado real do Git e dos arquivos do projeto qual é a arquitetura de incorporação pretendida para o bloco NT-001 a NT-027 (por que ficaram de fora de `textual_identity.json` até agora — decisão deliberada, lacuna, ou dependência de outra etapa).
2. Somente depois dessa confirmação, decidir o próximo lote de trabalho.

A próxima seleção deverá ser feita a partir do estado real do Git e dos arquivos do projeto, não por suposição.
