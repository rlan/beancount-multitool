# Development

Instructions for developers.

## macOS

Install

* [Homebrew](https://brew.sh/)
* [pyenv](https://github.com/pyenv/pyenv) (optional)
* [Poetry](https://github.com/python-poetry/poetry)

## Project

* `git clone`

* Install

  ```sh
  poetry install
  ```

* Development

  Launch virtualenv:

  ```sh
  poetry shell
  ```

  Test:

  ```sh
  pytest
  ```

  Run code coverage:

  ```sh
  pytest --cov --cov-report term
    ```

* Publish

  * https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04
