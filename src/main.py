# Algorithm Imports #
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.gnome_sort import gnome_sort
from algorithms.shell_sort import shell_sort
from algorithms.comb_sort import comb_sort
from algorithms.heap_sort import heap_sort

# Miscellaneous Imports #
from random import randint
from rich.table import Table
from rich.console import Console
from animate_graph import camera
import matplotlib.pyplot as plt


arr_size: int = 30 # Size of the visualized array.
interval_time: int = 75 # Interval between frames.
arr: list[int] = [  ] # Array to visualize being sorted.


ALGORITHMS = {
    # "algorithm_name": [algorithm_function, wctc, actc, bctc],
    "selection_sort": [selection_sort, "O(n * n)", "O(n * n)", "O(n * n)"],
    "insertion_sort": [insertion_sort, "O(n * n)", "O(n * n)", "O(n)"],
    "bubble_sort": [bubble_sort, "O(n * n)", "O(n * n)", "O(n)"],
    "quick_sort": [quick_sort, "O(n * n)", "O(n log n)", "O(n log n)"],
    "merge_sort": [merge_sort, "O(n log n)", "O(n log n)", "O(n log n)"],
    "gnome_sort": [gnome_sort, "O(n * n)", "O(n * n)", "O(n)"],
    "shell_sort": [shell_sort, "O(?)", "O(?)", "O(?)"],
    "comb_sort": [comb_sort, "O(n * n)", "O(n * n / 2^i)", "O(n log n)"],
    "heap_sort": [heap_sort, "O(n log n)", "O(n log n)", "O(n)"],
}


def main():
    global interval_time
    global arr_size
    
    # Intro #
    console = Console()
    console.print("[bold blue]Sorting Algorithm Visualizer[/bold blue]")
    console.print(f"[bold][green]Default Array Size:[/green] [cyan]{arr_size}[/cyan][/bold]")
    console.print(f"[bold][green]Default Interval:[/green] [cyan]{interval_time}ms[/cyan][/bold]\n")
    
    # Sorting Algorithms Table: Table displaying sorting algorithms and their time complexities. #
    sa_table = Table(title="Sorting Algorithms", title_style="bold green", show_lines=True)
    sa_table.add_column("Algorithm", justify="center", style="bold cyan", no_wrap=True)
    sa_table.add_column("Worst Case Time Complexity", justify="center", style="bold red", no_wrap=True)
    sa_table.add_column("Average Case Time Complexity", justify="center", style="bold yellow", no_wrap=True)
    sa_table.add_column("Best Case Time Complexity", justify="center", style="bold green", no_wrap=True)
    for key in ALGORITHMS.keys():
        sa_table.add_row(key, ALGORITHMS[key][1], ALGORITHMS[key][2], ALGORITHMS[key][3])
    console.print(sa_table)
    console.print()
    
    # Size Input: Set `arr_size` to a user-defined value. #
    size_input: str = console.input("[bold][magenta]size~int[/magenta][yellow]:$[/yellow][/bold] ")
    if size_input.isdigit():
        if int(size_input) >= 1:
            arr_size = int(size_input)
        else:
            console.print("[bold][red]ERROR:[/red] Specified size input is too small, using default array size.[/bold]")
    else:
        console.print("[bold][red]ERROR:[/red] Cannot convert size input to integer, using default array size.[/bold]")
    
    # Interval Input: Set `interval_time` to a user-defined value. #
    interval_input: str = console.input("[bold][magenta]interval~ms[/magenta][yellow]:$[/yellow][/bold] ")
    if interval_input.isdigit():
        interval_time = int(interval_input)
    else:
        console.print("[bold][red]ERROR:[/red] Cannot convert interval input to integer, using default interval.[/bold]")
    
    # Algorithm Input: Get user-input for which algorithm to run. #
    algorithm_input: str = console.input("[bold][magenta]algorithm~str[/magenta][yellow]:$[/yellow][/bold] ")
    algorithm_input = algorithm_input.lower()
    
    # Array Creation: Create array for visualization. #
    arr.clear()
    for _ in range(arr_size):
        arr.append(randint(0, arr_size))
    
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
    main()


if __name__ == "__main__":
    main()