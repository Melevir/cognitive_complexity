check:
	flake8 .
	mypy .
	make test check_readme

test:
	python -m pytest --cov=cognitive_complexity --cov-report=xml

check_readme:
	mdl README.md
