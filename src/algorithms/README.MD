# **algorithms**
Module for the Sorting Algorithms to be visualized while sorting.

## **Documentation**
The `docstring` for each algorithm function should contain at least the time complexities as well as the space complexity for the algorithm. An example of a proper `docstring` is shown below.

```py
"""
    ## Complexities:
    ```py
    Worst Case Time Complexity == O(n * n)
    Average Case Time Complexity == O(n * n)
    Best Case Time Complexity == O(n * n)
    Space Complexity == O(1)
    ```
"""
```

## **Using `animate_graph.plot`**
`animate_graph.plot` is the main function used for animating the graphs.
An example of it's usage within the `insertion_sort` algorithm is shown below.
It's best used in the primary loop of the sorting algorithm,
when the bulk of that iteration's sorting is finished.

```py
# algorithms/insertion_sort.py #
from animate_graph import plot

for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1] # Swap
            j = j - 1
            plot(i, arr, other_highlights=[j])
```

```py
# Parameter Explanation #
hightlight: int # Normally the pivot point, crucial index to be highlighted in the visualization.
data: list # Data values for visualization, almost always the main array being sorted.
other_highlights: list[int] = [  ] # Other crucial indexes within the main array.
```

## **Implementing A New Algorithm**
```py
# algorithms/NEW_ALGORITHM.py

def NEW_ALGORITHM(arr: list[int]):
    # Note: `arr` is the list to sort, make sure your function only has this one parameter.
    pass
```

```py
# main.py

from algorithms.NEW_ALGORITHM import NEW_ALGORITHM

...

ALGORITHMS = {
    # "algorithm_name": [algorithm_function, wctc, actc, bctc],
    "NEW_ALGORITHM": [NEW_ALGORITHM, "Time complexities", "go", "here"],
    ...
}
```

```py
# test_algorithms.py

from algorithms.NEW_ALGORITHM import NEW_ALGORITHM

...

def test_NEW_ALGORITHM():
    arr: list[int] = [ 5, 3, 2, 1, 5 ] # Unsorted Array
    NEW_ALGORITHM(arr)
    assert arr == [ 1, 2, 3, 5, 5 ] # Sorted Array
```