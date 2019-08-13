from collections import defaultdict

"""

"""

direct_acyclic_graph = {
    "book": {"LP": 5, "poster": 0},
    "LP": {"guitar": 15, "drums": 20},
    "guitar": {"piano": 20},
    "drums": {"piano": 10},
    "poster": {"guitar": 20, "drums": 35},
    "piano": {},
}


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

    # populate costs of each vertex
    for vertex, cost in graph[first].items():
        costs[vertex] = cost
            
    # populate parents of each vertex
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


result = dijkstra(direct_acyclic_graph, "book")
print(result)
