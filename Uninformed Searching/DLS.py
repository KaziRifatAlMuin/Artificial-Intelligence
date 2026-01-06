# Depth-Limited Search (DLS)

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F', 'G'],
    'C': ['A', 'H'],
    'D': ['A'],
    'E': ['B'],
    'F': ['B', 'I'],
    'G': ['B'],
    'H': ['C', 'J'],
    'I': ['F'],
    'J': ['H', 'K'],
    'K': ['J']
}

search_order = []
visited_count = 0

def dls(node, goal, limit, parent=None):
    global visited_count

    search_order.append(node)
    visited_count += 1

    if node == goal:
        return "SUCCESS"

    if limit == 0:
        return "CUTOFF"

    for child in graph[node]:
        if child != parent:  # avoid going back to parent
            result = dls(child, goal, limit - 1, node)
            if result == "SUCCESS":
                return "SUCCESS"

    return "FAILURE"


# Driver Code
start = 'A'
goal = 'K'
depth_limit = 4

result = dls(start, goal, depth_limit)

print("DLS Search Order:", search_order)
print("Result:", result)
print("Depth Limit:", depth_limit)
print("Total Nodes Visited:", visited_count)
