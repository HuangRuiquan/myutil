# Sample Test passing with nose and pytest
from myutil.myutil import sample


def test_sample():
    assert sample(True), "dummy sample test"
    assert not sample(False), "dummy sample test"
