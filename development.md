# Development

Instructions for developers.

## macOS

Install

* [Homebrew](https://brew.sh/)

* [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

  ```sh
  brew install pyenv pyenv-virtualenv
  ```

* [pipx](https://github.com/pypa/pipx)

  ```sh
  brew install pipx
  ```

* [Poetry](https://github.com/python-poetry/poetry)

  ```sh
  pipx install poetry
  ```

* [ruff](https://github.com/astral-sh/ruff)

  ```sh
  brew install ruff
  ```

Similar to this [setup](https://github.com/Hasenpfote/python-poetry-example?tab=readme-ov-file), but no tox and uses ruff.

## Project

* `git clone`

* Development

  ```sh
  poetry install
  ```

  Launch virtualenv:

  ```sh
  poetry shell
  ```

  Code formatting:

  ```sh
  poetry run ruff format
  ```

  Linter:

  ```sh
  poetry run ruff check
  ```

  Test with coverage:

  ```sh
  pytest --cov --cov-report term
    ```

* Publish checklist

  * https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04

  * Bump version
    * [pyproject.toml](pyproject.toml)
    * [src/beancount_multitool/__version__.py](src/beancount_multitool/__version__.py)
    * Update [changelog](changelog.md)
  * Run local tests and coverage.
    * Update coverage number in [README.md](README.md).
  * `git commit` and check that GitHub Action tests succeed.
  * `poetry build`
  * `poetry publish`
  