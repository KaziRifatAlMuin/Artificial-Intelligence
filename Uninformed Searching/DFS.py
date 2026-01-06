# Depth-First Search (DFS) - General Undirected Graph (11 nodes, cyclic)

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F', 'C'],   # degree 4
    'C': ['A', 'B', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['B', 'C'],             # cycle: B-C-F-B
    'G': ['C', 'J'],
    'H': ['D'],
    'I': ['E', 'K'],
    'J': ['G'],
    'K': ['I']
}

visited = set()
search_order = []
visited_count = 0

def dfs(node, goal):
    global visited_count

    search_order.append(node)
    visited_count += 1

    if node == goal:
        return True

    visited.add(node)

    for child in graph[node]:
        if child not in visited:
            if dfs(child, goal):
                return True

    return False


# Driver Code
start = 'A'
goal = 'K'

found = dfs(start, goal)

print("DFS Search Order:", search_order)
print("Goal Found:", found)
print("Total Nodes Visited:", visited_count)
