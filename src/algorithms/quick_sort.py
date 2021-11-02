from animate_graph import plot
from typing import List

def partition(arr: List[int], left: int, right: int) -> int:
    pivot: int = right
    i, j = left - 1, right
    
    while True:
        i += 1
        while arr[i] < arr[pivot]: i += 1
        
        j -= 1
        while j >= 0 and arr[j] > arr[pivot]: j -= 1
        
        if i >= j: break
        else: arr[i], arr[j] = arr[j], arr[i] # Swap
        plot(pivot, arr, other_highlights=[i, j])
    
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def quick_sort_lr(arr: List[int], left: int, right: int):
    """
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n * n)
    Average Case Time Complexity == O(n log n)
    Best Case Time Complexity == O(n log n)
    Space Complexity == O(n)
    ```
    """
    
    if left < right:
        part = partition(arr=arr, left=left, right=right)
        quick_sort_lr(arr=arr, left=left, right=part-1)
        quick_sort_lr(arr=arr, left=part+1, right=right)


def quick_sort(arr: List[int]):
    """
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n * n)
    Average Case Time Complexity == O(n log n)
    Best Case Time Complexity == O(n log n)
    Space Complexity == O(n)
    ```
    """
    
    quick_sort_lr(arr, 0, len(arr) - 1)