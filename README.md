# congnitive-complexity

[![Build Status](https://travis-ci.org/Melevir/cognitive_complexity.svg?branch=master)](https://travis-ci.org/Melevir/cognitive_complexity)
[![Maintainability](https://api.codeclimate.com/v1/badges/853d47d353e7becc9f09/maintainability)](https://codeclimate.com/github/Melevir/cognitive_complexity/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/853d47d353e7becc9f09/test_coverage)](https://codeclimate.com/github/Melevir/cognitive_complexity/test_coverage)
[![PyPI version](https://badge.fury.io/py/cognitive-complexity.svg)](https://badge.fury.io/py/cognitive-complexity)

Library to calculate Python functions cognitive complexity via code.


## Installation

    pip install cognitive_complexity

    Tested on python 3.7.

## Usage

    >>> import ast
    
    >>> funcdef = ast.parse("""
    ... def f(a):
    ...     return a * f(a - 1)  # +1 for recursion
    ... """).body[0]
    
    >>> from cognitive_complexity.api import get_cognitive_complexity
    >>> get_cognitive_complexity(funcdef)
    1


## What is cognitive complexity

Here are some readings about cognitive complexity:

- [Cognitive Complexity, Because Testability != Understandability](https://blog.sonarsource.com/cognitive-complexity-because-testability-understandability);
- [Cognitive Complexity: A new way of measuring understandability](https://www.sonarsource.com/docs/CognitiveComplexity.pdf), white paper by G. Ann Campbell;
- [Cognitive Complexity: the New Guide to Refactoring for Maintainable Code](https://www.youtube.com/watch?v=5C6AGTlKSjY);
- [Cognitive Complexity](https://docs.codeclimate.com/docs/cognitive-complexity) from CodeClimate docs;
- [Is Your Code Readable By Humans? Cognitive Complexity Tells You](https://www.tomasvotruba.cz/blog/2018/05/21/is-your-code-readable-by-humans-cognitive-complexity-tells-you/).


## Realization details

This is not precise realization of original algorithm proposed by SonarSource,
but it gives rather similar results.
The algorithm gives complexity points for breaking control flow, nesting,
recursion, stacks logic operation etc.

