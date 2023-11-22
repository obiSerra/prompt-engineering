from openai import OpenAI
from prompt_egineering.prompts import Prompt
from prompt_egineering.response_models import GptResponse


class GptClient:
    def __init__(self):
        api_key = open("key.txt", "r").read().strip("\n")

        self.model = "gpt-3.5-turbo"

        # defaults to os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(
            api_key=api_key,
        )

    def complete(self, prompt: Prompt, role="user"):
        resp = self.client.chat.completions.create(
            messages=[
                {
                    "role": prompt.role,
                    "content": prompt.prompt,
                }
            ],
            model=self.model,
        )

        return self._parse_response(resp)

    def _parse_response(self, resp):
        return GptResponse(**dict(resp))
