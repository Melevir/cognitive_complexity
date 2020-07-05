from conftest import get_code_snippet_compexity


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


def test_simple_elif_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if (a):  # +1
            return 1
        elif (b):  # +1
            return 2
        else:  # +1
            return 3
    """) == 3


def test_simple_else_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a):
        if (a):  # +1
            return 1
        else:  # +1
            return 3
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


def test_real_function():
    assert get_code_snippet_compexity("""
    def process_raw_constant(constant, min_word_length):
        processed_words = []
        raw_camelcase_words = []
        for raw_word in re.findall(r'[a-z]+', constant):  # +1
            word = raw_word.strip()
            if (  # +2
                len(word) >= min_word_length  # +4 (2 bool operator sequences * 2 for nesting)
                and not (word.startswith('-') or word.endswith('-'))
            ):
                if is_camel_case_word(word):  # +2
                    raw_camelcase_words.append(word)
                else:  # +1
                    processed_words.append(word.lower())
        return processed_words, raw_camelcase_words
    """) == 11


def test_break_and_continue():
    assert get_code_snippet_compexity("""
    def f(a):
        for a in range(10):  # +1
            if a % 2:  # +2
                continue  # +2
            if a == 8:  # +2
                break  # +2
    """) == 9


def test_nested_functions():
    assert get_code_snippet_compexity("""
    def f(a):
        def foo(a):
            if a:  # +2
                return 1
        bar = lambda a: lambda b: b or 2  # +2 (+2 for or because lambda increases nesting)
        return bar(foo(a))(a)
    """) == 4


def test_ternary_operator():
    assert get_code_snippet_compexity("""
    def f(a):
        if a % 2:  # +1
            return 'c' if a else 'd'  # +2
        return 'a' if a else 'b'  # +1
    """) == 4


def test_nested_if_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a == b:  # +1
            if (a):  # +2 (nesting=1)
                return 1
        return 0
    """) == 3


def test_nested_else_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a == b:  # +1
            if (a):  # +2 (nesting=1)
                return 1
            else:  # +1
                return 3
        return 0
    """) == 4


def test_nested_elif_condition_complexity():
    assert get_code_snippet_compexity("""
    def f(a, b):
        if a == b:  # +1
            if (a):  # +2 (nesting=1)
                return 1
            elif (b):  # +1
                return 2
            else:  # +1
                return 3
        return 0
    """) == 5


def test_for_else_complexity():
    assert get_code_snippet_compexity("""
    def f(a):
        for a in range(10):  # +1
            if a % 2:  # +2
                continue  # +2
            if a == 8:  # +2
                break  # +2
        else:  # +1
            return 5
    """) == 10


def test_while_else_complexity():
    assert get_code_snippet_compexity("""
    def f(a):
        a = 0
        while a < 10:  # +1
            if a % 2:  # +2
                continue  # +2
            if a == 8:  # +2
                break  # +2
            a += 1
        else:  # +1
            return 5
    """) == 10
