# Depth-First Search (DFS)

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