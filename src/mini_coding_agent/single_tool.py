import ast
import operator

import openai
from pydantic import BaseModel


class CalculatorInput(BaseModel):
    expression: str


CALCULATOR_TOOL = openai.pydantic_function_tool(
    CalculatorInput,
    name="calculator",
    description="Evaluate a basic arithmetic expression and return the numeric result.",
)


_BINARY_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def run_calculator(expression: str) -> str:
    tree = ast.parse(expression, mode="eval")
    result = _eval_ast(tree.body)
    return str(result)


def _eval_ast(node: ast.AST) -> float | int:
    if isinstance(node, ast.Constant) and isinstance(node.value, int | float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_OPS:
        left = _eval_ast(node.left)
        right = _eval_ast(node.right)
        return _BINARY_OPS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        operand = _eval_ast(node.operand)
        return _UNARY_OPS[type(node.op)](operand)

    raise ValueError("Unsupported expression. Use only basic arithmetic.")
