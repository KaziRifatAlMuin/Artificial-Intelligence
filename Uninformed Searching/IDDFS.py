# Iterative Deepening DFS (IDDFS) - General Graph (with cycles)

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

def dls(node, goal, limit, visited, order, counter):
    order.append(node)
    counter[0] += 1

    if node == goal:
        return True

    if limit == 0:
        return False

    visited.add(node)

    for child in graph[node]:
        if child not in visited:
            if dls(child, goal, limit - 1, visited, order, counter):
                return True

    return False


# Driver Code
start = 'A'
goal = 'K'

for depth in range(0, 8):
    search_order = []
    visited_counter = [0]

    found = dls(start, goal, depth, set(), search_order, visited_counter)

    print(f"\nDepth Limit = {depth}")
    print("Search Order:", search_order)
    print("Nodes Visited:", visited_counter[0])

    if found:
        print("Goal Found at Depth:", depth)
        break
