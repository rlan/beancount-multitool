# Development

Instructions for developers.

## On macOS

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

Similar to this [setup](https://github.com/Hasenpfote/python-poetry-example), but no tox and uses ruff.

## Procedure

Get repo:

```sh
git clone
```

Install development environment:

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

Build documentation:

```sh
mkdocs build
```

## PyPi publish checklist

Ref: [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04)

* [ ] Bump version
  * [ ] `pyproject.toml`
  * [ ] `src/beancount_multitool/__version__.py`
  * [ ] Update [changelog](changelog.md) in the documentation.
* [ ] Run local tests and coverage.
  * [ ] Update coverage number in project `README.md`.
* [ ] Update documentation, if necessary
    * [ ] Build documentation and check for warnings and errors.
* [ ] `git commit` and `git push`.
  * [ ] [Check](https://github.com/rlan/beancount-multitool/actions) that tests and deploy docs actions succeeded on GitHub Action.
* [ ] Tag the new version: `git tag -a v0.5.0 -m "v0.5.0"`
* [ ] `poetry build`
* [ ] `poetry publish`
