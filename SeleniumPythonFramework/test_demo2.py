import pytest


@pytest.mark.smoke   # custom mark
@pytest.mark.skip    # predefined mark
def test_firstProgram():
    msg = "hello"
    assert msg == "Hi", "Test failed because Strings do not match"

def test_FourthProgram():
    a = 4
    b = 6
    assert a+2 == b, "Test failed because Addition do not match"

