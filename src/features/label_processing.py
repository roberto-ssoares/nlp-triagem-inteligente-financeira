import re


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip()


def normalize_label(label: str) -> str:
    return normalize_whitespace(str(label))


def build_label_mapping(labels: list[str]) -> tuple[dict, dict]:
    label_list = sorted(set(labels))
    label_to_id = {label: idx for idx, label in enumerate(label_list)}
    id_to_label = {idx: label for label, idx in label_to_id.items()}
    return label_to_id, id_to_label


    