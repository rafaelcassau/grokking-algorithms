"""
Recursive implementation of sum

Stack push
f(array=[1, 2, 3, 4, 5])
f(array=[2, 3, 4, 5])
f(array=[3, 4, 5])
f(array=[4, 5])
f(array=[5])

Base case
f(array=[])

Stack pop
f(array=[5]) = 5
f(array=[4, 5]) = 9
f(array=[3, 4, 5]) = 12
f(array=[2, 3, 4, 5]) = 14
f(array=[1, 2, 3, 4, 5]) = 15
"""

def recursive_sum(array):
    if not array:
        return 0

    result = array.pop(0)
    return result + recursive_sum(array)


assert sum([]) == 0
assert sum([1]) == 1
assert sum([1, 2]) == 3
assert sum([1, 2, 3]) == 6
assert sum([1, 2, 3, 4]) == 10
assert sum([1, 2, 3, 4, 5]) == 15
