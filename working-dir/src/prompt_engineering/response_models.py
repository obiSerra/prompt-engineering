from pydantic import BaseModel, Field, root_validator


class ChatCompletionMessage(BaseModel):
    content: str = Field(..., title="Content", description="The content of the message")
    role: str = Field(..., title="Role", description="The role of the message")


class Choice(BaseModel):
    finish_reason: str = Field(..., title="Finish Reason", description="The reason the completion finished")
    index: int = Field(..., title="Index", description="The index of the completion")
    message: ChatCompletionMessage = Field(..., title="Message", description="The message of the completion")

    @root_validator(pre=True)
    def load_response(cls, values):
        values["message"] = dict(values["message"])

        return values


class CompletionUsage(BaseModel):
    completion_tokens: int = Field(..., title="Completion Tokens", description="The number of tokens in the completion")
    prompt_tokens: int = Field(..., title="Prompt Tokens", description="The number of tokens in the prompt")
    total_tokens: int = Field(..., title="Total Tokens", description="The number of tokens in the prompt and completion")


class GptResponse(BaseModel):
    id: str = Field(..., title="ID", description="The ID of the completion")
    choices: list[Choice] = Field(..., title="Choices", description="The choices of the completion")
    created: int = Field(..., title="Created", description="The time the completion was created")
    model: str = Field(..., title="Model", description="The model used for the completion")
    object: str = Field(..., title="Object", description="The object of the completion")
    system_fingerprint: None = Field(..., title="System Fingerprint", description="The system fingerprint of the completion")
    usage: CompletionUsage = Field(..., title="Usage", description="The usage of the completion")

    @root_validator(pre=True)
    def load_response(cls, values):
        values["choices"] = [dict(c) for c in values["choices"]]
        values["usage"] = dict(values["usage"])

        return values

    def __str__(self):
        return self.choices[0].message.content
