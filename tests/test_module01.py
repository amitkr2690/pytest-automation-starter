import pytest
from conftest import app_version
pytestmark = [ pytest.mark.marked, pytest.mark.str ]

def fun1():
    print("fun1")
    return 1

@pytest.mark.skipif(app_version>2,reason="skiping the test")
def test_a1():
    assert fun1()

@pytest.mark.marked
def test_a3():
    assert 10-5==5

@pytest.mark.marked
def test_a2():
    assert 5+5==10

@pytest.mark.skip(reason="unconditional skiping the test")
def test_a4():
    assert 10-5==6, "failed test intentionally"


def test_a5():
    with pytest.raises(Exception):
        assert 1/0

def test_a6():
    with pytest.raises(ZeroDivisionError):
        assert 1/0


def div(a,b):
    if b==0:
        raise ValueError("value error")
    else:
        return a/b

def test_a7():
    with pytest.raises(Exception) as e:
        assert div(1,0)
    assert str(e.value)=="value error"
    #assert "division by zero" in str(e.value)

def test_a8():
    assert 10-5==5