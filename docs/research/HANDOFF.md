# HANDOFF — BÍBLIA ETÍOPE TEWAHEDO PT-BR

Data: 2026-09-02
Repositório: biblia-etiope-tewahedo-ptbr
Branch principal: `main` (todo o trabalho abaixo já está mesclado)
Substitui o handoff anterior (01/09/2026), que permanece válido como contexto histórico mas está desatualizado no estado numérico.

---

## 0. O QUE MUDOU DESDE O HANDOFF ANTERIOR

O handoff de 01/09/2026 descrevia:
- 81 inventário / 54 textual_identity / 20 documentary_audit / 34 pendências.

Estado atual:
- **81 inventário / 81 textual_identity / 81 documentary_audit / 0 pendências de identidade.**

Todas as 81 entradas do núcleo canônico (46 OT + 35 NT) agora têm:
1. Identidade textual registrada em `data/canon/textual_identity.json`;
2. Auditoria documental LEVEL 2 / `ACADEMICALLY_CORROBORATED` em `data/canon/documentary_audit.json`, com fontes SRC-0001 (EOTC) e SRC-0004 (Cowley 1974) no mínimo.

**Isto NÃO significa que o projeto está pronto para tradução.** Ver seção 3.

---

## 1. INSTRUÇÃO PRINCIPAL PARA O PRÓXIMO CHAT

Mesmas regras do handoff original continuam valendo:

1. Não repetir pesquisas já consolidadas (as 81 entradas de identidade/LEVEL 2 estão feitas — não reauditar sem razão concreta).
2. Não reconstruir arquivos por memória ou suposição — sempre ler o estado real do repositório primeiro.
3. Não inventar fontes, DOI, manuscritos, URLs, identificadores ou equivalências.
4. Não transformar hipótese em fato; preferir `TO_BE_VERIFIED` a suposição.
5. Não considerar nomes semelhantes como prova de identidade textual.
6. Não elevar uma entrada para LEVEL 3 apenas por associação nominal ou pela existência de uma edição crítica — LEVEL 3 exige revisão textual-crítica dedicada.
7. **Antes de iniciar qualquer tradução, confirmar que `textual_source_available = SIM` (ou equivalente) e `rights_status` resolvido para a entrada específica.** Ver regra de tradução em `docs/research/RESEARCH_PROTOCOL.md`.
8. Ambiente: esta sessão roda em execução remota com acesso direto ao clone Git local (não é mais um cenário Termux-sem-acesso como o handoff original presumia) — comandos Git podem ser executados diretamente pelo assistente.
9. Sempre validar (`python3 -m json.tool` ou equivalente) antes de commitar arquivos JSON.
10. Merges para `main` são autorizados pelo usuário (confirmado em 02/09/2026) — mesclar ao final de cada lote/marco concluído, não acumular divergência.

---

## 2. ESTRUTURA E ARQUITETURA (sem mudanças)

```
data/canon/
├── official_eotc_inventory.json   # fonte institucional bruta (46 OT + 35 NT nomes)
├── canon_inventory.json           # 81 entradas operacionais (OT-001..046, NT-001..035)
├── canon_layers.json              # camadas (CORE_81, BROADER_CANON, TRADITIONAL, DISPUTED)
├── canon_status.json              # vocabulário de status (schema, não dados)
├── broader_canon.json             # Sinodos/Covenant/Clement/Didascalia (fora do núcleo 81)
├── normalization_queue.json       # fila de problemas de normalização (Q-001..Q-015)
├── research_matrix.json           # matriz de pesquisa (RM-001..RM-015)
├── textual_identity.json          # 81/81 — identidade textual de cada entrada
└── documentary_audit.json         # 81/81 — auditoria LEVEL 2 de cada entrada

docs/research/
├── SOURCES_INITIAL.md             # SRC-0001 a SRC-0009 (ver seção 4)
├── CANON_RESEARCH.md              # estado da pesquisa do cânon
├── DECISION_LOG.md                # DEC-0001 a DEC-0003
├── RESEARCH_PROTOCOL.md           # níveis de evidência, hierarquia de fontes, regra de ouro
└── HANDOFF.md                     # este arquivo
```

