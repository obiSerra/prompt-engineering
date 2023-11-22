from prompt_egineering.gpt_client import GptClient
from prompt_egineering.prompts import Prompt


if __name__ == "__main__":
    client = GptClient()

    test_prompt = Prompt(prompt="Say 'Hello World' in French")

    print(client.complete(test_prompt))
