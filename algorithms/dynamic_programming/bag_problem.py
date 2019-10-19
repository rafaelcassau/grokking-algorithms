"""
Imagine you are a thief and you have a bag that can fill 4KG and you want to stole
a store, inside the store we have some items:

1 - Guitar   - $ 1.500 1KG
2 - Radio    - $ 3.000 4KG
3 - Notebook - $ 2.000 3KG

You want to fill the bag with the most valueble items, how do you do that?

The best solution requires that you calcule each subset of items for all possibilities and
chose the best one that fill the bag with the most expensive items, the problem behind this
approach is the huge amount of possibilities, to be more expecifically O(2^N) or O(N!),
see bellow some examples:

    3  items 2^3  = 8          possibilities
    4  items 2^4  = 16         possibilities
    5  items 2^5  = 32         possibilities
    6  items 2^6  = 64         possibilities
    32 items 2^32 = 4 billions possibilities

To solve this problem we can use two different approaches, the first one is greedy algorithms
with this approach we can find a approximately good solution, but the best one will be reach
using dynamic programing.

Dynamic programing is a technique that divide the complex problem in a small set of sub problems
and resolve each subproblem progressively, in each iterator we solve a next subproblem,
when the iterator ends we have reached the best solution.

The secret is how the way that you model the problem inside the table.
"""

weights = (0, 1, 2, 3, 4)

products = [
    {"name": "default", "price": 0, "weight": 0},
    {"name": "guitar", "price": 1500, "weight": 1},
    {"name": "radio", "price": 3000, "weight": 4},
    {"name": "notebook", "price": 2000, "weight": 3},
]

# we need to create a empty table where the lines will be the items that can be stolen
# and columns will be virtual bags (weights), because the ideia of dynamic programming is divide
# the complex problem in a small set of subproblems in this case each subproblem will
# be (bags) and we will have virtual bags, each column will represent a bag from 1KG to 4KG.

# to work correctly we need to create a table with one more column and one more line,
# after that we need to initialize these values with zeros (read only)
# these values will not change, however the other ones will be replaced on demand.
def create_matrix(products, weights):
    matrix = []
    for line in range(len(products)):
        matrix.append([0 for i in range(len(weights))])
    return matrix


def get_item_by_weight(product, weight):
    for name, value in product.items():
        if name == "weight" and value <= weight:
            return product["name"], product["weight"], product["price"]
    return ("default", 0, 0)


def stole_store(products, weights):
    matrix = create_matrix(products, weights)

    for line in range(1, len(products)):
        for column_weight in range(1, len(weights)):
            name, weight, current_item_price = get_item_by_weight(products[line], column_weight)
            
            previous_item_price = matrix[line - 1][column_weight]

            remaining_weight = column_weight - weight
            remaining_price_for_weight = matrix[line - 1][remaining_weight]
       
            matrix[line][column_weight] = max(previous_item_price, (current_item_price + remaining_price_for_weight))

    return matrix


matrix = stole_store(products, weights)

assert matrix[1][1] == 1500
assert matrix[1][2] == 1500
assert matrix[1][3] == 1500
assert matrix[1][4] == 1500

assert matrix[2][1] == 1500
assert matrix[2][2] == 1500
assert matrix[2][3] == 1500
assert matrix[2][4] == 3000

assert matrix[3][1] == 1500
assert matrix[3][2] == 1500
assert matrix[3][3] == 2000
assert matrix[3][4] == 3500
