import ast

from cognitive_complexity.common_types import AnyFuncdef
from cognitive_complexity.utils.ast import has_recursive_calls, process_child_nodes


def get_cognitive_complexity(funcdef: AnyFuncdef) -> int:
    complexity = 0
    for node in funcdef.body:
        complexity += get_cognitive_complexity_for_node(node)
    if has_recursive_calls(funcdef):
        complexity += 1
    return complexity


def get_cognitive_complexity_for_node(
        node: ast.AST,
        increment_by: int = 0,
        verbose: bool = True,
) -> int:
    control_flow_breakers = (
        ast.If,
        ast.For,
        ast.While,
    )
    incrementers_nodes = (
        ast.FunctionDef,
        ast.AsyncFunctionDef,
        ast.Lambda,
    )

    base_complexity = 0
    child_complexity = 0
    should_iter_children = True
    if isinstance(node, control_flow_breakers):
        increment_by += 1
        base_complexity += max(1, increment_by)
    elif isinstance(node, incrementers_nodes):
        increment_by += 1
    elif isinstance(node, ast.BoolOp):
        inner_boolops_amount = len([n for n in ast.walk(node) if isinstance(n, ast.BoolOp)])
        base_complexity += inner_boolops_amount * max(increment_by, 1)
        should_iter_children = False
    elif isinstance(node, (ast.Break, ast.Continue)):
        base_complexity += max(1, increment_by)

    if should_iter_children:
        child_complexity += process_child_nodes(
            node,
            increment_by,
            verbose,
            get_cognitive_complexity_for_node,
        )

    complexity = base_complexity + child_complexity
    if verbose:
        print(  # noqa
            f'Complexity for {node} is {complexity} ({base_complexity} + {child_complexity})'
            f' (increment {increment_by})',
        )
    return complexity
