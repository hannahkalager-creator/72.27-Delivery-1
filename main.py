from grid_world import GridWorld
from boards import simple_board, start, goal
from search import bfs #imports BFS

# Create the Grid World
world = GridWorld(simple_board, start, goal)

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

