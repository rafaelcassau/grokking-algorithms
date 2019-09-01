from collections import defaultdict

"""
Dijkstra algorithm can calcule the shortest path in a Direct Acyclic Graph or DAG
DAG is a acyclic digraph that has weight in each of its edges.

The main difference between BFS and Dijkstra algorithm is that:

BFS: find the shortest path in a DAG that has no weight on its edges (unweighted graph),
it means the shortest path will be the path with lowest amount of edges.

Dijkstra: find the shortest path in a DAG that has weight on its edges (weighted graph),
it means that the shortest path can have more edges but the weight's sum of that edges
is less than a path with less edges but with a bigger weight sum.

Dijkstra algorithm does not work in cyclic graphs or acyclic graphs with negative weight.

If your graph have negative weight then you should use Bellman-Ford algorithm.

Steps:

1 - Find the cheapest vertice.
2 - Update the cost of the neighbors of this vertex, if some neighboor's cost was updated
    you should to update the vertex parent and mark the vertex as processed too.
3 - Repeat it until will have done this for each vertex of the graph.
4 - Calcule the final path.

Complexity:
    Dijkstra algorithm as O(E + V log V) complexity, where V is the number of
    vertex and E is a number of edges, then it's complexity is O(N log N)
"""


def _find_node_with_lowest_cost(costs, processed):
    node = None
    lowest_cost = float("inf")

    for vertex, cost in costs.items():
        if vertex in processed:
            continue
        
        if cost < lowest_cost:
            lowest_cost = cost
            node = vertex        

    return node


def dijkstra(graph, first):
    costs = defaultdict(lambda: float("inf"))
    parents = defaultdict(lambda: None)
    processed = []

    # populate costs of first vertex
    for vertex, cost in graph[first].items():
        costs[vertex] = cost
            
    # populate parents of first vertex
    for vertex in graph[first].keys():
        parents[vertex] = first 

    node = _find_node_with_lowest_cost(costs, processed)

    while node is not None:
        cost = costs[node]
        neighboors = graph[node]

        for neighboor in neighboors.keys():
            new_cost = cost + neighboors[neighboor]
            if costs[neighboor] > new_cost:
                costs[neighboor] = new_cost
                parents[neighboor] = node

        processed.append(node)
        node = _find_node_with_lowest_cost(costs, processed)
    
    return dict(costs)


exchange_graph = {
    "book": {"LP": 5, "poster": 0},
    "LP": {"guitar": 15, "drums": 20},
    "guitar": {"piano": 20},
    "drums": {"piano": 10},
    "poster": {"guitar": 20, "drums": 35},
    "piano": {},
}

result = dijkstra(exchange_graph, "book")

assert result["LP"] == 5
assert result["poster"] == 0
assert result["guitar"] == 20
assert result["drums"] == 25
assert result["piano"] == 35


more_faster_path = {
    "home": {"park": 6, "school": 2},
    "school": {"park": 1, "office": 5},
    "park": {"office": 3},
    "office": {},
}

result = dijkstra(more_faster_path, "home")

assert result["park"] == 3
assert result["school"] == 2
assert result["office"] == 6

