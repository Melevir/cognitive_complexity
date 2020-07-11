import ast

from typing import Callable, Tuple, Union

from cognitive_complexity.common_types import AnyFuncdef


def has_recursive_calls(funcdef: AnyFuncdef) -> bool:
    return bool([
        n for n in ast.walk(funcdef)
        if (
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == funcdef.name
        )
    ])


def is_decorator(funcdef: AnyFuncdef) -> bool:
    return (
        isinstance(funcdef, ast.FunctionDef)
        and len(funcdef.body) == 2
        and isinstance(funcdef.body[0], ast.FunctionDef)
        and isinstance(funcdef.body[1], ast.Return)
    )


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


def process_control_flow_breaker(
    node: Union[ast.If, ast.For, ast.While, ast.IfExp],
    increment_by: int,
) -> Tuple[int, int, bool]:
    if isinstance(node, ast.IfExp):
        # C if A else B; ternary operator equivalent
        increment = 0
        increment_by += 1
    elif isinstance(node, ast.If) and len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
        # node is an elif; the increment will be counted on the ast.If
        increment = 0
    elif node.orelse:
        # +1 for the else and add a nesting level
        increment = 1
        increment_by += 1
    else:
        # no 'else' to count, just add a nesting level
        increment = 0
        increment_by += 1
    return increment_by, max(1, increment_by) + increment, True


def process_node_itself(
    node: ast.AST,
    increment_by: int,
) -> Tuple[int, int, bool]:
    control_flow_breakers = (
        ast.If,
        ast.For,
        ast.While,
        ast.IfExp,
    )
    incrementers_nodes = (
        ast.FunctionDef,
        ast.AsyncFunctionDef,
        ast.Lambda,
    )

    if isinstance(node, control_flow_breakers):
        return process_control_flow_breaker(node, increment_by)
    elif isinstance(node, incrementers_nodes):
        increment_by += 1
        return increment_by, 0, True
    elif isinstance(node, ast.BoolOp):
        inner_boolops_amount = len([n for n in ast.walk(node) if isinstance(n, ast.BoolOp)])
        base_complexity = inner_boolops_amount
        return increment_by, base_complexity, False
    return increment_by, 0, True
