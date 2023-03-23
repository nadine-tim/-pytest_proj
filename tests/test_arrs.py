from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4, 5], -1, -2) == []
    assert arrs.my_slice([1, 2, 3], -5, -2) == [1]
    assert arrs.my_slice([], 1, 3) == []
