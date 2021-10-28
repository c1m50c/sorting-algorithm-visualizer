from algorithms.selection_sort import selection_sort

def test_with_ints():
    arr: list[int] = [ 5, 2, 1, 0, 2, 5, 7 ]
    assert selection_sort(arr) == [ 0, 1, 2, 2, 5, 5, 7 ]


def test_with_floats():
    arr: list[float] = [ 3.33, 4.20, 1.337, 4.53, 3.60, 6.0, 0.0 ]
    assert selection_sort(arr) == [ 0.0, 1.337, 3.33, 3.60, 4.20, 4.53, 6.0 ]