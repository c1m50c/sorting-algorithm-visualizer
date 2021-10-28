from animate_graph import plot

def selection_sort(arr: list[int]):
    """
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n * n)
    Average Case Time Complexity == O(n * n)
    Best Case Time Complexity == O(n * n)
    Space Complexity == O(1)
    ```
    """
    
    for i in range(0, len(arr)):
        cur_min_idx: int = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
                plot(i, arr, other_highlights=[cur_min_idx])
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i] # Swap


def test_with_ints():
    arr: list[int] = [ 4, 3, 2, 1, 5, 5, 0 ]
    assert arr == arr.sort()


def test_with_floats():
    arr: list[float] = [ 1.3, 1.0, 5.55, 4.20, 9.76, 1.2 ]
    assert arr == arr.sort()