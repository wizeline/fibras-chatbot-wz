import functions_framework
from flask import Request
import utils_dialogflow as dgflow
from utils_translate import translate_text_per_tag


@functions_framework.http
def process_request(request: Request):
    webhook_request = dgflow.json_to_webhook_request(request.json)
    translate_args = dgflow.translate_args_from_webhook_request(webhook_request)
    print(f'Received destination language: {translate_args.target}. Text: {translate_args.text}')
    translated_text = translate_text_per_tag(
        webhook_request.fulfillment_info.tag,
        translate_args)
    print(f'Translated text: {translated_text}')
    webhook_response = dgflow.build_webhook_response({'translated_text': translated_text})
    return webhook_response
