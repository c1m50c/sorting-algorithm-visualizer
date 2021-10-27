from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort

from colorama import Style, Fore
from animate_graph import camera
import matplotlib.pyplot as plt
import numpy as np
import random


ARR_SIZE: int = 30
INTERVAL_TIME: int = 100
arr: list[int] = [  ]


ALGORITHMS = {
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
}


def main():
    print(f"{Style.BRIGHT}{Fore.BLUE}Visual Sorting Algorithms{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Valid Algorithms: {Style.RESET_ALL}(")
    for key in ALGORITHMS.keys():
        print(f". {Fore.CYAN}{key}{Fore.RESET}")
    
    print(")\n")
    inp: str = input(f"{Style.BRIGHT}{Fore.MAGENTA}algorithm{Fore.YELLOW}:${Style.RESET_ALL} ")
    inp = inp.lower()
    
    
    arr.clear()
    for i in range(ARR_SIZE):
        arr.append(random.randint(0, ARR_SIZE))
    
    if inp in ALGORITHMS.keys():
        ALGORITHMS[inp](arr)
    else:
        quit()
    
    animation = camera.animate(interval=INTERVAL_TIME)
    plt.show()


if __name__ == "__main__":
    main()