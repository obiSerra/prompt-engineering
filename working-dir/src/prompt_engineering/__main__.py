import logging

from prompt_engineering.gpt_client import GptClient
from prompt_engineering.prompts import Prompt
from prompt_engineering.response_models import DocumentResponse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# def gen_document(key_points, tone="objective", style="Wikipedia Article", section="Article"):
def gen_document(prompt: str):
    client = GptClient()

    # TODO improve system prompt
    # system_prompt = Prompt(content=load_template("doc_system_prompt.txt"))

    default_system_prompt = (
        "Generate a text using the information provided; only generate the text without any additional information."
    )

    system_prompt = Prompt(content=default_system_prompt)
    user_prompt = Prompt(content=prompt)
    resp = client.complete(user_prompt, system_prompt=system_prompt)
    doc_resp = DocumentResponse(**resp.model_dump())
    print("\n\n" + doc_resp)


# TODO validate quotes and parse response
# TODO add chain of thought


if __name__ == "__main__":
    print("Please use the CLI.")
