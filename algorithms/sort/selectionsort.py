"""
Selection sort is a sortable algorithm that get min value index and of a array that will be removed that array and gonna be added a new ordered array, (n² - n)/2

Complexity: O(n²)
"""

def select_min_value_index(unordered_array):
    min_value_index = 0
    min_value = unordered_array[0]

    for i in range(len(unordered_array)):
        if unordered_array[i] < min_value:
            min_value = unordered_array[i]
            min_value_index = i

    return min_value_index


def selection_sort(unordered_array):
    ordered_array = []
    
    for i in range(len(unordered_array)):
        min_value_index = select_min_value_index(unordered_array)
        ordered_array.append(unordered_array.pop(min_value_index))
    
    return ordered_array


unordered_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert selection_sort(unordered_array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
