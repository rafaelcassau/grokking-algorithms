"""
Recursive implementation of biggest number

Stack push
f(array=[5, 4, 3, 2, 1])
f(array=[4, 3, 2, 1])
f(array=[3, 2, 1])
f(array=[2, 1])
f(array=[1])

Base case
f(array=[])

Stack pop
f(array=[1]) = 1
f(array=[2, 1]) = 2
f(array=[3, 2, 1]) = 3
f(array=[4, 3, 2, 1]) = 4
f(array=[5, 4, 3, 2, 1]) = 5
"""

def recursive_biggest_number(array):
    if not array:
        return None

    biggest = array.pop()
    other = recursive_biggest_number(array)
    if other is not None and other > biggest:
        biggest = other

    return biggest

assert recursive_biggest_number([5, 4, 3, 2, 1]) == 5
assert recursive_biggest_number([4, 3, 2, 1]) == 4
assert recursive_biggest_number([3, 2, 1]) == 3
assert recursive_biggest_number([2, 1]) == 2
assert recursive_biggest_number([1]) == 1
assert recursive_biggest_number([]) is None
