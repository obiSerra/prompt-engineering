import json
import logging
import re

from prompt_engineering.gpt_client import GptClient
from prompt_engineering.prompts import Prompt
from prompt_engineering.response_models import (DocumentResponse,
                                                QuoteResponse, SummaryResponse)
from prompt_engineering.utils import get_page_content, load_template
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def scrape_page():
    # TODO get url from user
    url = "https://stackoverflow.blog/2019/09/30/how-to-make-good-code-reviews-better/"

    page_content = get_page_content(url)

    client = GptClient()

    # TODO improve system prompt
    system_prompt = Prompt(
        content="""# MISSION
        Retrieve all the information from the provided sources.
        Do not add any information that is not in the sources.
        """
    )

    user_prompt = Prompt(
        content=f"""Given the following article, write a list of the most important points in the article.
        For each point add a relevant quote from the article.
        Format the answer as JSON following this structure {{\n"points": [{{\n"point": ...,"quote": ...}},\n...\n]\n}}'
        \n\n{url}\n"""
    )
    resp = client.complete(user_prompt, system_prompt=system_prompt)

    quote_resp = QuoteResponse(**json.loads(f"{resp}"))

    second_step_prompt = Prompt(
        content="""Starting from the list of points and quotes, write a summary of the article.
                                Format the answer as JSON following this structure {{\n"summary": ...\n}}"""
    )

    resp = client.complete(second_step_prompt, new_context=False)

    summary_resp = SummaryResponse(**json.loads(f"{resp}"))

    print(
        f"""Summary:
{summary_resp}

Points and quotes:
{quote_resp}"""
    )


# def gen_document(key_points, tone="objective", style="Wikipedia Article", section="Article"):
def gen_document(prompt: str):
    client = GptClient()

    # TODO improve system prompt
    system_prompt = Prompt(content=load_template("doc_system_prompt.txt"))

    # doc = DocumentPrompt(
    #     key_points=key_points,
    #     tone=tone,
    #     style=style,
    #     section=section,
    # )

    user_prompt = Prompt(content=prompt)
    resp = client.complete(user_prompt, system_prompt=system_prompt)
    doc_resp = DocumentResponse(**resp.model_dump())
    print(doc_resp)


# TODO validate quotes and parse response
# TODO add chain of thought


if __name__ == "__main__":
    # scrape_page()
    # gen_document()
    print("Hello world")
