from pydantic import BaseModel


class Step(BaseModel):
    explain: str
    output: str


class MathReasoning(BaseModel):
    steps: list[Step]
    final_result: str
