# DFS

def dfs(initial, goal):
    stack = [(initial, [initial])]
    visited = set()
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        state, path = stack.pop()
        state_tuple = tuple(tuple(row) for row in state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if state == goal:
            return path

        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    zero_row, zero_col = i, j

        for dr, dc in moves:
            new_row = zero_row + dr
            new_col = zero_col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in state]

                new_state[zero_row][zero_col], \
                new_state[new_row][new_col] = \
                new_state[new_row][new_col], \
                new_state[zero_row][zero_col]

                new_tuple = tuple(tuple(row) for row in new_state)

                if new_tuple not in visited:
                    stack.append((new_state, path + [new_state]))

    return None


# IDS

def recursive_dls(node, goal, limit, path):
    if node == goal:
        return path, "success"

    if limit == 0:
        return None, "cutoff"

    cutoff_occurred = False
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(3):
        for j in range(3):
            if node[i][j] == 0:
                zero_row, zero_col = i, j

    for dr, dc in moves:
        new_row = zero_row + dr
        new_col = zero_col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            child = [row[:] for row in node]

            child[zero_row][zero_col], \
            child[new_row][new_col] = \
            child[new_row][new_col], \
            child[zero_row][zero_col]

            child_tuple = tuple(tuple(row) for row in child)
            path_states = {
                tuple(tuple(row) for row in state) for state in path
            }

            if child_tuple not in path_states:
                result, status = recursive_dls(
                    child, goal, limit - 1, path + [child]
                )

                if status == "cutoff":
                    cutoff_occurred = True
                elif status == "success":
                    return result, "success"

    if cutoff_occurred:
        return None, "cutoff"

    return None, "failure"


def depth_limited_search(initial, goal, limit):
    return recursive_dls(initial, goal, limit, [initial])


def iterative_deepening_search(initial, goal):
    depth = 0

    while True:
        result, status = depth_limited_search(initial, goal, depth)
        print(f"Depth limit {depth}: {status}")

        if status == "success":
            return result

        if status == "failure":
            return None

        depth += 1


def print_puzzle(state):
    for row in state:
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


initial = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

print("8-Puzzle using DFS")
solution = dfs(initial, goal)

if solution:
    print("Goal state reached!")
    print("Number of moves:", len(solution) - 1)
    print("Solution path:\n")

    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution found.")

print("8-Puzzle using IDS")
solution = iterative_deepening_search(initial, goal)

if solution:
    print("\nGoal state reached!")
    print("Number of moves:", len(solution) - 1)
    print("Solution path:\n")

    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution found.")
