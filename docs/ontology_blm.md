# Ontologia e BLM — NLP Triagem Inteligente Financeira

## Objetivo

Este documento registra a camada inicial de entendimento do domínio do projeto, utilizando uma abordagem CRISP-DM+ Lean com foco em:

- Ontologia mínima do domínio
- BLM (Business Language Model)
- Hipóteses semânticas para NLP aplicado

---

## 1. Ontologia mínima do domínio

A ontologia mínima foi desenhada para representar os principais elementos envolvidos no processo de triagem textual no contexto financeiro.

### Entidades principais

- **Cliente**: pessoa que origina a manifestação, reclamação ou solicitação.
- **Demanda**: texto livre contendo a necessidade, problema ou dúvida.
- **Produto**: serviço ou produto financeiro ao qual a demanda se refere.
- **Canal**: origem da demanda, como aplicativo, telefone, e-mail ou chat.
- **Categoria**: classe principal atribuída à demanda.
- **Prioridade**: nível de urgência operacional da demanda.
- **Atendimento**: fluxo humano ou automatizado de tratamento.
- **Encaminhamento**: destino operacional responsável pela tratativa.

### Relações principais

- Cliente **abre** Demanda
- Demanda **refere-se a** Produto
- Demanda **chega por** Canal
- Demanda **recebe** Categoria
- Demanda **recebe** Prioridade
- Demanda **é tratada em** Atendimento
- Demanda **é encaminhada para** Encaminhamento

---

## 2. BLM — Business Language Model

O BLM organiza a linguagem operacional do negócio presente nos textos e ajuda a reduzir ambiguidades na etapa de modelagem.

### Glossário inicial

- **fatura**: documento de cobrança relacionado ao produto financeiro
- **limite**: valor disponível ou teto operacional do produto
- **contestação**: pedido de revisão de cobrança, compra ou transação
- **fraude**: indício de uso indevido ou transação não reconhecida
- **bloqueio**: impedimento temporário ou definitivo de uso
- **cobrança indevida**: valor cobrado considerado incorreto pelo cliente
- **renegociação**: revisão de condições de pagamento ou dívida
- **atraso**: não pagamento dentro do prazo esperado
- **atendimento**: interação com canal, agente ou processo
- **cancelamento**: solicitação de encerramento de produto ou serviço

---

## 3. Hipóteses semânticas iniciais

- Termos relacionados a cobrança, fatura e vencimento tendem a formar grupos semânticos próximos.
- Mensagens de fraude e transação não reconhecida devem apresentar vocabulário distintivo.
- Algumas categorias operacionais podem apresentar sobreposição semântica parcial.
- Textos muito curtos podem reduzir a capacidade discriminativa do modelo.
- Pode haver potencial para priorização adicional a partir de termos de urgência e risco.

---

## 4. Papel desta camada no projeto

Esta camada será usada para:

- orientar a leitura exploratória dos dados
- apoiar a definição das classes-alvo
- ajudar na revisão de rótulos
- melhorar a interpretação dos erros do modelo
- fortalecer a documentação do portfólio
