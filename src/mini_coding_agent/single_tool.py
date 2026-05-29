import openai
from pydantic import BaseModel


class Step(BaseModel):
    explain: str
    output: str


class MathReasoning(BaseModel):
    steps: list[Step]
    final_result: str


# Go 类比: 把 struct 注册为一个可被调用的 handler
MATH_TOOL = openai.pydantic_function_tool(MathReasoning)
