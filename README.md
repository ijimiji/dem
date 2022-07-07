# Dem — Telegram bot to create demotivational memes
## Install
```bash
poetry install
```
- For legal reasons I can't bundle Microsoft Windows fonts with this repo. So you'll have to manually create `static/fonts` folder and copy `arial.ttf` and `times.ttf` to it.

- Also you'll have to provide `.env` file in the root of a project with `API_TOKEN="verysecretkey"`.
## Run
```bash
poetry run python3 main.py
```
## Choices
### Editor
- Poetry is configured through `poetry.toml` to create venv in the project root, so that it can be detected by Pyright, which is enabled in `[tool.pyright]` section of `pyproject.toml`.
### Linting and formatting
- pre-commit is configured to auto `black` and `isort`.
### To be done
- [ ] Connect image processors with bot endpoint.
- [ ] Add devoper scripts to reload bot on change.
- [ ] Configure telegram security policies.
- [ ] Handle parameters from messages.