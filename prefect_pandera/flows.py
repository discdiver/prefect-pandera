"""This is an example flows module"""
from prefect import flow

from prefect_pandera.tasks import (
    goodbye_prefect_pandera,
    hello_prefect_pandera,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_prefect_pandera)
    print(goodbye_prefect_pandera)
    return "Done"
