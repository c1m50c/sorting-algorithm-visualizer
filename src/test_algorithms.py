# Functions that test the algorithm implementations, for `pytest` #

from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.gnome_sort import gnome_sort
from algorithms.shell_sort import shell_sort
from algorithms.comb_sort import comb_sort
from algorithms.heap_sort import heap_sort

from typing import List


def test_selection_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    selection_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_insertion_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    insertion_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_bubble_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    bubble_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_quick_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    quick_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_merge_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    merge_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_gnome_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    gnome_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_shell_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    shell_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_comb_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    comb_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]


def test_heap_sort():
    arr: List[int] = [ 5, 3, 2, 1, 5 ]
    heap_sort(arr)
    assert arr == [ 1, 2, 3, 5, 5 ]