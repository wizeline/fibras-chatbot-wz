import json
from typing import Union
from google.cloud.dialogflowcx_v3.types import WebhookRequest, WebhookResponse
from utils_translate import TranslateArgs


def json_to_webhook_request(request_json: Union[dict, str, None]) -> WebhookRequest:
    if request_json:
        if isinstance(request_json, dict):
            request_json = json.dumps(request_json)
        if isinstance(request_json, str):
            return WebhookRequest.from_json(
                request_json, ignore_unknown_fields=True)
    return WebhookRequest()


def translate_args_from_webhook_request(webhook_request: WebhookRequest) -> TranslateArgs:
    parameters = webhook_request.session_info.parameters
    target = parameters.get('user_input_language')
    text = parameters.get('text')
    return TranslateArgs(target=target, text=text)


def build_webhook_response(parameters: dict) -> WebhookResponse:
    webhook_response = WebhookResponse()
    for key, value in parameters.items():
        webhook_response.session_info.parameters[key] = value
    return json.loads(WebhookResponse.to_json(webhook_response))
