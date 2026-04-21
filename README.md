# NLP Triagem Inteligente Financeira

Projeto de **Processamento de Linguagem Natural (NLP)** aplicado ao domínio financeiro, com foco em **classificação multiclasses de perguntas e demandas textuais** e preparação para **deployment inicial com API e monitoramento básico**.

---

## 1. Visão Geral

Este projeto foi construído como um case de portfólio para demonstrar um ciclo completo de IA aplicada, desde o entendimento do problema até readiness para uso operacional.

A solução foi estruturada para responder a uma pergunta central:

> Como automatizar a triagem de demandas textuais no contexto financeiro, apoiando classificação, priorização e encaminhamento operacional?

O trabalho foi conduzido com uma abordagem **CRISP-DM+ Lean**, incorporando elementos de:

- **Ontologia de domínio**
- **BLM (Business Language Model)**
- **Hipóteses semânticas iniciais**
- **Pipeline analítico em camadas bronze / silver / gold**
- **Comparação entre baseline clássico e transformer**
- **Decisão técnica baseada em evidência**
- **Preparação para deployment com logging e monitoramento inicial**

---

## 2. Problema de Negócio

Instituições financeiras lidam diariamente com grande volume de perguntas, solicitações, reclamações e manifestações textuais vindas de canais como:

- aplicativo
- chat
- e-mail
- web
- call center

Quando a triagem dessas demandas depende fortemente de tratamento manual, surgem desafios como:

- aumento do tempo operacional
- inconsistência de classificação
- roteamento incorreto
- dificuldade de priorização
- baixa escalabilidade analítica

Este projeto propõe uma solução de NLP para apoiar a **triagem inteligente de textos financeiros**, com foco inicial em **classificação de categorias**.

---

## 3. Objetivo do Projeto

### Objetivo de negócio

Apoiar a automação da triagem textual no setor financeiro, aumentando consistência de classificação e reduzindo esforço operacional.

### Objetivo analítico

Desenvolver uma solução de NLP capaz de receber um texto livre e prever sua **categoria de demanda**.

### Objetivo técnico

Construir um pipeline completo com:

- entendimento de domínio
- preparação de dados
- baseline supervisionado
- experimento com transformer
- avaliação comparativa
- readiness para deployment inicial

---

## 4. Dataset

### Base principal

**FAQ_BACEN**

Dataset em português, do domínio financeiro, estruturado com:

- perguntas
- categorias
- respostas

Esse dataset foi escolhido por sua aderência ao problema, ao idioma e ao domínio regulatório-financeiro.

### Papel da base no projeto

A base foi usada para simular um cenário de triagem inteligente de demandas textuais financeiras, permitindo modelagem supervisionada multiclasses.

---

## 5. Abordagem Metodológica

O projeto foi estruturado em uma adaptação do **CRISP-DM+ Lean**.

### Etapa 0 — Domain Understanding+

- Ontologia mínima do domínio
- BLM (Business Language Model)
- Hipóteses semânticas iniciais

### Etapa 1 — Business Understanding

- definição do problema
- objetivos de negócio
- objetivos analíticos
- critérios de sucesso
- riscos e premissas

### Etapa 2 — Data Understanding

- leitura do dataset
- inspeção estrutural
- distribuição das classes
- leitura das características textuais

### Etapa 3 — Data Preparation

- limpeza textual controlada
- padronização de labels
- geração das camadas silver e gold
- preparação para baseline e transformer

### Etapa 4 — Modeling Baseline

- **TF-IDF + Logistic Regression**
- comparação entre configurações
- avaliação em validação e teste

### Etapa 5 — Modeling Advanced

- experimento com **transformer** para comparação com o baseline

### Etapa 6 — Evaluation & Business Interpretation

- comparação entre abordagens
- diagnóstico do comportamento do transformer
- decisão técnica final

### Etapa 7 — Deployment & Monitoring

- inferência local
- contrato de entrada e saída
- logging de predições
- monitoramento básico
- preparação para API REST

