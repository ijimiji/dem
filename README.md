# Dem — Telegram bot to create demotivational memes
## Install
```bash
poetry install
```
## Choices
### Editor
- Poetry is configured through `poetry.toml` to create venv in the project root, so that it can be detected by Pyright, which is enabled in `[tool.pyright]` section of `pyproject.toml`.
### Linting and formatting
- pre-commit is configured to auto `black` and `isort`.
