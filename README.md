# prefect-pandera

<a href="https://pypi.python.org/pypi/prefect-pandera/" alt="PyPI Version">
    <img src="https://badge.fury.io/py/prefect-pandera.svg" /></a>
<a href="https://github.com/discdiver/prefect-pandera/" alt="Stars">
    <img src="https://img.shields.io/github/stars/discdiver/prefect-pandera" /></a>
<a href="https://pepy.tech/badge/prefect-pandera/" alt="Downloads">
    <img src="https://pepy.tech/badge/prefect-pandera" /></a>
<a href="https://github.com/discdiver/prefect-pandera/pulse" alt="Activity">
    <img src="https://img.shields.io/github/commit-activity/m/discdiver/prefect-pandera" /></a>
<a href="https://github.com/discdiver/prefect-pandera/graphs/contributors" alt="Contributors">
    <img src="https://img.shields.io/github/contributors/discdiver/prefect-pandera" /></a>
<br>
<a href="https://prefect-community.slack.com" alt="Slack">
    <img src="https://img.shields.io/badge/slack-join_community-red.svg?logo=slack" /></a>
<a href="https://discourse.prefect.io/" alt="Discourse">
    <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?logo=discourse" /></a>

## Welcome!

This package makes it easy to use Prefect and Pandera together so that you can ensure your data looks how you expect it to look.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-pandera` with `pip`:

```bash
pip install prefect-pandera
```

### Write and run a flow

```python
from prefect import flow
from prefect_pandera.tasks import (
    goodbye_prefect_pandera,
    hello_prefect_pandera,
)


@flow
def example_flow():
    hello_prefect_pandera
    goodbye_prefect_pandera

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-pandera`, feel free to open an issue in the [prefect-pandera](https://github.com/discdiver/prefect-pandera) repository.

If you have any questions or issues while using `prefect-pandera`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-pandera` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/discdiver/prefect-pandera.git

cd prefect-pandera/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
