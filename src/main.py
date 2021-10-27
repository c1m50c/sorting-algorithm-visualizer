from algorithms.selection_sort import selection_sort

from animate_graph import camera
import matplotlib.pyplot as plt
import numpy as np
import random


ARR_SIZE: int = 30
INTERVAL_TIME: int = 100
arr: list[int] = [  ]


def main():
    arr.clear()
    for i in range(ARR_SIZE):
        arr.append(random.randint(0, ARR_SIZE))
    selection_sort(arr)
    animation = camera.animate(interval=INTERVAL_TIME)
    plt.show()


if __name__ == "__main__":
    main()