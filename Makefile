check:
	flake8 .
	mypy .
	python -m pytest --cov=cognitive_complexity --cov-report=xml
