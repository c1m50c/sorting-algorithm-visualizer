from animate_graph import plot
from typing import List

def gnome_sort(arr: List[int]):
    """
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n * n)
    Average Case Time Complexity == O(n * n)
    Best Case Time Complexity == O(n)
    Space Complexity == O(1) Auxiliary
    ```
    """
    
    for p in range(1, len(arr)):
        position: int = p
        while position > 0 and arr[position - 1] > arr[position]:
            arr[position - 1], arr[position] = arr[position], arr[position - 1] # Swap
            position -= 1
            plot(p, arr, other_highlights=[position])