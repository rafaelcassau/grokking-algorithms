"""
You are a greedy stolen and you are at a store with your bag that can hold 16 pounds.
Inside the store has a lot of objects and your strategy is to stole more expensive objects that
fit inside your bag. To do that you follow the steps below:

1 - Get the more expensive item that fits inside your bag.
2 - Get the next more expensive item that fits inside your bag, and so on.

In this example the greedy algorithm doesn't work as expected. For example, supose there are 3 items
that can be stoled.

Radio    - R$ 3.000 - 13KG
Notebook - R$ 2.000 -  9KG
Guitar   - R$ 1.500 -  6KG

On the first step you stole the Radio, that is the more expensive item,
but after that no more items can fit inside your bag, it means that you
have 3 pounds of free space that can't be used anymore, because the remaing
items can't fit there.

You stole R$ 3.000, but if you had stoled the notebook and the guitar you could have R$ 3.500!

Clearly the greedy algorithm does not offer the best strategy here, but you have an approximate solution,
and it's good!
"""

from collections import namedtuple


Item = namedtuple("Item", ["name", "price", "weight"])


bag_16kg = []
items = [
    Item(name="radio", price=3000, weight=13),
    Item(name="notebook", price=2000, weight=9),
    Item(name="guitar", price=1500, weight=6),
]


def _get_more_expensive_item_that_fit_inside_the_bag(items, remaining_weight):
    expensive_item = Item(name="fake", price=0, weight=0)
    for item in items:
        if item.price >= expensive_item.price and item.weight <= remaining_weight:
            expensive_item = item
    return expensive_item if expensive_item.name != "fake" else None


def stolen_store(items, bag_16kg):
    remaining_weight = 16
    while items:
        item = _get_more_expensive_item_that_fit_inside_the_bag(items, remaining_weight)
        if item is None:
            break
        
        bag_16kg.append(item.name)
        remaining_weight -= item.weight
        items.remove(item)

    return bag_16kg


stolen_bag16kg = stolen_store(items, bag_16kg)
assert stolen_bag16kg == ["radio"]
