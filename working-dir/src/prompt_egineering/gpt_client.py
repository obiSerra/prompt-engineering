from openai import OpenAI
from prompt_egineering.prompts import Prompt, SystemPrompt
from prompt_egineering.response_models import GptResponse


class GptClient:
    def __init__(self, model="gpt-3.5-turbo"):
        api_key = open("key.txt", "r").read().strip("\n")

        self.model = model

        # defaults to os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(
            api_key=api_key,
        )

    def complete(self, prompt: Prompt, system_prompt: SystemPrompt = None):
        messages = []

        if system_prompt:
            messages.append(dict(system_prompt))
        messages.append(dict(prompt))
        resp = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
        )

        return self._parse_response(resp)

    def _parse_response(self, resp):
        return GptResponse(**dict(resp))