`canon_inventory.json` mantém `identity_status: "UNVERIFIED"` para todas as entradas — este campo **não é atualizado** pela auditoria (decisão implícita mantida por precedente desde a primeira rodada); `documentary_audit.json` é a fonte de verdade para o nível de verificação, não `canon_inventory.json`.

---

## 3. O QUE "81/81 AUDITADAS" SIGNIFICA — E O QUE NÃO SIGNIFICA

A arquitetura de progressão do projeto é:

```
CANON → 81 ENTRADAS → TEXTUAL IDENTITY → DOCUMENTARY AUDIT → TEXTUAL SOURCE / RIGHTS STATUS → CORPUS READY → PT-BR
```

**Concluído**: as duas primeiras setas (identidade + auditoria documental LEVEL 2) para as 81 entradas.

**Não concluído** — e é a maior parte do projeto:

- `textual_source_available`: `TO_BE_VERIFIED` para 79 de 81 entradas. Só OT-013 (Jubilees) e OT-014 (1 Enoch) têm `AVAILABLE` confirmado (edições críticas reais: Charles 1895/1906, VanderKam 1989, Knibb 1978 — ver SRC-0006 a SRC-0009).
- `rights_status`: `TO_BE_VERIFIED` (ou `MIXED_TO_BE_VERIFIED` para Jubilees/Enoch) para praticamente todas as entradas. Nenhuma licença deve ser presumida.
- **LEVEL 3** (verificação textual-crítica completa): 0 entradas. Isso exigiria comparação direta contra manuscrito/edição crítica, não apenas confirmação de que uma edição existe.
- **CORPUS, TRADUÇÃO, REVISÃO, VALIDAÇÃO, QA, BUILD**: nenhuma dessas fases foi iniciada.

### Estimativa de escopo restante (comunicada ao usuário em 02/09/2026)

| Fase | Escopo | Natureza |
|---|---|---|
| Resolver fonte/direitos por entrada | 79 entradas restantes | Terminável — pesquisa dedicada por obra, ritmo similar ao já empregado (~8-15 lotes de trabalho) |
| Resolver pendências específicas já sinalizadas (seção 5) | ~6 itens | Terminável — 1-2 lotes |
| CORPUS (obtenção real dos textos-fonte) | Depende da fase anterior; disponibilidade real pode ser um limite, não apenas esforço | Incerto |
| TRADUÇÃO | ~81 livros, potencialmente 1M+ palavras de saída final | **Projeto de escala completamente diferente** — não deve ser iniciado como extensão automática da auditoria documental |
| REVISÃO / VALIDAÇÃO / QA / BUILD | Escala com o volume traduzido | Depende da fase anterior |

**Recomendação explícita para o próximo chat**: tratar "resolver fonte/direitos + pendências específicas" como o próximo marco terminável e razoável. Tratar o início da fase de TRADUÇÃO como uma **decisão separada e explícita do usuário**, não algo a iniciar por inércia ou suposição de escopo.

---

## 4. FONTES REGISTRADAS (docs/research/SOURCES_INITIAL.md)

