import json
from typing import List, Union, Tuple
from utils_answer import InfobotAnswerArgs
from google.cloud.dialogflowcx_v3.types import WebhookRequest, WebhookResponse
from google.cloud.dialogflowcx_v3.types import response_message

REPLACE = WebhookResponse.FulfillmentResponse.MergeBehavior.REPLACE


def json_to_webhook_request(request_json: Union[dict, str, None]) -> WebhookRequest:
    if request_json:
        if isinstance(request_json, dict):
            request_json = json.dumps(request_json)
        if isinstance(request_json, str):
            return WebhookRequest.from_json(request_json, ignore_unknown_fields=True)

    return WebhookRequest()


def process_infobot_webhook_request(request: WebhookRequest) -> InfobotAnswerArgs:
    parameters = request.session_info.parameters
    if request.text:
        search_query = request.text
    elif request.transcript:
        search_query = request.transcript
    else:
        search_query = parameters.get("search_query", "")

    search_filter = parameters.get("search_filter", "")
#     if "$the_dni" in search_filter:
#         dni = parameters.get("dni", "")
#         fixed_dni = ""
#         if isinstance(dni, int):
#             fixed_dni = f"{dni:08d}"
#         if isinstance(dni, float):
#             fixed_dni = f"{int(dni):08d}"
#         if isinstance(dni, str):
#             fixed_dni = dni
#         search_filter.replace("$the_dni", fixed_dni)

    args = InfobotAnswerArgs(
        search_query=search_query,
        search_filter=search_filter,
        last_query=parameters.get("last_query", ""),
        context=parameters.get("context", ""),
        negative_response=parameters.get("negative_response", ""),
    )
    return args


def format_infobot_webhook_response(
    response: str, search_results: list, infobot_args: InfobotAnswerArgs, session_id: str
) -> WebhookResponse:
    webhook_response = WebhookResponse()
    webhook_response.fulfillment_response.merge_behavior = REPLACE
    message_text = response_message.ResponseMessage()
    message_text.text = response_message.ResponseMessage.Text(text=[response])
#     message_text.response_type = response_message.ResponseMessage.ResponseType("ENTRY_PROMPT")
    webhook_response.fulfillment_response.messages.append(message_text)
    message_rich = response_message.ResponseMessage()
    message_rich.payload = {
        "richContent": [
            [
                {
                    "type": "info",
                    "title": result.get("title"),
                    "subtitle": result.get("snippet"),
                    "actionLink": result.get("link"),
                }
            ]
            for result in search_results
        ]
    }
    webhook_response.fulfillment_response.messages.append(message_rich)
    webhook_response.session_info.session = session_id
    webhook_response.session_info.parameters["last_query"] = (
        f"Q:{infobot_args.search_query} " f"A:{response}"
    )
    return json.loads(WebhookResponse.to_json(webhook_response))


def format_conversational_webhook_response(
    response: str, history: List[Tuple[str, str]]
) -> WebhookResponse:
    webhook_response = WebhookResponse()
    webhook_response.fulfillment_response.merge_behavior = REPLACE
    message_text = response_message.ResponseMessage()
    message_text.text = response_message.ResponseMessage.Text(text=[response])
    webhook_response.fulfillment_response.messages.append(message_text)
    webhook_response.session_info.parameters["history"] = history
    return json.loads(WebhookResponse.to_json(webhook_response))
