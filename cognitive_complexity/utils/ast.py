import ast

from cognitive_complexity.common_types import AnyFuncdef


def has_recursive_calls(funcdef: AnyFuncdef) -> bool:
    return bool([
        n for n in ast.walk((funcdef))
        if (
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == funcdef.name
        )
    ])
