import heapq


def manhattan_distance(state, goal):
    distance = 0

    for i in range(3):
        for j in range(3):
            tile = state[i][j]

            if tile != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == tile:
                            distance += abs(i - x) + abs(j - y)

    return distance


def get_neighbors(state):
    neighbors = []

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j
                break
        else:
            continue
        break

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [r[:] for r in state]

            new_state[row][col], new_state[new_row][new_col] = (
                new_state[new_row][new_col],
                new_state[row][col]
            )

            neighbors.append(new_state)

    return neighbors


def a_star(initial, goal):
    open_list = []
    closed = set()
    parent = {}
    g = {}
    states = {}

    start = tuple(map(tuple, initial))
    goal_state = tuple(map(tuple, goal))

    g[start] = 0
    states[start] = initial

    h = manhattan_distance(initial, goal)
    heapq.heappush(open_list, (h, 0, start))

    while open_list:
        f, current_g, current = heapq.heappop(open_list)

        if current in closed:
            continue

        current_state = states[current]

        if current == goal_state:
            path = []

            while current in parent:
                path.append(states[current])
                current = parent[current]

            path.append(initial)
            path.reverse()

            return path

        closed.add(current)

        for neighbor in get_neighbors(current_state):
            neighbor_key = tuple(map(tuple, neighbor))
            new_g = current_g + 1

            if neighbor_key not in closed and (
                neighbor_key not in g or new_g < g[neighbor_key]
            ):
                parent[neighbor_key] = current
                g[neighbor_key] = new_g
                states[neighbor_key] = neighbor

                h = manhattan_distance(neighbor, goal)
                new_f = new_g + h

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor_key)
                )

    return None


def print_puzzle(state):
    for row in state:
        print(" ".join("_" if tile == 0 else str(tile) for tile in row))
    print()


initial = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solution = a_star(initial, goal)

if solution:
    print("Goal state reached!")
    print("Depth:", len(solution) - 1)

    for i, state in enumerate(solution):
        print("Step", i)
        print_puzzle(state)
else:
    print("Failure: No solution found.")
