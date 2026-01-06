# Iterative Deepening DFS (IDDFS)

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

def dls(node, goal, limit, parent, order, counter):
    order.append(node)
    counter[0] += 1

    if node == goal:
        return True

    if limit == 0:
        return False

    for child in graph[node]:
        if child != parent:
            if dls(child, goal, limit - 1, node, order, counter):
                return True

    return False


# Driver Code
start = 'A'
goal = 'K'

for depth in range(0, 8):
    search_order = []
    visited_counter = [0]

    found = dls(start, goal, depth, None, search_order, visited_counter)

    print(f"\nDepth Limit = {depth}")
    print("Search Order:", search_order)
    print("Nodes Visited:", visited_counter[0])

    if found:
        print("Goal Found at Depth:", depth)
        break