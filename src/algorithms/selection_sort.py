from animate_graph import plot
from typing import List

def selection_sort(arr: List[int]):
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