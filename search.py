
import time
import heapq

# This function reconstructs the solution path from start to goal
# by tracking where each state came from.
def reconstruct_path(came_from, start, goal):
    path = []
    current = goal

    # Follow the path backwards from goal to start
    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    # Reverse it so the path goes from start to goal
    path.reverse()

    return path



## BFS implementation inspired by:
#https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/


def bfs(world):
    start_time = time.perf_counter()
    # States that have already been visited
    visited = []

    # States waiting to be explored
    queue = []

    #to remember previous places
    came_from = {}

    #counts how many nodes BFS expands
    expanded_nodes = 0

    # Start BFS from the initial position
    queue.append(world.start)
    visited.append(world.start)

    while queue:
        # BFS explores the first state in the queue
        current_state = queue.pop(0)
        expanded_nodes += 1


        # Return the solution path if the goal is reached
        if current_state == world.goal:
            path= reconstruct_path(came_from, world.start, world.goal)
            # Number of nodes still waiting in the frontier when the search ends
            frontier_nodes = len(queue)


            end_time = time.perf_counter()
            processing_time = end_time - start_time


            return path, expanded_nodes, frontier_nodes, processing_time


        # Explore all valid neighboring states
        for neighbor in world.get_neighbors(current_state):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                # Remember where this state came from
                came_from[neighbor] = current_state


    end_time = time.perf_counter()
    processing_time = end_time-start_time

    # No solution was found
    return None, expanded_nodes, len(queue), processing_time

def dfs(world):
    start_time = time.perf_counter()

    visited = []
    stack = []
    came_from = {}
    expanded_nodes = 0

    stack.append(world.start)
    visited.append(world.start)

    while stack:
        current_state= stack.pop()
        expanded_nodes += 1

        if current_state == world.goal:
            path = reconstruct_path(came_from, world.start, world.goal)
            frontier_nodes = len(stack)

            end_time = time.perf_counter()
            processing_time = end_time-start_time

            return path, expanded_nodes, frontier_nodes, processing_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)
                came_from[neighbor] = current_state

    end_time = time.perf_counter()
    processing_time = end_time-start_time

    return None, expanded_nodes, len(stack), processing_time

def greedy(world, heuristic):
    start_time = time.perf_counter()

    visited = []
    frontier = []
    came_from = {}
    expanded_nodes = 0

    frontier.append(world.start)
    visited.append(world.start)

    while frontier:
    # Selects the state with the lowest heuristic value.
    # lambda calculates h(n) for 
    # each state so min() can choose the state closest to the goal.
        current_state = min(
            frontier, 
            key = lambda state: heuristic(state, world.goal)
        )

        frontier.remove(current_state)
        expanded_nodes += 1

        if current_state == world.goal:
            path = reconstruct_path(came_from, world.start, world.goal)
            frontier_nodes = len(frontier)

            end_time = time.perf_counter()
            processing_time = end_time - start_time

            return path, expanded_nodes, frontier_nodes, processing_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in visited:
                visited.append(neighbor)
                frontier.append(neighbor)
                came_from[neighbor] = current_state

    end_time = time.perf_counter()
    processing_time = end_time- start_time

    return None, expanded_nodes, len(frontier), processing_time

def astar(world, heuristic):
    start_time = time.perf_counter()

    explored = set()          # Exp: states already expanded
    came_from = {}            # search tree: tracks where each state came from
    expanded_nodes = 0

    g_cost = {world.start: 0}                          # g(n): actual cost from start
    frontier = [(heuristic(world.start, world.goal), world.start)]  # Fr: ordered by f(n); f(n) = g(n) + h(n)

    while frontier:
        f, current_state = heapq.heappop(frontier)

        if current_state in explored:
            continue
        explored.add(current_state)
        expanded_nodes += 1

        if current_state == world.goal:
            path = reconstruct_path(came_from, world.start, world.goal)
            end_time = time.perf_counter()
            return path, expanded_nodes, len(frontier), end_time - start_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in explored:
                g_new = g_cost[current_state] + 1      # cost of each move is 1
                if neighbor not in g_cost or g_new < g_cost[neighbor]:
                    g_cost[neighbor] = g_new
                    f_new = g_new + heuristic(neighbor, world.goal)
                    heapq.heappush(frontier, (f_new, neighbor))
                    came_from[neighbor] = current_state

    end_time = time.perf_counter()
    return None, expanded_nodes, len(frontier), end_time - start_time

