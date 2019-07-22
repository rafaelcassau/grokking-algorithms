"""
Recursive implementation of count

Stack push
f(array=[1, 2, 3, 4, 5])
f(array=[2, 3, 4, 5])
f(array=[3, 4, 5])
f(array=[4, 5])
f(array=[5])

Base case
f(array=[])

Base pop
f(array=[5]) = 1
f(array=[4, 5]) = 2
f(array=[3, 4, 5]) = 3
f(array=[2, 3, 4, 5]) = 4
f(array=[1, 2, 3, 4, 5]) = 5
"""

def recursive_count(array):
    count = 0
    if not array:
        return count

    array.pop()
    count = recursive_count(array)
    return count + 1


assert recursive_count([1, 2, 3, 4, 5]) == 5
assert recursive_count([2, 3, 4, 5]) == 4
assert recursive_count([3, 4, 5]) == 3
assert recursive_count([4, 5]) == 2
assert recursive_count([5]) == 1
assert recursive_count([]) == 0
