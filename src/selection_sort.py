# https://github.com/c1m50c/py-algorithms/blob/main/src/selection_sort.py #

def selection_sort(array: list[int]) -> None:
    """
        # Selection Sort
        ### Complexities
        ```py
        Worst Case Time Complexity == O(n^2)
        Average Case Time Complexity == O(n^2)
        Best Case Time Complexity == O(n^2)
        Space Complexity == O(1)
        ```
    """

    if len(array) <= 1:
        return
    
    for i in range(0, len(array) - 1):
        cur_min_idx: int = i
        for j in range(i + 1, len(array)):
            if array[j] < array[cur_min_idx]:
                cur_min_idx = j
        array[i], array[cur_min_idx] = array[cur_min_idx], array[i]
        yield array