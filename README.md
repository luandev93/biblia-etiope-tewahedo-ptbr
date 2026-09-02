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

Nova expansão da auditoria documental foi consolidada para as entradas OT-017 a OT-019 e OT-022 a OT-024.

- OT-017 — Tobit
- OT-018 — Judith
- OT-019 — Esther
- OT-022 — Job
- OT-023 — Psalms
- OT-024 — Proverbs

As seis entradas foram classificadas como:

- LEVEL 2
- ACADEMICALLY_CORROBORATED

OT-017 e OT-018 seguem o padrão simples já estabelecido. As demais quatro exigiram ressalvas textuais específicas, registradas em nota em cada entrada:

- **OT-019 (Esther)**: a tradição etíope do AT deriva da Septuaginta (LXX); é conhecimento acadêmico consolidado que Ester, nas tradições que seguem a LXX, inclui as "Adições a Ester" (seis passagens ausentes do texto massorético hebraico). A entrada não deve ser presumida equivalente ao Ester hebraico sem essas adições. A extensão exata na forma etíope permanece `TO_BE_VERIFIED`.
- **OT-022 (Job)**: a forma grega (LXX) de Jó é sensivelmente mais curta que o texto massorético e contém um epílogo adicional ausente do hebraico; dado que a tradição etíope deriva da LXX, é plausível que reflita essas características, mas isso não foi verificado diretamente nesta rodada. Não deve ser confundido com o pseudepígrafo "Testamento de Jó".
- **OT-023 (Psalms)**: o Saltério etíope segue a família textual grega e inclui o Salmo 151 ao final da sequência de 150 salmos. O volume litúrgico do Saltério etíope tradicionalmente reúne outros textos (cânticos, Cântico dos Cânticos, Wǝddase Maryam, Anqäṣä Bǝrhan) que não devem ser confundidos com o conteúdo estrito desta entrada canônica.
- **OT-024 (Proverbs)**: sua fronteira com OT-025 (Tegsats/Reproof, já auditada) permanece um ponto em aberto. Há literatura secundária associando uma divisão tradicional "Mesale" (~Provérbios 1-24) e "Tegsats" (~Provérbios 25-31), mas essa correspondência não pôde ser confirmada diretamente contra uma fonte primária nesta rodada — o acesso de pesquisa a páginas relevantes foi bloqueado pelo proxy de rede do ambiente. Mantendo a cautela já registrada em OT-025, esta entrada NÃO fixa Provérbios 1-24 como extensão universal.

Nenhuma fonte nova foi registrada nesta rodada; as ressalvas acima refletem conhecimento acadêmico geral sobre a tradição textual da LXX, não citações específicas verificadas contra fonte primária. Onde a verificação direta não foi possível, o texto da nota diz isso explicitamente.

### Estado da auditoria

- Inventário canônico total: 81 entradas
- `textual_identity.json`: 54 entradas
- `documentary_audit.json`: 36 entradas
- Entradas auditadas: 36
- Entradas ainda pendentes em `textual_identity.json`: 18
- Entradas NT-001 a NT-027 ainda fora da camada atual de `textual_identity.json`

### Entradas já auditadas

NT-028 a NT-035; OT-001 a OT-026; OT-045; OT-046.

### Próximo passo

Continuar a auditoria documental somente das entradas ainda pendentes, sem repetir as 36 entradas já consolidadas.

Lote natural seguinte: OT-027 a OT-035 (Ecclesiastes, Song of Songs, Isaiah, Jeremiah, Ezekiel, Daniel, Hosea, Amos, Micah), a confirmar contra o estado real do Git antes de iniciar. Daniel (OT-032) exige atenção especial: como Esther e Job, a tradição etíope do AT deriva da LXX, e Daniel grego é conhecido por incluir adições (Susana, Bel e o Dragão, Cântico dos Três Jovens) ausentes do texto hebraico/aramaico — a mesma ressalva de "forma grega/LXX vs. forma hebraica" já aplicada a OT-019 e OT-022 deve ser considerada para OT-032.

A próxima seleção deverá ser feita a partir do estado real do Git e dos arquivos do projeto.
