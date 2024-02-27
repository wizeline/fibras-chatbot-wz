from typing import NamedTuple
from google.cloud import translate_v3 as translate
from utils_config import PROJECT_ID

translate_client = translate.TranslationServiceClient()

def identify_language(text: str) -> dict:
    if isinstance(text, bytes):
        text = text.decode("utf-8")

    request = translate.DetectLanguageRequest(
        content=text,
        parent=f'projects/{PROJECT_ID}',
    )
    response = translate_client.detect_language(request=request)
    language_code = response.languages[0].language_code
    return language_code