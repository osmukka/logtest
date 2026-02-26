import pytest

from peekable import peekable


@pytest.fixture
def non_empty():
    return peekable.Peekable([1, 2, 3])

@pytest.fixture
def empty():
    return peekable.Peekable([])


class TestInit:
    def test_valid_value(self):
        p = peekable.Peekable([1, 2, 3])
        assert isinstance(p, peekable.Peekable)

    def test_invalid_value(self):
        with pytest.raises(TypeError):
            p = peekable.Peekable("Not a list!")


class TestItemsLeft:
    def test_non_empty(self, non_empty):
        assert non_empty.items_left() == 3, ""

    def test_empty(self, empty):
        assert empty.items_left() == 0


class TestPeek:
    def test_non_empty(self, non_empty):
        assert non_empty.peek() == 1, "Should return 1 item by default"
        assert non_empty.peek(2) == [1, 2], "Should return a slice from the peekable"
        assert non_empty.peek(4) is None, "Peeking too many items should return None"
        with pytest.raises(ValueError):
            non_empty.peek(0)

    def test_empty(self, empty):
        assert empty.peek() is None, "Peeking an empty peekable should return None"


class TestAdvance:
    def test_non_empty(self, non_empty):
        assert non_empty.advance() == 1, "Advance should return 1 item by default"
        assert non_empty.advance(2) == [2, 3], "Advancing should increment the iterator"
        assert non_empty.advance() is None, "Advancing too many items should return None"


    def test_empty(self, empty):
        assert empty.advance() is None, "Advancing on an empty peekable should return None"

