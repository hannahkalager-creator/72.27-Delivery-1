from grid_world import GridWorld
from boards import test_board, test_goal, test_start
from search import bfs, dfs, greedy, astar #imports the search algorithms
from heuristics import manhattan_distance


# Create the Grid World
world = GridWorld(test_board, test_start, test_goal)

# Print basic information
print("Start:", world.start)
print("Goal:", world.goal)

# Test which positions the agent can move to from the start
neighbors = world.get_neighbors(world.start)

print("Possible moves from start:", neighbors)

#run BFS
path, expanded_nodes, frontier_nodes, processing_time = bfs(world)

print("BFS solution:", path)
print("Expanded nodes:", expanded_nodes)
print("Frontier nodes:", frontier_nodes)
print("Processing time:", processing_time, "seconds")

#this is to find the cost
if path:
    cost = len(path) - 1
    print("BFS cost:", cost)
else:
    print("No solution found.")


# Run DFS
dfs_path, dfs_expanded, dfs_frontier, dfs_time = dfs(world)

print("\nDFS")
print("DFS solution:", dfs_path)
print("Expanded nodes:", dfs_expanded)
print("Frontier nodes:", dfs_frontier)
print("Processing time:", dfs_time, "seconds")

if dfs_path:
    dfs_cost = len(dfs_path) - 1
    print("DFS cost:", dfs_cost)
else:
    print("No solution found.")

# Run Greedy Search using Manhattan distance
greedy_path, greedy_expanded, greedy_frontier, greedy_time = greedy(
    world, manhattan_distance
)

print("\nGreedy")
print("Greedy solution:", greedy_path)
print("Expanded nodes:", greedy_expanded)
print("Frontier nodes:", greedy_frontier)
print("Processing time:", greedy_time, "seconds")

if greedy_path:
    greedy_cost = len(greedy_path) - 1
    print("Greedy cost:", greedy_cost)
else:
    print("No solution found.")

# Run A*
astar_path, astar_expanded, astar_frontier, astar_time = astar(world, manhattan_distance)

print("\nA*")
print("A* solution:", astar_path)
print("Expanded nodes:", astar_expanded)
print("Frontier nodes:", astar_frontier)
print("Processing time:", astar_time, "seconds")

if astar_path:
    print("A* cost:", len(astar_path) - 1)
else:
    print("No solution found.")
