import pytest

@pytest.fixture()
def setup():
    print("Basic setup")

def test_method1(setup):
    print("Method 1")

@pytest.fixture(scope="session",autouse=True)
def suite():
    print("Suite setup")
    yield
    print("Suite teardown")


@pytest.fixture(scope="function",autouse=True)
def test_case():
    print("Test setup")
    yield
    print("Test teardown")

def test_example():
    assert 1==1