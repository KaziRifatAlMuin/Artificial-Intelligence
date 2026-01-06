# Bidirectional Search - General Undirected Graph (with cycles)

from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F', 'C'],
    'C': ['A', 'B', 'G', 'F'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['B', 'C'],
    'G': ['C', 'J'],
    'H': ['D'],
    'I': ['E', 'K'],
    'J': ['G'],
    'K': ['I']
}

def bidirectional_search(start, goal):
    if start == goal:
        return True

    frontier_fwd = deque([start])
    frontier_bwd = deque([goal])

    visited_fwd = {start}
    visited_bwd = {goal}

    order_fwd = []
    order_bwd = []

    while frontier_fwd and frontier_bwd:
        # Forward expansion
        node_fwd = frontier_fwd.popleft()
        order_fwd.append(node_fwd)

        for neighbor in graph[node_fwd]:
            if neighbor in visited_bwd:
                print("Meeting Node:", neighbor)
                return True, order_fwd, order_bwd
            if neighbor not in visited_fwd:
                visited_fwd.add(neighbor)
                frontier_fwd.append(neighbor)

        # Backward expansion
        node_bwd = frontier_bwd.popleft()
        order_bwd.append(node_bwd)

        for neighbor in graph[node_bwd]:
            if neighbor in visited_fwd:
                print("Meeting Node:", neighbor)
                return True, order_fwd, order_bwd
            if neighbor not in visited_bwd:
                visited_bwd.add(neighbor)
                frontier_bwd.append(neighbor)

    return False, order_fwd, order_bwd


# Driver Code
start = 'A'
goal = 'K'

found, fwd_order, bwd_order = bidirectional_search(start, goal)

print("\nForward Search Order:", fwd_order)
print("Backward Search Order:", bwd_order)
print("Total Nodes Visited:", len(fwd_order) + len(bwd_order))
print("Goal Found:", found)
