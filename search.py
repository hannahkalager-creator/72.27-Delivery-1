
import time
import heapq
from collections import deque

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
    expanded_nodes = 0
    
    visited = set()
    queue = deque() # States waiting to be explored
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
    start_time = time.perf_counter()
    expanded_nodes = 0

    visited = set()
    stack = [] # A list, not a deque: DFS pops from the end, which is already O(1)
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
    start_time = time.perf_counter()
    expanded_nodes = 0

    visited = set()
    frontier = []
    came_from = {}

    frontier.append(world.state)
    visited.add(world.state)

    while frontier:
    # Selects the state with the lowest heuristic value.
    # lambda calculates h(n) for 
    # each state so min() can choose the state closest to the goal.
        current_state = min(
            frontier,
            key = lambda state: world.heuristic_cost(state, heuristic)
        )

        frontier.remove(current_state)
        expanded_nodes += 1

        if world.all_agents_at_goal(current_state):
            # Rebuild from the reached state; only it is a key in came_from
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
    start_time = time.perf_counter()
    expanded_nodes = 0

    explored = set()          # Exp: states already expanded
    came_from = {}            # search tree: tracks where each state came from
    insertions = 0            # breaks f(n) ties by insertion order

    g_cost = {world.state: 0}                          # g(n): actual cost from start
    # Fr: ordered by f(n); f(n) = g(n) + h(n)
    frontier = [(world.heuristic_cost(world.state, heuristic), insertions, world.state)]

    while frontier:
        f, _, current_state = heapq.heappop(frontier)

        if current_state in explored:
            continue
        explored.add(current_state)
        expanded_nodes += 1

        if world.all_agents_at_goal(current_state):
            # Rebuild from the reached state; only it is a key in came_from
            path = reconstruct_path(came_from, world.state, current_state)
            end_time = time.perf_counter()
            return path, expanded_nodes, len(frontier), end_time - start_time

        for neighbor in world.get_neighbors(current_state):
            if neighbor not in explored:
                g_new = g_cost[current_state] + 1      # cost of each move is 1
                if neighbor not in g_cost or g_new < g_cost[neighbor]:
                    g_cost[neighbor] = g_new
                    f_new = g_new + world.heuristic_cost(neighbor, heuristic)
                    insertions += 1
                    heapq.heappush(frontier, (f_new, insertions, neighbor))
                    came_from[neighbor] = current_state

    end_time = time.perf_counter()
    return None, expanded_nodes, len(frontier), end_time - start_time

