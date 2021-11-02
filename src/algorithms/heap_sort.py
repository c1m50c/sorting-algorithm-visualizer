from animate_graph import plot
from typing import List

def create_heap(arr: List[int], length: int, idx: int):
    largest: int = idx
    left: int = 2 * idx + 1
    right: int = 2 * idx + 2
    
    if left < length and arr[left] > arr[largest]: largest = left
    if right < length and arr[right] > arr[largest]: largest = right
    
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx] # Swap
        create_heap(arr=arr, length=length, idx=largest)
        plot(idx, arr, other_highlights=[largest])


def heap_sort(arr: List[int]):
    """
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n log n)
    Average Case Time Complexity == O(n log n)
    Best Case Time Complexity == O(n)
    Space Complexity == O(n) Total, O(1) Auxiliary
    ```
    """
    
    for i in range(len(arr) // 2 - 1, -1, -1):
        create_heap(arr=arr, length=len(arr), idx=i)
    
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap
        plot(-1, arr, other_highlights=[i])
        create_heap(arr=arr, length=i, idx=0)