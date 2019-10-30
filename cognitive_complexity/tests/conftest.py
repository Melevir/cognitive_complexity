import ast

from cognitive_complexity.api import get_cognitive_complexity


def get_code_snippet_compexity(src: str) -> int:
    funcdef = ast.parse(src.strip()).body[0]
    return get_cognitive_complexity(funcdef)
