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
                else:
                    processed_words.append(word.lower())
        return processed_words, raw_camelcase_words
    """) == 10
