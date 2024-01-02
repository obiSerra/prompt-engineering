from pydantic import BaseModel, Field


class Prompt(BaseModel):
    content: str = Field(..., title="Prompt", description="The prompt to send to the GPTAPI")
    role: str = Field("user", title="Role", description="The role of the prompt")


class SystemPrompt(Prompt):
    role: str = Field("system", title="Role", description="The role of the prompt")
