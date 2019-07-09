"""
Recursive implementation of factorial, f(5) = 5 * 4 * 3 * 2 * 1

Stack push
f(n=5 * f(4))
f(n=4 * f(3))
f(n=3 * f(2))
f(n=2 * f(1))

Base case
f(n=1)

Stack pop
f(n=2, * f(1)) = 2
f(n=3, * f(2)) = 6
f(n=4, * f(3)) = 24
f(n=5, * f(4)) = 120
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)



assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720

