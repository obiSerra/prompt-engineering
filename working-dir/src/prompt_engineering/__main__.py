from prompt_engineering.gpt_client import GptClient
from prompt_engineering.prompts import Prompt
import requests

from bs4 import BeautifulSoup

# TODO validate quotes and parse response
# TODO add chain of thought


def get_page_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for script in soup.find_all("script"):
        script.decompose()
    for svg in soup.find_all("svg"):
        svg.decompose()
    for foot in soup.find_all("footer"):
        foot.decompose()
    # soup.script.decompose()
    # soup.style.decompose()
    # soup.img.decompose()
    return soup.find("body").text


if __name__ == "__main__":
    # TODO get url from user
    url = "https://stackoverflow.blog/2019/09/30/how-to-make-good-code-reviews-better/"
    page_content = get_page_content(url)

    client = GptClient()

    # TODO improve system prompt
    system_prompt = Prompt(
        content="""Your task is to extract information and summarize a text.
                Reply with a short summary and a list of the five most important points"""
    )

    user_prompt = Prompt(
        content=f"""Given the following article, write a short summary of it and a list of the five most important points.
        For each point quote the relevant text from the article.
        \n\n```{page_content}```\n\n"""
    )

    print(client.complete(user_prompt, system_prompt=system_prompt))
