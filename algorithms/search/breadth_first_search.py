"""
Graph is a data structure with vertex and edges, an edge is a
representation of a relationship between two vertex, ex:
A -- B is the same of B -- A


A DiGraph is a direct graph with arrows pointing to the next item ex:
A -> B -> C


Breadth First Search says if there are a path from A to B
If there are a path, the breadth first search gives the minimum path

Breadth First Search has O(V + E) complexity, where V is the number of
vertex and E is a number of edges, then it's complexity is O(N)


Applications:

1 - Write a AI algorithm that calcule the minimum amount of necessary
moviments to win a checkers game.

2 - Write a Spell Checker that calcule the minimum number of editions
to fix a wrong message in a correct message, ex: REABER to READER

3 - Find the doctor that suits your health plan most close to you
"""
from collections import deque


di_graph = {}

# direct friends
di_graph["You"] = ["Claire", "Alice", "Bob"]

# friends of friends
di_graph["Bob"] = ["Anuj", "Peggy"]
di_graph["Claire"] = ["Thom", "Jonny"]
di_graph["Alice"] = ["Peggy"]

# friends of friends of friends
di_graph["Anuj"] = []
di_graph["Peggy"] = []
di_graph["Thom"] = []
di_graph["Jonny"] = []

# no relation
di_graph["Alone"] = []


def breadth_first_search(di_graph, from_vertice, to_vertice):
    verified_list = set()
    queue_to_search = deque()
    queue_to_search.extend(di_graph[from_vertice])
    while queue_to_search:
        friend = queue_to_search.popleft()
        if friend not in verified_list:
            if friend == to_vertice:
                return True

        queue_to_search.extend(di_graph[friend])
        verified_list.add(friend)

    return False


assert breadth_first_search(di_graph, "You", "Bob") is True
assert breadth_first_search(di_graph, "You", "Claire") is True
assert breadth_first_search(di_graph, "You", "Alice") is True

assert breadth_first_search(di_graph, "You", "Anuj") is True
assert breadth_first_search(di_graph, "You", "Peggy") is True
assert breadth_first_search(di_graph, "You", "Thom") is True
assert breadth_first_search(di_graph, "You", "Jonny") is True

assert breadth_first_search(di_graph, "You", "Alone") is False
