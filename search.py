
import time
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
    