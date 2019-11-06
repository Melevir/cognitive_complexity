check:
	flake8 .
	mypy .
	make test

test:
	python -m pytest --cov=cognitive_complexity --cov-report=xml
