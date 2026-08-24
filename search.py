
import time
import heapq
from collections import deque


def reconstruct_path(came_from, start, goal):
    """This function reconstructs the solution path from start to goal 
    by tracking where each state came from."""
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


def bfs(world):
    """This function implements the Breadth-First Search (BFS) algorithm 
    to find the shortest path from the start state to the goal state in a grid world.
    It is inspired by https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/."""
    start_time = time.perf_counter()
    expanded_nodes = 0
    visited = set()
    queue = deque()
    came_from = {}
    queue.append(world.state)
    visited.add(world.state)

    while queue:
        current_state = queue.popleft()
        expanded_nodes += 1

        if world.all_agents_at_goal(current_state):
            path= reconstruct_path(came_from, world.state, current_state)
            frontier_nodes = len(queue)
            end_time = time.perf_counter()
            processing_time = end_time - start_time
            return path, expanded_nodes, frontier_nodes, processing_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                came_from[neighbor] = current_state

    end_time = time.perf_counter()
    processing_time = end_time-start_time
    return None, expanded_nodes, len(queue), processing_time


def dfs(world):
    """This function implements the Depth-First Search (DFS) algorithm 
    to find a path from the start state to the goal state in a grid world."""
    start_time = time.perf_counter()
    expanded_nodes = 0
    visited = set()
    stack = []
    came_from = {}
    stack.append(world.state)
    visited.add(world.state)

    while stack:
        current_state= stack.pop()
        expanded_nodes += 1

        if world.all_agents_at_goal(current_state):
            path = reconstruct_path(came_from, world.state, current_state)
            frontier_nodes = len(stack)
            end_time = time.perf_counter()
            processing_time = end_time-start_time
            return path, expanded_nodes, frontier_nodes, processing_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                came_from[neighbor] = current_state

    end_time = time.perf_counter()
    processing_time = end_time-start_time
    return None, expanded_nodes, len(stack), processing_time


def greedy(world, heuristic):
    """This function implements the Greedy Best-First Search algorithm 
    to find a path from the start state to the goal state in a grid world, 
    using a specified heuristic function to estimate the cost from the current state to the goal state."""
    start_time = time.perf_counter()
    expanded_nodes = 0
    visited = set()
    frontier = []
    came_from = {}
    frontier.append(world.state)
    visited.add(world.state)

    while frontier:
        current_state = min(frontier, key = lambda state: world.heuristic_cost(state, heuristic))
        frontier.remove(current_state)
        expanded_nodes += 1

        if world.all_agents_at_goal(current_state):
            path = reconstruct_path(came_from, world.state, current_state)
            frontier_nodes = len(frontier)
            end_time = time.perf_counter()
            processing_time = end_time - start_time
            return path, expanded_nodes, frontier_nodes, processing_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append(neighbor)
                came_from[neighbor] = current_state

    end_time = time.perf_counter()
    processing_time = end_time- start_time
    return None, expanded_nodes, len(frontier), processing_time


def astar(world, heuristic):
    """This function implements the A* search algorithm 
    to find the shortest path from the start state to the goal state in a grid world, 
    using a specified heuristic function to estimate the cost from the current state to the goal state. 
    The A* algorithm combines the actual cost from the start state (g(n)) and the estimated cost to the goal state (h(n)) 
    to prioritize which states to explore next."""
    start_time = time.perf_counter()
    expanded_nodes = 0
    explored = set()
    came_from = {}
    insertions = 0
    g_cost = {world.state: 0}
    frontier = [(world.heuristic_cost(world.state, heuristic), insertions, world.state)]

    while frontier:
        f, _, current_state = heapq.heappop(frontier)
        if current_state in explored:
            continue
        explored.add(current_state)
        expanded_nodes += 1

        if world.all_agents_at_goal(current_state):
            path = reconstruct_path(came_from, world.state, current_state)
            end_time = time.perf_counter()
            processing_time = end_time - start_time
            return path, expanded_nodes, len(frontier),processing_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in explored:
                g_new = g_cost[current_state] + 1
                if neighbor not in g_cost or g_new < g_cost[neighbor]:
                    g_cost[neighbor] = g_new
                    f_new = g_new + world.heuristic_cost(neighbor, heuristic)
                    insertions += 1
                    heapq.heappush(frontier, (f_new, insertions, neighbor))
                    came_from[neighbor] = current_state

    end_time = time.perf_counter()
    processing_time = end_time- start_time
    return None, expanded_nodes, len(frontier), processing_time