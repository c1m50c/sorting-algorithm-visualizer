from animate_graph import plot
from typing import List

def next_gap(gap: int) -> int:
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap


def comb_sort(arr: List[int]):
    """
        ## Complexities:
        ```py
        Worst Case Time Complexity == O(n * n)
        Average Case Time Complexity == O(n * n / 2^i) # i = number of increments
        Best Case Time Complexity == O(n log n)
        Space Complexity == O(1)
        ```
    """
    
    gap: int = len(arr)
    swapped: bool = True
 
    while gap != 1 or swapped == True:
        gap = next_gap(gap)
        swapped = False

        for i in range(0, len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            plot(i, arr, other_highlights=[i + gap])