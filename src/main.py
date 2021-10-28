# Algorithm Imports #
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.gnome_sort import gnome_sort
from algorithms.comb_sort import comb_sort
from algorithms.heap_sort import heap_sort

# Miscellaneous Imports #
from rich.table import Table
from rich.console import Console
from animate_graph import camera
import matplotlib.pyplot as plt
import random


arr_size: int = 30 # Size of the visualized array.
interval_time: int = 75 # Interval between frames.
arr: list[int] = [  ] # Array to visualize being sorted.


ALGORITHMS = {
    # "algorithm_name": [algorithm_function, wctc, actc, bctc],
    "selection_sort": [selection_sort, "O(n * n)", "O(n * n)", "O(n * n)"],
    "insertion_sort": [insertion_sort, "O(n * n)", "O(n * n)", "O(n)"],
    "bubble_sort": [bubble_sort, "O(n * n)", "O(n * n)", "O(n)"],
    "quick_sort": [quick_sort, "O(n * n)", "O(n log n)", "O(n log n)"],
    "gnome_sort": [gnome_sort, "O(n * n)", "O(n * n)", "O(n)"],
    "comb_sort": [comb_sort, "O(n * n)", "O(n * n / 2^p)", "O(n log n)"],
    "heap_sort": [heap_sort, "O(n log n)", "O(n log n)", "O(n)"],
}


def main():
    global interval_time
    global arr_size
    console = Console()
    
    # Intro #
    console.print("[bold blue]Sorting Algorithm Visualizer[/bold blue]")
    console.print(f"[bold green]Default Array Size:[/bold green] {arr_size}")
    console.print(f"[bold green]Default Interval:[/bold green]: {interval_time}\n")
    
    # Algorithms Table #
    va_table = Table(title="Algorithms", title_style="bold green")
    va_table.add_column("Input", justify="full", style="bold cyan", no_wrap=True)
    va_table.add_column("Worst Case Time Complexity", justify="full", style="cyan", no_wrap=True)
    va_table.add_column("Average Case Time Complexity", justify="full", style="cyan", no_wrap=True)
    va_table.add_column("Best Case Time Complexity", justify="full", style="cyan", no_wrap=True)
    for key in ALGORITHMS.keys():
        va_table.add_row(key, ALGORITHMS[key][1], ALGORITHMS[key][2], ALGORITHMS[key][3])
    console.print(va_table)
    console.print()
    
    # Size Input: Set `arr_size` to a user-defined value. #
    size_input: str = console.input("[bold][magenta]size[/magenta][yellow]:$[/yellow][/bold] ")
    if size_input.isdigit():
        arr_size = int(size_input)
    else:
        console.print("[bold][red]ERROR:[/red] Cannot convert size input to integer, using default array size.[/bold]")
    
    # Interval Input: Set `interval_time` to a user-defined value. #
    interval_input: str = console.input("[bold][magenta]interval[/magenta][yellow]:$[/yellow][/bold] ")
    if interval_input.isdigit():
        interval_time = int(interval_input)
    else:
        console.print("[bold][red]ERROR:[/red] Cannot convert interval input to integer, using default interval.[/bold]")
    
    # Algorithm Input: Get user-input for which algorithm to run. #
    algorithm_input: str = console.input("[bold][magenta]algorithm[/magenta][yellow]:$[/yellow][/bold] ")
    algorithm_input = algorithm_input.lower()
    
    # Array Creation: Create array for visualization. #
    arr.clear()
    for i in range(arr_size):
        arr.append(random.randint(0, arr_size))
    
    # Algorithm Input Check: Check if the `algorithm_input` contains a valid algorithm, else quit. #
    if algorithm_input in ALGORITHMS.keys():
        ALGORITHMS[algorithm_input][0](arr)
        plt.title(algorithm_input)
    else:
        console.print("[bold][red]ERROR:[/red] Specified algorithm does not exist, quitting[white]...[/white][/bold]")
        quit()
    
    # Animate #
    animation = camera.animate(interval=interval_time)
    plt.show()


if __name__ == "__main__":
    main()