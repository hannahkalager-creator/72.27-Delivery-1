from grid_world import GridWorld
from boards import simple_board, start, goal

# Create the Grid World
world = GridWorld(simple_board, start, goal)

# Print basic information
print("Start:", world.start)
print("Goal:", world.goal)

# Test which positions the agent can move to from the start
neighbors = world.get_neighbors(world.start)

print("Possible moves from start:", neighbors)