### Etapa 8 — Executive Conclusion

- fechamento executivo do case
- narrativa de portfólio
- empacotamento para README, HTML e entrevistas

---

## 6. Arquitetura Analítica

### Organização das camadas

```text
data/
├── 00-raw/
├── 01-bronze/
├── 02-silver/
├── 03-gold/
└── 04-inference/
```

### Organização do projeto

```text
nlp-triagem-inteligente-financeira/
├── notebooks/
├── src/
│   ├── api/
│   ├── domain/
│   ├── features/
│   ├── models/
│   └── monitoring/
├── data/
├── models/
│   ├── baseline/
│   └── transformer/
├── artifacts/
│   ├── reports/
│   ├── figures/
│   └── logs/
└── docs/
```

---

## 7. Notebooks do Projeto

| Notebook | Etapa                                | Entrega principal                             |
| -------- | ------------------------------------ | --------------------------------------------- |
| 01       | Business Understanding               | Problema, objetivos, Ontologia e BLM          |
| 02       | Data Understanding                   | Exploração inicial do FAQ_BACEN               |
| 03       | Data Preparation                     | Limpeza textual, labels e camadas silver/gold |
| 04       | Modeling Baseline                    | TF-IDF + Logistic Regression                  |
| 05       | Modeling Advanced                    | Experimento com transformer                   |
| 06       | Evaluation & Business Interpretation | Comparação, diagnóstico e decisão técnica     |
| 07       | Deployment & Monitoring              | Inferência, logging e API readiness           |
| 08       | Executive Conclusion                 | Encerramento executivo e empacotamento        |

---

## 8. Modelos Avaliados

### 8.1 Baseline

**TF-IDF + Logistic Regression**

#### Papel no projeto

Estabelecer uma linha de base robusta, interpretável e operacionalmente simples.

#### Pontos fortes

- treinamento leve
- boa interpretabilidade relativa
- baixo custo de serving
- bom comportamento multiclasses no contexto do projeto

---

### 8.2 Modelo Avançado

**Transformer para classificação textual**

#### Papel no projeto

Testar se uma abordagem contextual avançada entregaria ganho real sobre o baseline.

#### Hipótese

Melhorar a separação entre classes semanticamente próximas.

#### Resultado observado

O experimento **não se validou com sucesso** na formulação atual e colapsou para uma classe dominante.

---

## 9. Resultados Principais

### Comparação global no teste

| Modelo                                | Accuracy | Macro F1 | Weighted F1 | Macro Precision | Macro Recall |
| ------------------------------------- | --------:| --------:| -----------:| ---------------:| ------------:|
| Baseline TF-IDF + Logistic Regression | 0.3029   | 0.2368   | 0.3028      | 0.2557          | 0.2640       |
| Transformer                           | 0.1769   | 0.0021   | 0.0532      | 0.0012          | 0.0068       |

### Leitura dos resultados

A evidência quantitativa mostrou que:

- o **baseline apresentou desempenho significativamente superior**
- o **transformer não demonstrou ganho prático** na formulação atual
- a decisão correta foi preservar o modelo com melhor comportamento empírico

---

## 10. Diagnóstico do Transformer

O experimento com transformer foi importante porque mostrou, com clareza, um problema de formulação:

- o modelo previu apenas **uma única classe** no teste
- a classe dominante prevista foi **SEM-CATEGORIA**
- isso caracteriza **colapso para classe dominante**

### Interpretação correta

Esse resultado **não significa que transformers não funcionam para NLP financeiro**.

Ele indica que, nesta configuração específica:

- a granularidade do target está alta demais
- o espaço de classes está excessivamente pulverizado
- a formulação atual precisa de redesign antes de nova rodada

---

## 11. Decisão Técnica Final

### Modelo aprovado para deployment inicial

**Baseline TF-IDF + Logistic Regression**

### Justificativa

O baseline foi escolhido porque demonstrou:

