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

### Marco concluído — auditoria documental completa (81/81)

O bloco NT-001 a NT-027 foi investigado antes de qualquer alteração: `canon_inventory.json` já continha essas 27 entradas (Matthew a Revelation — o conjunto padrão de 27 livros do Novo Testamento, universalmente reconhecido, incluindo pela tradição etíope), simplesmente ainda não processadas em `textual_identity.json`/`documentary_audit.json`. Não se tratava de uma decisão arquitetural deliberada de exclusão, mas de trabalho ainda não realizado — confirmado antes de agir, conforme exigia o handoff original.

Como esse conjunto de 27 livros não apresenta disputas de identidade nominal ou textual em nenhuma tradição cristã (diferentemente dos livros do "cânon amplo" já auditados, como Sinodos, Livros da Aliança, Clemente e Didascalia etíopes), as 27 entradas foram:

1. Registradas em `textual_identity.json` (status `HIGH_CONFIDENCE`);
2. Auditadas em `documentary_audit.json` (LEVEL 2 / `ACADEMICALLY_CORROBORATED`, fontes SRC-0001 e SRC-0004).

**Com isso, `textual_identity.json` e `documentary_audit.json` chegam a 81/81 entradas — a totalidade do núcleo canônico (46 OT + 35 NT) possui registro de identidade textual e auditoria documental.**

### O que "concluído" significa aqui — e o que NÃO significa

Esta conclusão refere-se estritamente à **Camada B (identidade) e à corroboração documental inicial (LEVEL 2)** de todas as 81 entradas do núcleo canônico, conforme a arquitetura definida no princípio do projeto:

```
CANON → 81 ENTRADAS → TEXTUAL IDENTITY → DOCUMENTARY AUDIT → TEXTUAL SOURCE / RIGHTS STATUS → CORPUS READY → PT-BR
```

Isso **não** significa que o projeto de tradução esteja concluído. Para a esmagadora maioria das 81 entradas:

- `textual_source_available` permanece `TO_BE_VERIFIED` (exceto Jubilees e 1 Enoch, marcadas `AVAILABLE` por terem edições críticas confirmadas);
- `rights_status` permanece `TO_BE_VERIFIED` (ou `MIXED_TO_BE_VERIFIED` para Jubilees/1 Enoch);
- Nenhuma entrada atingiu LEVEL 3 (verificação textual-crítica completa contra manuscrito/edição);
- Nenhum trabalho de corpus ou tradução foi iniciado, pois a regra de tradução do projeto exige `IDENTIDADE >= LEVEL 2` **e** `FONTE TEXTUAL DISPONÍVEL = SIM` **e** `DIREITOS/LICENÇA = RESOLVIDOS` — condições ainda não satisfeitas para o corpus como um todo.

Também permanecem em aberto, registradas nas notas de auditoria correspondentes, questões específicas que exigem pesquisa dedicada antes de qualquer trabalho textual:
- fronteira entre OT-024 (Proverbs) e OT-025 (Tegsats);
- extensão exata do agrupamento "Rest of Jeremiah" em OT-030;
- forma exata das Adições a Ester (OT-019) e a Daniel (OT-032) na versão etíope;
- qual recensão de Tobit (OT-017) serviu de base à tradução etíope;
- direitos de uso das edições críticas modernas de Jubilees/1 Enoch (VanderKam 1989, Knibb 1978).

### Estado da auditoria

- Inventário canônico total: 81 entradas
- `textual_identity.json`: 81 entradas (81/81)
- `documentary_audit.json`: 81 entradas (81/81)
- Entradas com `textual_source_available = AVAILABLE`: 2 (OT-013 Jubilees, OT-014 1 Enoch)
- Entradas com verificação LEVEL 3: 0

### Próximo passo

A auditoria documental de identidade (Camadas A e B, mais corroboração inicial LEVEL 2) está completa para as 81 entradas do núcleo canônico. As próximas etapas possíveis, em ordem de dependência, são:

1. **Resolver `textual_source_available` e `rights_status` individualmente** para cada entrada — isso exige pesquisa dedicada por obra (edições críticas, manuscritos digitalizados, domínio público vs. direitos autorais modernos), não pode ser feito em lote genérico como a identidade textual.
2. **Resolver as questões em aberto** listadas acima (fronteira Proverbs/Tegsats, extensão de Jeremiah, forma das Adições, recensão de Tobit) antes de qualquer trabalho de corpus nessas entradas específicas.
3. Somente depois disso, iniciar a fase de CORPUS/TRADUÇÃO para as entradas que satisfizerem as três condições da regra de tradução (LEVEL >= 2, fonte disponível, direitos resolvidos).

Nenhuma dessas etapas deve ser executada em lote ou por suposição — cada uma exige verificação documental própria, seguindo o mesmo rigor aplicado até aqui.

### Handoff de continuidade

Para retomar o trabalho em uma nova sessão, ler primeiro `docs/research/HANDOFF.md` — contém o estado detalhado, estimativa de escopo restante e limitações técnicas encontradas nesta rodada (bloqueio de acesso de rede a alguns domínios de pesquisa).
