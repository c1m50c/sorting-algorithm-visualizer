from animate_graph import plot

def shell_sort(arr: list[int]):
    """
        ## Complexities:
        ```py
        # Time Complexities largely depend on the gap sequence.
        Worst Case Time Complexity == O(?)
        Average Case Time Complexity == O(?)
        Best Case Time Complexity == O(?)
        Space Complexity == O(n) Total, O(1) Auxiliary
        ```
    """
    
    GAP_SEQUENCE: list[int] = [ 701, 301, 132, 57, 23, 10, 4, 1 ]
    
    for gap in GAP_SEQUENCE:
        for i in range(gap, len(arr)):
            temp: int = arr[i]
            j: int = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                plot(i, arr, other_highlights=[j])
            
            arr[j] = temp