- melhor qualidade preditiva observada
- melhor comportamento multiclasses
- menor complexidade operacional
- menor custo de serving
- maior previsibilidade para um MVP

### Status do transformer

O transformer permanece como:

- trilha futura de evolução
- hipótese técnica ainda não validada
- experimento relevante, mas não aprovado para o primeiro deployment

---

## 12. Deployment Inicial

O projeto foi preparado para um cenário inicial de deployment com:

- carregamento do pipeline salvo
- inferência local padronizada
- contrato mínimo de entrada e saída
- logging de predições
- monitoramento básico de uso
- preparação para API REST com FastAPI

### Endpoints planejados

- `POST /predict`
- `GET /health`
- `GET /model-info`

---

## 13. Monitoramento Inicial

Nesta primeira camada de deployment, o monitoramento foi pensado para acompanhar:

- volume de inferências
- distribuição das categorias previstas
- distribuição por canal de origem
- rastreabilidade por `request_id`

### Evoluções futuras

- delayed labels
- monitoramento de drift
- taxa de fallback humano
- análise de erro pós-tratativa

---

## 14. Stack Utilizada

### Linguagem e ambiente

- Python
- Jupyter Notebook

### Bibliotecas principais

- pandas
- numpy
- matplotlib
- scikit-learn
- transformers
- datasets
- joblib
- FastAPI
- Pydantic

### Organização analítica

- CRISP-DM+ Lean
- Ontologia de domínio
- BLM
- bronze / silver / gold

---

## 15. Principais Aprendizados

Este projeto gerou aprendizados técnicos importantes:

1. **Baseline forte continua sendo decisivo** em NLP aplicado
2. **Modelo mais complexo não deve ser promovido sem evidência**
3. **Granularidade do target importa muito** em tarefas multiclasses
4. **Diagnosticar falhas com honestidade fortalece o case**
5. **Deployment readiness agrega muito valor ao portfólio**

---

## 16. Como Apresentar Este Projeto em Entrevista

Uma forma madura de resumir o case é:

> Desenvolvi uma solução de NLP para triagem inteligente no contexto financeiro, estruturada desde o entendimento de domínio até readiness para deployment. Comparei um baseline clássico com um transformer, diagnostiquei o colapso do modelo avançado na formulação atual e mantive a decisão de deployment baseada em evidência, escolhendo o baseline pela melhor relação entre desempenho e simplicidade operacional.

---

## 17. Próximos Passos

### Trilha A — evolução do deployment

- implementar API FastAPI executável
- adicionar healthcheck e model-info
- robustecer logging
- criar dashboard simples de monitoramento

### Trilha B — evolução do transformer

- usar `question_raw`
- reduzir a granularidade do target
- agrupar classes raras
- repetir fine-tuning com taxonomia mais viável

---

## 18. Valor de Portfólio

Este case demonstra:

- capacidade de estruturar um problema real de NLP
- capacidade de comparar abordagens com rigor
- capacidade de documentar decisões com clareza
- capacidade de diagnosticar experimentos malsucedidos sem maquiar resultado
- capacidade de preparar uma solução para uso operacional inicial

Em outras palavras, este projeto não mostra apenas modelagem.
Mostra **método, maturidade analítica, visão de produto e prontidão para deployment**.

---

## 19. Autor

**Roberto dos Santos Soares**  
Profissional de Dados | BI | Analytics | Data Science | Engenharia de Dados  
[LinkedIn](https://www.linkedin.com/in/roberto-dos-santos-soares/)  
[Portfólio](https://roberto-ssoares.github.io/meu-portfolio/)

---

## 20. Observação Final

O ponto mais forte deste projeto não é apenas o baseline ter vencido.

O ponto mais forte é que a decisão final foi tomada com base em:

- evidência quantitativa
- diagnóstico técnico
- simplicidade operacional
- coerência com o objetivo de negócio

Esse é exatamente o tipo de raciocínio que diferencia um experimento de notebook de uma solução com potencial real de uso.