| ID | Referência | Tipo |
|---|---|---|
| SRC-0001 | EOTC, "The Bible" (lista institucional, ethiopianorthodox.org) | PRIMARY/INSTITUTIONAL |
| SRC-0002 | Bruk A. Asale 2016, "Neither Open nor Closed" | ACADEMIC |
| SRC-0003 | Daniel Assefa 2022, Oxford Handbook | ACADEMIC |
| SRC-0004 | R. W. Cowley 1974, "The Biblical Canon of the EOC Today" | ACADEMIC |
| SRC-0005 | Peter Brandt 2000, "Geflecht aus 81 Büchern" | ACADEMIC |
| SRC-0006 | R. H. Charles 1895, edição crítica de Jubileus (Ge'ez) | PRIMARY/CRITICAL_EDITION — domínio público |
| SRC-0007 | R. H. Charles 1906, edição crítica de 1 Enoque (Ge'ez) | PRIMARY/CRITICAL_EDITION — domínio público |
| SRC-0008 | Michael Knibb 1978, edição crítica de 1 Enoque | ACADEMIC/CRITICAL_EDITION — direitos autorais modernos |
| SRC-0009 | James VanderKam 1989, edição crítica de Jubileus (CSCO) | ACADEMIC/CRITICAL_EDITION — direitos autorais modernos |

Não criar SRC-* novos sem necessidade e sem fonte documental real, seguindo a regra original.

---

## 5. QUESTÕES ESPECÍFICAS EM ABERTO (não resolver por suposição)

Registradas nas notas de `documentary_audit.json` das respectivas entradas:

- **OT-024/OT-025** (Proverbs / Tegsats): possível divisão tradicional "Mesale" (Prov 1-24) / "Tegsats" (Prov 25-31) aparece em literatura secundária, mas não foi confirmada contra fonte primária (acesso de rede bloqueado para os domínios relevantes nesta sessão — Wikipedia, islamic-awareness.org, translation.bible). Fronteira entre as duas entradas continua indefinida.
- **OT-030** (Jeremiah): nenhuma entrada separada existe para Lamentations/Baruch/Letter of Jeremiah. Literatura acadêmica descreve um agrupamento "Rest of Jeremiah" tratado como unidade no cânon de 46 livros — plausível que "Jeremiah" no inventário cubra esse conjunto mais amplo, mas não confirmado contra SRC-0001 diretamente.
- **OT-019** (Esther): confirmado academicamente que a tradição etíope segue a LXX e inclui as Adições a Ester — mas a extensão exata na forma etíope específica não foi verificada.
- **OT-032** (Daniel): confirmado que o cânon etíope inclui as Adições a Daniel (Susana, Bel e o Dragão, Cântico dos Três Jovens) — mas há variação documentada entre manuscritos/comentários Ge'ez quanto a quais adições aparecem e como.
- **OT-017** (Tobit): existem múltiplas recensões gregas (curta/longa) + testemunhos latinos/aramaicos; qual serviu de base à tradução etíope não foi identificado.
- **OT-015 vs OT-016**: "Ezra and Nehemiah" (OT-015) e "Ezra (2nd) and Ezra Sutuel" (OT-016) são entidades distintas — não confundir pela recorrência do nome "Ezra".

---

## 6. LIMITAÇÃO TÉCNICA DESTA SESSÃO

`WebFetch` foi bloqueado pelo proxy de rede do ambiente para múltiplos domínios testados (en.wikipedia.org, islamic-awareness.org, translation.bible). Apenas `WebSearch` funcionou (retorna resumos, não o texto primário). Isso limitou a verificação direta de algumas afirmações (ver seção 5) a conhecimento acadêmico geral bem estabelecido, sinalizado explicitamente como tal nas notas — nunca apresentado como citação primária confirmada. Uma futura sessão deve tentar novamente ou usar outro mecanismo de acesso caso precise confirmar essas citações diretamente.

---

## 7. PRÓXIMO PASSO SUGERIDO

1. Confirmar estado real do Git (`git status`, `git log`, `git branch`) — não presumir que nada mudou desde este handoff.
2. Escolher um lote de ~5-10 entradas para resolver `textual_source_available`/`rights_status` (ex.: começar pelas mais simples — Pentateuco, evangelhos — antes das mais complexas).
3. Pesquisar apenas esse lote; não reabrir identidade textual já corroborada sem razão concreta.
4. Atualizar `documentary_audit.json` apenas nos campos necessários (`textual_source_available`, `rights_status`, `note`).
5. Validar JSON, `git diff --check`, commit, push, merge para `main` (autorizado).
6. Atualizar este HANDOFF.md (não o README, que é resumo executivo) com o novo estado ao final do lote.
7. Repetir até esgotar as 79 entradas restantes ou até o usuário redirecionar prioridades.

**Não iniciar a fase de TRADUÇÃO sem decisão explícita do usuário**, dado o salto de escala descrito na seção 3.
