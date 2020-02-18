import pytest

class TestSource:
    def __init__(self, x, y):
        self.x = x
        self.y = y

@pytest.fixture
def source():
    return TestSource(0,0)