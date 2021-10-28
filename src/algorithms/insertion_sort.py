from animate_graph import plot

def insertion_sort(arr: list[int]):
    """
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n * n)
    Average Case Time Complexity == O(n * n)
    Best Case Time Complexity == O(n)
    Space Complexity == O(n) Total, O(1) Auxiliary
    ```
    """
    
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1
            plot(i, arr, other_highlights=[j])