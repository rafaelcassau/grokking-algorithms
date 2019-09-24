"""
Supose that you have a class room and you want to reserve the maximum amount of classes there.
You receive a class list but you can't schedule all those classes because some classes conflict with others.

It's sound like a hard problem isn't. But the truth is that, the algorithm is so simple that can surprise you.
Look the solution bellow:

1 - Take the class that ends early. This is the first class that you schedule.
2 - Now you should take the next class that starts after last class that you had took. Again take the class that ends early.
3 - Repeat this these pass for each class of the list and you will find the correct answer.

This os the beault of greedy algorithm, it's so easy. For each iteration it's find the best choice and at the end you will have
ideal overall solution.

When you have NP problem (Nondeterministic polynomial time) like a (travelling salesman problem) you should use a greedy algorithm strategy
this kind of problem is so hard to solve and require a lot o computional power to do that, then with greedy algorithm you can reach a approximately
solution doing the best choice for each iteration, it's not the best solution but it's good enough.

How to check if a problem is a NP complexity:

1 - Your algorithm runs fast with some items, but run much more slowly when more items are added.
2 - "All combinations of X" usually means a NP problem.
3 - You should calculate "each possible version of X" because you can't divide in small problems? Maybe it is a NP problem.
4 - If your problem require a sequence like a sequence of cities, like the (travelling salesman problem) and it's hard to solve,
    it can be a NP problem.
5 - If your problem is (minumum set coverage) like "How to cover all united states with the less amount of radio stations"
    you probably have a NP problem.


Greedy algorithms optimize locally to reach approximately in a global optimization.

NP problems doesn't have a fast solution.

If you're trying to solve a NP problem, the best way to do that is writing a greedy algorithm.

Greedy algorithm are easy to write and have smaller Big(O), therefore they are good choices to 
solve a NP problem with approximation strategy.
"""

classes = [
    ("arts", (9, 10)),
    ("english", (9.3, 10.3)),
    ("math", (10, 11)),
    ("cc", (10.3, 11.3)),
    ("music", (11, 12)),
]


def _get_class_that_ends_more_early(classes):
    ends_more_early = classes[0]
    for c in classes[1:]:
        if c[1][1] < ends_more_early[1][1]:
            ends_more_early = c
    return ends_more_early


def _get_next_class_that_starts_after_last_class_and_ends_more_early(last_class, classes, visited_classes):
    for c in classes:
        if c not in visited_classes:
            if c[1][0] >= last_class[1][1]:
                return c
    return None


def schedule_classes(classes):
    scheduled_classes = []
    visited_classes = set()
    ends_more_early = _get_class_that_ends_more_early(classes)
    visited_classes.add(ends_more_early)
    scheduled_classes.append(ends_more_early[0])

    for c in classes:
        next_class = _get_next_class_that_starts_after_last_class_and_ends_more_early(ends_more_early, classes, visited_classes)
        if next_class:
            scheduled_classes.append(next_class[0])
            ends_more_early = next_class
            visited_classes.add(next_class)

    return scheduled_classes


scheduled_classes = schedule_classes(classes)
assert scheduled_classes == ["arts", "math", "music"]

