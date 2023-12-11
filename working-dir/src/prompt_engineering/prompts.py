from pydantic import BaseModel, Field


class Prompt(BaseModel):
    content: str = Field(..., title="Prompt", description="The prompt to send to the GPTAPI")
    role: str = Field("user", title="Role", description="The role of the prompt")


class SystemPrompt(Prompt):
    role: str = Field("system", title="Role", description="The role of the prompt")


class DocumentPrompt(BaseModel):
    key_points: list[str] = Field(..., title="Key Points", description="The key points of the document")
    tone: str = Field(..., title="Tone", description="The tone of the document")
    style: str = Field(..., title="Style", description="The style of the document")
    section: str = Field(..., title="Section", description="The section of the document")

    def __str__(self):
        return f"""
    Key points: {self.key_points}
    Tone: {self.tone}
    Style: {self.style}
    Section: {self.section}
    """
