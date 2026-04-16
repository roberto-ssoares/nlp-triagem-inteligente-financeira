from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class OntologyEntity:
    name: str
    description: str


@dataclass(frozen=True)
class OntologyRelation:
    source: str
    relation: str
    target: str


ONTOLOGY_ENTITIES: List[OntologyEntity] = [
    OntologyEntity("Cliente", "Pessoa que origina a manifestação, reclamação ou solicitação."),
    OntologyEntity("Demanda", "Texto livre contendo a necessidade, problema ou dúvida."),
    OntologyEntity("Produto", "Serviço ou produto financeiro ao qual a demanda se refere."),
    OntologyEntity("Canal", "Origem da demanda, como app, telefone, e-mail ou chat."),
    OntologyEntity("Categoria", "Classe principal atribuída à demanda."),
    OntologyEntity("Prioridade", "Nível de urgência operacional da demanda."),
    OntologyEntity("Atendimento", "Fluxo humano ou automatizado de tratamento da demanda."),
    OntologyEntity("Encaminhamento", "Destino operacional responsável pela tratativa."),
]

ONTOLOGY_RELATIONS: List[OntologyRelation] = [
    OntologyRelation("Cliente", "abre", "Demanda"),
    OntologyRelation("Demanda", "refere-se a", "Produto"),
    OntologyRelation("Demanda", "chega por", "Canal"),
    OntologyRelation("Demanda", "recebe", "Categoria"),
    OntologyRelation("Demanda", "recebe", "Prioridade"),
    OntologyRelation("Demanda", "é tratada em", "Atendimento"),
    OntologyRelation("Demanda", "é encaminhada para", "Encaminhamento"),
]


def get_entity_names() -> List[str]:
    return [entity.name for entity in ONTOLOGY_ENTITIES]


def get_relations_as_tuples() -> List[tuple]:
    return [(rel.source, rel.relation, rel.target) for rel in ONTOLOGY_RELATIONS]


    