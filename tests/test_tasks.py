from prefect import flow

from prefect_pandera.tasks import (
    goodbye_prefect_pandera,
    hello_prefect_pandera,
)


def test_hello_prefect_pandera():
    @flow
    def test_flow():
        return hello_prefect_pandera()

    result = test_flow()
    assert result == "Hello, prefect-pander!"


def goodbye_hello_prefect_pandera():
    @flow
    def test_flow():
        return goodbye_prefect_pandera()

    result = test_flow()
    assert result == "Goodbye, prefect-pander!"
