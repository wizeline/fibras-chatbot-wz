from typing import NamedTuple
from google.cloud import translate_v3 as translate
from utils_config import PROJECT_ID

translate_client = translate.TranslationServiceClient()


class TranslateArgs(NamedTuple):
    target: str
    text: str


def translate_text(args: TranslateArgs, destination_language = None) -> dict:
    if isinstance(args.text, bytes):
        args.text = args.text.decode("utf-8")

    if not destination_language:
        destination_language = args.target

    request = translate.TranslateTextRequest(
        contents=[args.text],
        target_language_code=destination_language,
        parent=f'projects/{PROJECT_ID}')
    response = translate_client.translate_text(request=request)
    translated_text = response.translations[0].translated_text
    return translated_text


def translate_text_per_tag(tag: str, translate_args: TranslateArgs) -> str:
    user_language_code = translate_args.target
    text_to_translate = translate_args.text

    if tag == 'user_text':
        if user_language_code == "es":
            translated_text = text_to_translate
        else:
            translated_text = translate_text(translate_args, "es")
    elif tag == 'vertex_response':
        if user_language_code != "es":
            translated_text = translate_text(translate_args)
        else:
            translated_text = text_to_translate
    else:
        raise ValueError('Invalid tag')
    return translated_text
