import ast

from typing import Callable

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


def process_child_nodes(
    node: ast.AST,
    increment_by: int,
    verbose: bool,
    complexity_calculator: Callable,
) -> int:
    child_complexity = 0
    child_nodes = ast.iter_child_nodes(node)

    for node_num, child_node in enumerate(child_nodes):
        if isinstance(node, ast.Try):
            if node_num == 1:
                # add +1 for all try nodes except body
                increment_by += 1
            if node_num:
                child_complexity += max(1, increment_by)
        child_complexity += complexity_calculator(
            child_node,
            increment_by=increment_by,
            verbose=verbose,
        )
    return child_complexity
