# congnitive-complexity

[![Build Status](https://travis-ci.org/Melevir/cognitive_complexity.svg?branch=master)](https://travis-ci.org/Melevir/cognitive_complexity)
[![Maintainability](https://api.codeclimate.com/v1/badges/853d47d353e7becc9f09/maintainability)](https://codeclimate.com/github/Melevir/cognitive_complexity/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/853d47d353e7becc9f09/test_coverage)](https://codeclimate.com/github/Melevir/cognitive_complexity/test_coverage)
[![PyPI version](https://badge.fury.io/py/cognitive-complexity.svg)](https://badge.fury.io/py/cognitive-complexity)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cognitive-complexity)

Library to calculate Python functions cognitive complexity via code.

## Installation

```bash
pip install cognitive_complexity
```

## Usage

```python
>>> import ast

>>> funcdef = ast.parse("""
... def f(a):
...     return a * f(a - 1)  # +1 for recursion
... """).body[0]

>>> from cognitive_complexity.api import get_cognitive_complexity
>>> get_cognitive_complexity(funcdef)
1
```

### Flake8-Cognitive-Complexity Extension

Perhaps the most common way to use this library (especially if you are
already using the [Flake8 linter](https://flake8.pycqa.org/en/latest/))
is to use the
[flake8-cognitive-complexity extension](https://github.com/Melevir/flake8-cognitive-complexity).
If you run Flake8 with this extension installed, Flake8 will let you know
if your code is too complex. For more details and documentation, visit the
[flake8-cognitive-complexity extension repository](https://github.com/Melevir/flake8-cognitive-complexity).

## What is cognitive complexity

Here are some readings about cognitive complexity:

- [Cognitive Complexity, Because Testability != Understandability](https://blog.sonarsource.com/cognitive-complexity-because-testability-understandability);
- [Cognitive Complexity: A new way of measuring understandability](https://www.sonarsource.com/docs/CognitiveComplexity.pdf),
  white paper by G. Ann Campbell;
- [Cognitive Complexity: the New Guide to Refactoring for Maintainable Code](https://www.youtube.com/watch?v=5C6AGTlKSjY);
- [Cognitive Complexity](https://docs.codeclimate.com/docs/cognitive-complexity)
  from CodeClimate docs;
- [Is Your Code Readable By Humans? Cognitive Complexity Tells You](https://www.tomasvotruba.cz/blog/2018/05/21/is-your-code-readable-by-humans-cognitive-complexity-tells-you/).

## Realization details

This is not precise realization of original algorithm
proposed by [G. Ann Campbell](https://github.com/ganncamp),
but it gives rather similar results.
The algorithm gives complexity points for breaking control flow, nesting,
recursion, stacks logic operation etc.

## Contributing

We would love you to contribute to our project. It's simple:

- Create an issue with bug you found or proposal you have. Wait for
  approve from maintainer.
- Create a pull request. Make sure all checks are green.
- Fix review comments if any.
- Be awesome.

Here are useful tips:

- You can run all checks and tests with `make check`. Please do it
  before TravisCI does.
- We use [BestDoctor python styleguide](https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md).
  Sorry, styleguide is available only in Russian for now.
- We respect [Django CoC](https://www.djangoproject.com/conduct/).
  Make soft, not bullshit.
