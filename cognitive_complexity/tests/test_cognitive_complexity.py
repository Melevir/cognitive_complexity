from cognitive_complexity.tests.conftest import get_code_snippet_compexity


def test_simple_if_simple_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a:  # +1
            return 1
    """) == 1


def test_simple_if_serial_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a and b and True:  # +2
            return 1
    """) == 2


def test_simple_if_serial_heterogenious_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a and b or True:  # +3
            return 1
    """) == 3


def test_simple_if_complex_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if (  # +1
            a and b and  # +1
            (c or d)  # +1
        ):
            return 1
    """) == 3


def test_simple_structure_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if (a):  # +1
            return 1
        if (b):  # +1
            return 2
    """) == 2


def test_nested_structure_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a:  # +1
            for i in range(b):  # +2
                return 1
    """) == 3


def test_very_nested_structure_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a:  # +1
            for i in range(b):  # +2
                if b:  # +3
                    return 1
    """) == 6


def test_try_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        try:
            for foo in bar:  # +1
                return a
        except Exception:  # +1
            if a < 0:  # +2
                return a
    """) == 4


def test_recursion_complexity():
    assert get_code_snippet_compexity("""
    def f(a):
        return a * f(a - 1)  # +1 for recursion
    """) == 1
