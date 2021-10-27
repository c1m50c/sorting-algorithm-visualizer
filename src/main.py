from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort

from colorama import Style, Fore
from animate_graph import camera
import matplotlib.pyplot as plt
import numpy as np
import random


ARR_SIZE: int = 30 # Size of the visualized array.
interval_time: int = 75 # Interval between frames.
arr: list[int] = [  ] # Array to visualize being sorted.


ALGORITHMS = {
    # "algorithm_name": algorithm_function,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
}


def main():
    global interval_time
    print(f"{Style.BRIGHT}{Fore.BLUE}Visual Sorting Algorithms{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Default Interval: {Fore.RESET}{interval_time}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Valid Algorithms: {Style.RESET_ALL}(")
    for key in ALGORITHMS.keys():
        print(f". {Fore.CYAN}{key}{Fore.RESET}")
    print(")\n")
    
    # Interval Input: Set `interval_time` to a user-defined value. #
    interval_input: str = input(f"{Style.BRIGHT}{Fore.MAGENTA}interval{Fore.YELLOW}:${Style.RESET_ALL} ")
    if interval_input.isdigit():
        interval_time = int(interval_input)
    else:
        print(f"{Style.BRIGHT}{Fore.RED}ERROR: {Fore.RESET}Cannot convert interval input to integer, using default interval.{Style.RESET_ALL}")
    
    # Algorithm Input: Get user-input for which algorithm to run. #
    algorithm_input: str = input(f"{Style.BRIGHT}{Fore.MAGENTA}algorithm{Fore.YELLOW}:${Style.RESET_ALL} ")
    algorithm_input = algorithm_input.lower()
    
    # Array Creation: Create array for visualization. #
    arr.clear()
    for i in range(ARR_SIZE):
        arr.append(random.randint(0, ARR_SIZE))
    
    # Algorithm Input Check: Check if the `algorithm_input` contains a valid algorithm, else quit. #
    if algorithm_input in ALGORITHMS.keys():
        ALGORITHMS[algorithm_input](arr)
    else:
        quit()
    
    # Animate #
    animation = camera.animate(interval=interval_time)
    plt.show()


if __name__ == "__main__":
    main()