.PHONY: run install clean check runner
.DEFAULT_GOAL := runner

run: install
	cd app && poetry run python run.py

install: pyproject.toml
	poetry install --no-root

clean:
ifeq ($(OS),Windows_NT)
	PowerShell -Command "Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force"
else
	find . -type d -name "__pycache__" -exec rm -r {} +
endif

check:
	poetry run flake8 app/

runner: check run clean