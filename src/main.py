from random import randint

from selection_sort import selection_sort
from insertion_sort import insertion_sort

from matplotlib.container import BarContainer
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def get_method_name(method: str) -> str:
    string_arr: list[str] = method.split("_")
    string = ""
    for s in string_arr:
        string += s.capitalize()
    return string


def create_array(array: list[int], length: int = 250) -> None:
    array.clear()
    for i in range(0, length):
        array.append(randint(0, length))


def get_array_as_str(array: list[int]) -> str:
    return f"[{array[0]} .. {array[len(array) - 1]}]"


def main(method: str, count: int = 250) -> None:
    arr: list[int] = [  ]
    
    create_array(array=arr, length=count)
    
    if method == "selection_sort":
        gen = selection_sort(array=arr)
    elif method == "insertion_sort":
        gen = insertion_sort(array=arr)
    else:
        raise ValueError
    
    fig, ax = plt.subplots()
    ax.set_title(get_method_name(method))
    bars = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, count)
    ax.set_ylim(0, int(1.05 * count))
    
    iteration: list[int] = [ 0 ]
    def update_figure(array: list[int], rects: BarContainer, iteration: list[int]) -> None:
        for rect, value in zip(rects, array):
            rect.set_height(value)
        iteration[0] += 1
    
    animation = anim.FuncAnimation(
        fig=fig,
        func=update_figure,
        fargs=(bars, iteration),
        frames=gen,
        interval=0.5,
        repeat=False
    )
    
    plt.show()


if __name__ == "__main__":
    main("selection_sort", 100)