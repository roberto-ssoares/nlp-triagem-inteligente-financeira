<<<<<<< HEAD
# NLP Triagem Inteligente Financeira

## CRISP-DM+ Lean: abordagem orientada por Ontologia, BLM e Semântica para NLP aplicado

Construir uma solução end-to-end de NLP para classificar, priorizar e apoiar o encaminhamento de demandas textuais de clientes do setor financeiro.

---

## Objetivo do projeto

Este projeto demonstra, de ponta a ponta, a construção de uma solução de Inteligência Artificial aplicada ao negócio, com foco em Processamento de Linguagem Natural (NLP), modelagem, avaliação, disponibilização via API REST e monitoramento inicial de inferência.

---

## Problema de negócio

Operações de atendimento e backoffice frequentemente recebem grandes volumes de mensagens, reclamações e solicitações em texto livre. A triagem manual desses conteúdos tende a ser:

- lenta
- inconsistente
- cara operacionalmente
- sensível a erro humano

A proposta deste projeto é desenvolver uma solução capaz de apoiar a automação dessa triagem textual, aumentando consistência, velocidade e capacidade analítica.

---

## Questão central

Como automatizar a triagem de textos no contexto financeiro para apoiar classificação, priorização e encaminhamento de demandas?

---

## Abordagem metodológica

Este projeto utiliza uma adaptação do framework **CRISP-DM+ Lean**, incorporando na etapa inicial:

- **Ontologia de domínio**
- **BLM (Business Language Model)**
- **Exploração semântica inicial**

Essa abordagem busca reduzir ambiguidade de negócio antes da modelagem e fortalecer a conexão entre linguagem operacional, classes analíticas e arquitetura da solução.

---

## Escopo técnico

A solução será construída em etapas:

1. Entendimento do domínio e do problema
2. Entendimento e exploração dos dados textuais
3. Preparação e limpeza dos textos
4. Baseline com **TF-IDF + Logistic Regression**
5. Modelo avançado com **Transformer**
6. Avaliação técnica e interpretação de negócio
7. Disponibilização do modelo via **FastAPI**
8. Logging e monitoramento inicial de inferência

---

## Estrutura do projeto

```text
nlp-triagem-inteligente-financeira/
├── data/
├── notebooks/
├── src/
├── models/
├── artifacts/
├── docs/
├── tests/
└── app/
```

## Stack principal

- Python 3.12
- Pandas
- Scikit-learn
- Transformers
- PyTorch
- FastAPI
- DuckDB
- Streamlit

---

## Entregáveis esperados

- notebooks analíticos e de modelagem
- baseline clássico de NLP
- modelo avançado com transformer
- API REST para inferência
- logs de monitoramento
- documentação premium para portfólio

---

## Status do projeto

**Em construção — Sprint 0 / Setup e definição metodológica**

---

## Próximos passos

- definir dataset
- estabelecer classes-alvo
- montar Notebook 01
- preparar pipeline baseline
- construir API inicial

---  

# 7. Primeiro commit ideal

Depois disso:  

```powershell
git add . 
git commit -m "chore: bootstrap inicial do projeto NLP com estrutura CRISP-DM+ Lean" 
git push origin main
```

---

---

# 8. O que eu recomendo fazermos na sequência

Agora o próximo passo mais importante não é código pesado ainda.

É definir **a base analítica do case**:

## Precisamos fechar 3 coisas

- **dataset**
- **coluna textual principal**
- **classes-alvo**

Minha recomendação para o MVP é:

### Entrada

texto de reclamação, chamado ou manifestação

### Saída principal

**categoria da demanda**

### Saída secundária opcional

**prioridade da demanda**

Assim o projeto fica elegante e realista sem explodir o escopo.

---

# 9. Sprint 1 que eu abriria com você

Assim que você confirmar que essa base subiu no GitHub, eu te entrego:

## `Notebook 01 — Business Understanding + CRISP-DM+ Lean`

com:

- markdown célula por célula
- objetivo
- ações realizadas
- justificativa técnica
- resultados esperados

e também já monto:

- `docs/ontology_blm.md`
- `src/domain/ontology.py`
- `src/domain/blm_glossary.py`

---

# 10. Dataset

https://huggingface.co/datasets/Itau-Unibanco/FAQ_BACEN/resolve/main/df_train.csv
=======
# CRISP-DM+ Lean: abordagem orientada por Ontologia, BLM e Semântica para NLP aplicado

## Construir uma solução end-to-end de NLP para classificar, priorizar e encaminhar demandas textuais de clientes do setor financeiro.
>>>>>>> f493524540b60a97c37f29b8f0041ab92464aa48
