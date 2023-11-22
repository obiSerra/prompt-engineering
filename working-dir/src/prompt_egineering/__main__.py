from prompt_egineering.gpt_client import GptClient
from prompt_egineering.prompts import Prompt


if __name__ == "__main__":
    client = GptClient()

    with open("panna-cotta.txt", "r") as f:
        recipe = f.read()

    test_prompt = Prompt(
        content=f"""Given the following recipe, list the ingredients needed to make it. Only list ingredients,
        avoid mentioning any tool or intermediary products \n\n{recipe}"""
    )

    system_prompt = Prompt(
        content="Your task is to extract information from a given text. Reply only with a numbered list sorted by the order of appearance in the text."
    )

    print(client.complete(test_prompt, system_prompt=system_prompt))
