BLM_TERMS = {
    "fatura": "Documento de cobrança relacionado ao produto financeiro.",
    "limite": "Valor disponível ou teto operacional do produto.",
    "contestação": "Pedido de revisão de cobrança, compra ou transação.",
    "fraude": "Indício de uso indevido, transação não reconhecida ou comportamento suspeito.",
    "bloqueio": "Impedimento temporário ou definitivo de uso do produto ou conta.",
    "cobrança indevida": "Valor cobrado que o cliente considera incorreto.",
    "renegociação": "Pedido de revisão de condições de pagamento ou dívida.",
    "atraso": "Situação de não pagamento dentro do prazo esperado.",
    "atendimento": "Interação operacional com canal, agente ou processo.",
    "cancelamento": "Solicitação de encerramento de produto, serviço ou operação.",
}


def get_blm_terms() -> dict:
    return BLM_TERMS


def get_blm_term_list() -> list[str]:
    return list(BLM_TERMS.keys())


    