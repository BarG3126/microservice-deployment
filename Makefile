.PHONY: run install clean check runner
.DEFAULT_GOAL := runner

run: install
	cd src && poetry run python runner.py

install: pyproject.toml
	poetry install --no-root

clean:
ifeq ($(OS),Windows_NT)
	PowerShell -Command "Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force"
else
	find . -type d -name "__pycache__" -exec rm -r {} +
endif

check:
	poetry run flake8 src\

runner: check run clean