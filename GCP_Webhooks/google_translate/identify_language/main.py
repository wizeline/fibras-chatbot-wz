import functions_framework
from flask import Request
import utils_dialogflow as dgflow
from utils_translate import identify_language


@functions_framework.http
def process_request(request: Request):
    webhook_request = dgflow.json_to_webhook_request(request.json)
    text = dgflow.text_from_webhook_request(webhook_request)
    print(f'Received text: {text}.')
    detected_language = identify_language(text)
    print(f'Language identified: {detected_language}')
    webhook_response = dgflow.build_webhook_response({'user_input_language': detected_language})
    return webhook_response
