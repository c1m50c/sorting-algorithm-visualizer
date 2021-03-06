# Parts of this code based on repository: https://github.com/lucs123/sorting-visualizer-matplotlib

import matplotlib.pyplot as plt
from celluloid import Camera


fig = plt.figure()
camera = Camera(fig)


def plot(highlight: int, data: list, other_highlights: list[int] = [  ]):
    """
    To be used in animating a plot figure, see `algorithms` to see examples of its usage.
    ## Parameters:
    ```py
    highlight: int # Index of a value to highlight.
    data: list # The array containing the values being sorted.
    other_highlights: list[int] = [  ] # Other points important enough to be highlighted, Different color than normal highlight.
    ```
    """
    
    arr = list(range(len(data)))    
    colors = list(len(data) * "k")
    
    if highlight >= 0:
        colors[highlight] = "#ff0000"
    
    for i in other_highlights:
        colors[i] = "#00ff00"
    
    plt.bar(arr, data, color=colors)
    camera.snap()