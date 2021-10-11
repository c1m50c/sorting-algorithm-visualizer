# https://github.com/c1m50c/py-algorithms/blob/main/src/merge_sort.py #
# Todo: Find a good way to animate #

def merge_sort(array: list[int]) -> None:
    """
        # Merge Sort
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(n log n)
        Average Case Time Complexity == O(n log n)
        Best Case Time Complexity == O(n log n)
        Space Complexity == O(n)
        ```
    """
    
    if len(array) > 1:
        # Divide & Conquer
        left: list[int] = array[:len(array) // 2]
        right: list[int] = array[len(array) // 2:]
        merge_sort(array=left)
        merge_sort(array=right)
        
        # Start Merging
        i, j, m = 0, 0, 0 # Left, Right, Merged
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[m] = left[i]
                i += 1
            else:
                array[m] = right[j]
                j += 1
            m += 1
        
        while i < len(left):
            array[m] = left[i]
            i += 1
            m +=  1
        
        while j < len(right):
            array[m] = right[j]
            j += 1
            m += 1