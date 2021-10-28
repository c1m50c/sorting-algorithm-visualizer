# Algorithm Imports #
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.gnome_sort import gnome_sort
from algorithms.heap_sort import heap_sort

# Miscellaneous Imports #
from colorama import Style, Fore
from animate_graph import camera
import matplotlib.pyplot as plt
import random


arr_size: int = 30 # Size of the visualized array.
interval_time: int = 75 # Interval between frames.
arr: list[int] = [  ] # Array to visualize being sorted.


ALGORITHMS = {
    # "algorithm_name": algorithm_function,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "gnome_sort": gnome_sort,
    "heap_sort": heap_sort,
}


def main():
    global interval_time
    global arr_size
    
    # Intro #
    print(f"{Style.BRIGHT}{Fore.BLUE}Sorting Algorithm Visualizer{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Default Array Size: {Fore.RESET}{arr_size}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Default Interval: {Fore.RESET}{interval_time}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Valid Algorithms: {Style.RESET_ALL}(")
    for key in ALGORITHMS.keys():
        print(f". {Fore.CYAN}{key}{Fore.RESET}")
    print(")\n")
    
    # Size Input: Set `arr_size` to a user-defined value. #
    size_input: str = input(f"{Style.BRIGHT}{Fore.MAGENTA}size{Fore.YELLOW}:${Style.RESET_ALL} ")
    if size_input.isdigit():
        arr_size = int(size_input)
    else:
        print(f"{Style.BRIGHT}{Fore.RED}ERROR: {Fore.RESET}Cannot convert size input to integer, using default array size.{Style.RESET_ALL}")
    
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
    for i in range(arr_size):
        arr.append(random.randint(0, arr_size))
    
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