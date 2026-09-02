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

Nova expansão da auditoria documental foi consolidada para as entradas OT-027 a OT-035.

- OT-027 — Ecclesiastes
- OT-028 — The Song of Songs
- OT-029 — Isaiah
- OT-030 — Jeremiah
- OT-031 — Ezekiel
- OT-032 — Daniel
- OT-033 — Hosea
- OT-034 — Amos
- OT-035 — Micah

As nove entradas foram classificadas como:

- LEVEL 2
- ACADEMICALLY_CORROBORATED

Ecclesiastes, Song of Songs, Isaiah, Ezekiel, Hosea, Amos e Micah seguem o padrão simples já estabelecido. Duas entradas exigiram ressalvas específicas:

- **OT-030 (Jeremiah)**: nenhuma entrada separada para Lamentations, Baruch ou Letter of Jeremiah existe no inventário do projeto — "Jeremiah" é a única posição (30) cobrindo esse território. A literatura acadêmica descreve um agrupamento tradicional "Rest of Jeremiah" (Jeremias 1-52 + Lamentações/Säqoqawä Eremyas + Baruque + Carta de Jeremias/4 Baruque) tratado como unidade no cânon estreito de 46 livros. A entrada não deve ser presumida como o livro protocanônico de Jeremias isolado; a correspondência exata com esse agrupamento mais amplo permanece `TO_BE_VERIFIED` contra a fonte primária.
- **OT-032 (Daniel)**: mesma lógica já aplicada a Esther e Job — o cânon etíope inclui, como parte de Daniel, as "Adições a Daniel" (Susana; Bel e o Dragão; Oração de Azarias e Cântico dos Três Jovens), ausentes do texto hebraico/aramaico. A forma exata na tradição etíope (uniformidade das três adições) não foi verificada diretamente e permanece `TO_BE_VERIFIED`.

Como no lote anterior, essas ressalvas refletem conhecimento acadêmico geral bem estabelecido sobre a tradição textual da LXX/cânon etíope, não citações verificadas contra fonte primária nesta sessão — o texto de cada nota diz isso explicitamente.

### Estado da auditoria

- Inventário canônico total: 81 entradas
- `textual_identity.json`: 54 entradas
- `documentary_audit.json`: 45 entradas
- Entradas auditadas: 45
- Entradas ainda pendentes em `textual_identity.json`: 9
- Entradas NT-001 a NT-027 ainda fora da camada atual de `textual_identity.json`

### Entradas já auditadas

NT-028 a NT-035; OT-001 a OT-035; OT-045; OT-046.

### Próximo passo

Continuar a auditoria documental somente das entradas ainda pendentes, sem repetir as 45 entradas já consolidadas.

Lote natural seguinte: OT-036 a OT-044 (Joel, Obadiah, Jonah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi) — os últimos 9 profetas menores. Isso esgotaria todas as pendências atualmente registradas em `textual_identity.json` (54/81), restando apenas o bloco NT-001 a NT-027, que ainda não está presente em `textual_identity.json` e cuja arquitetura de incorporação precisa ser entendida antes de qualquer criação de registro (ver handoff original, seção 13).

A próxima seleção deverá ser feita a partir do estado real do Git e dos arquivos do projeto.
