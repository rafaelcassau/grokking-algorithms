"""
Binary search is a searchable algorithm that use divide by conquer strategy.

Complexity: O(log n)
"""

def binary_search(ordered_array, searchable):
    lower = 0
    higher = len(ordered_array) - 1
    while lower <= higher:
        half = (lower + higher) // 2
        item = ordered_array[half]

        if item == searchable:
            return half

        if item > searchable:
            higher = half - 1
            continue

        if item < searchable:
            lower = half + 1
            continue

    return None


ordered_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert binary_search(ordered_array, 10) == 9
assert binary_search(ordered_array, 5) == 4
assert binary_search(ordered_array, 0) is None
assert binary_search(ordered_array, 11) is None
