import json
from typing import NamedTuple
from utils_vertex_llm import llm_predict
from utils_app_builder import search
from google.cloud import logging

logging_client = logging.Client()


class InfobotAnswerArgs(NamedTuple):
    search_query: str
    search_filter: str
    last_query: str
    context: str
    negative_response: str


def answer_infobot(args: InfobotAnswerArgs):
    logger = logging_client.logger("webhook_enterprise_search")
    search_results = search(args.search_query, args.search_filter)
    if not search_results or not search_results[0].get("long_snippet"):
        return args.negative_response, search_results

    search_result_text = "\n".join(
        [
            json.dumps(result, ensure_ascii=False).encode("utf-8").decode()
            for result in search_results
        ]
    )
    prompt = args.context.format(
        last_query=args.last_query,
        search_query=args.search_query,
        search_results=search_result_text,
    )
    response = llm_predict(
        model_name="text-bison-32k",
        temperature=0.2,
        max_output_tokens=1024,
        top_p=0.9,
        top_k=40,
        content=prompt,
    )
    logger.log_text("Response: " + response)
    return response, search_results
