from animate_graph import plot

def bubble_sort(arr: list[int]):
    """
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n * n)
    Average Case Time Complexity == O(n * n)
    Best Case Time Complexity == O(n)
    Space Complexity == O(n) Total, O(1) Auxiliary
    ```
    """
    
    for i in range(0, len(arr)):
        swapped: bool = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                plot(i + 1, arr, other_highlights=[j + 1])
                swapped = True
        if swapped == False:
            break