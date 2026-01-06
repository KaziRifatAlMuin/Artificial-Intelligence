maze = [
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1]
]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

explored = set()

def gbfs(maze, start, goal, row, col):
    frontier = []
    cur = 0
    frontier.append(start)

    while(cur < len(frontier)):
        next = frontier[cur]
        for i in range(0, 4):
            next[0] = frontier[cur][0] + dr[i]
            next[1] = frontier[cur][1] + dc[i]
            if(next[0] >= 0 and next[0] < row and next[1] >= 0 and next[1] < col and maze[next[0]][next[1]] == 1):
                if next == goal:
                    return True
                if next not in explored:
                    frontier.append(next)
        explore_next = cur
        cost = 1000000000
        for j in range(cur, len(frontier)):
            node = frontier[j]
            h = abs(node[0] - goal[0]) + abs(node[1] - goal[1])
            if h < cost:
                cost = h
                explore_next = node
        if explore_next not in explored:
            frontier.append(explore_next)
        explored.add(cur)
        cur += 1
    return False

if gbfs(maze, [2, 1], [0, 5], 4, 6):
    print("Nodes visited: ", len(explored))
else:
    print("Not Found")

            



            


