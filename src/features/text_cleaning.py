import re
import unicodedata


def strip_accents(text: str) -> str:
    text = unicodedata.normalize("NFKD", str(text))
    return "".join(ch for ch in text if not unicodedata.combining(ch))


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip()


def remove_punctuation_keep_alnum(text: str) -> str:
    return re.sub(r"[^\w\s]", " ", str(text))


def clean_text_for_baseline(text: str) -> str:
    text = str(text).strip().lower()
    text = strip_accents(text)
    text = remove_punctuation_keep_alnum(text)
    text = normalize_whitespace(text)
    return text


def clean_text_light(text: str) -> str:
    text = str(text).strip().lower()
    text = normalize_whitespace(text)
    return text


    