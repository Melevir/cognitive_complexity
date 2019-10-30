import ast

from cognitive_complexity.common_types import AnyFuncdef
from cognitive_complexity.utils.ast import has_recursive_calls


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
        verbose: bool = False,
) -> int:
    control_flow_breakers = (
        ast.If,
        ast.For,
        ast.While,
        ast.While,
        ast.Try,
    )

    base_complexity = 0
    child_complexity = 0
    should_iter_children = True
    if isinstance(node, control_flow_breakers):
        increment_by += 1
        base_complexity += max(1, increment_by)
    elif isinstance(node, ast.BoolOp):
        inner_boolops_amount = len([n for n in ast.walk(node) if isinstance(n, ast.BoolOp)])
        base_complexity += inner_boolops_amount * increment_by
        should_iter_children = False

    if should_iter_children:
        child_nodes = ast.iter_child_nodes(node)
        child_complexity += sum(
            get_cognitive_complexity_for_node(n, increment_by=increment_by)
            for n in child_nodes
        )

    complexity = base_complexity + child_complexity
    if verbose:
        print(  # noqa
            f'Complexity for {node} is {complexity} ({base_complexity} + {child_complexity})'
            f' (increment {increment_by})',
        )
    return complexity
