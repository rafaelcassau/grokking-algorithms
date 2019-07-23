"""
Quick sort is a sortable algorithm that use divide by conquer strategy by calling itself until each part of array become less than 2 elements

Best case O(N log N)
Average case O(N log N)
Worst case O(N²)

Each time that quicksort is called recursively a O(N) operation is done.
O(log N) is the size of the stack with the amount of recursive calls

In this case the pivot position matters to reach a good performance.

Quicksort and Mergesort has the same asymtotic complexity, but when the complexity is equivalent, the constant C 'time' is important to consider the better performance, and in this context the constant C in Quicksort is more faster than the same constant in Mergesort.
"""


def quicksort(unordered_array):
    if len(unordered_array) < 2:
        return unordered_array
    
    pivot = unordered_array[0]
    less_list = [n for n in unordered_array[1:] if n <= pivot]
    bigger_list = [n for n in unordered_array[1:] if n > pivot]

    return quicksort(less_list) + [pivot] + quicksort(bigger_list)


unordered_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(quicksort(unordered_array))

assert quicksort(unordered_array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
