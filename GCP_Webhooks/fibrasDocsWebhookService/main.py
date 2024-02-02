from utils_answer import answer_infobot
from utils_dialogflow import process_infobot_webhook_request
from utils_dialogflow import json_to_webhook_request
from utils_dialogflow import format_infobot_webhook_response
import functions_framework
from flask import Request
from google.cloud import logging

logging_client = logging.Client()


@functions_framework.http
def dialogflow_request(request: Request):
    request_json = request.get_json(silent=True)
    logger = logging_client.logger("webhook_enterprise_search")
    logger.log_struct(request_json)
    if request_json and "fulfillmentInfo" in request_json:
        webhook_request = json_to_webhook_request(request_json)

        infobot_args = process_infobot_webhook_request(webhook_request)
        response, search_results = answer_infobot(infobot_args)
        session_id = request_json["sessionInfo"]["session"]
        webhook_response = format_infobot_webhook_response(
            response, search_results, infobot_args, session_id
        )
        logger.log_struct(webhook_response)
        return webhook_response
