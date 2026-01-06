# Depth-Limited Search (DLS) - General Undirected Graph (with cycles)

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F', 'C'],
    'C': ['A', 'B', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['B', 'C'],
    'G': ['C', 'J'],
    'H': ['D'],
    'I': ['E', 'K'],
    'J': ['G'],
    'K': ['I']
}

search_order = []
visited_count = 0

def dls(node, goal, limit, visited):
    global visited_count

    search_order.append(node)
    visited_count += 1

    if node == goal:
        return "SUCCESS"

    if limit == 0:
        return "CUTOFF"

    visited.add(node)

    for child in graph[node]:
        if child not in visited:
            result = dls(child, goal, limit - 1, visited)
            if result == "SUCCESS":
                return "SUCCESS"

    return "FAILURE"


# Driver Code
start = 'A'
goal = 'K'
depth_limit = 5

result = dls(start, goal, depth_limit, set())

print("DLS Search Order:", search_order)
print("Result:", result)
print("Depth Limit:", depth_limit)
print("Total Nodes Visited:", visited_count)
