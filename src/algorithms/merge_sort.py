from animate_graph import plot
from typing import List

def merge(arr: List[int], left: int, middle: int, right: int):
    n1, n2 = middle - left + 1, right - middle
    left_arr, right_arr = [0] * n1, [0] * n2
    
    for i in range(0, n1):
        left_arr[i] = arr[left + i]
    
    for i in range(0, n2):
        right_arr[i] = arr[middle + i + 1]
    
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if left_arr[i] > right_arr[j]:
            arr[k] = right_arr[j]
            j += 1
        else:
            arr[k] = left_arr[i]
            i += 1
        k += 1
    
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr: List[int]):
    """
        ## Complexities:
        ```py
        Worst Case Time Complexity == O(n log n)
        Average Case Time Complexity == O(n log n)
        Best Case Time Complexity == O(n log n)
        Space Complexity == O(n)
        ```
    """
    
    width: int = 1
    arr_len: int = len(arr)
    while width < arr_len:
        left: int = 0
        while left < arr_len:
            right: int = min(left + (width * 2 - 1), arr_len - 1)
            middle: int = (left + right) // 2
            
            if width > arr_len // 2:
                middle = right - (arr_len % width)
            merge(arr=arr, left=left, middle=middle, right=right)
            plot(middle, arr, other_highlights=[left, right])
            left += width * 2
        width *= 2