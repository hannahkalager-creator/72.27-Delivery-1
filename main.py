from grid_world import GridWorld, MultiAgentGridWorld
from boards import (
    test_board,
    test_goal,
    test_start,
    multi_board,
    multi_start,
    multi_goal
)
from search import bfs, dfs, greedy, astar
from heuristics import manhattan_distance


def calculate_agent_costs(path):
    if not path:
        return []

    positions, _ = path[0]
    agent_costs = [0] * len(positions)

    for i in range(1, len(path)):
        previous_positions, _ = path[i - 1]
        current_positions, _ = path[i]

        for agent_index in range(len(positions)):
            if previous_positions[agent_index] != current_positions[agent_index]:
                agent_costs[agent_index] += 1

    return agent_costs

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



multi_world = MultiAgentGridWorld(
    multi_board,
    multi_start,
    multi_goal
)

print("\nMulti-agent")
print("Start:", multi_world.start)
print("Goal:", multi_world.goal)

print("Possible next states:")

for neighbor in multi_world.get_neighbors(multi_world.start):
    print(neighbor)


multi_path, multi_expanded, multi_frontier, multi_time = bfs(multi_world)

print("\nMulti-agent BFS")
print("Solution:", multi_path)
print("Expanded nodes:", multi_expanded)
print("Frontier nodes:", multi_frontier)
print("Processing time:", multi_time, "seconds")

if multi_path:
    print("Cost:", len(multi_path) - 1)
else:
    print("No solution found.")

if multi_path:
    agent_costs = calculate_agent_costs(multi_path)

    print("Cost per agent:")
    for agent_index, cost in enumerate(agent_costs):
        print(f"Agent {agent_index}: {cost}")

    print("Total movement cost:", sum(agent_costs))



# Run DFS on the multi-agent Grid World
multi_dfs_path, multi_dfs_expanded, multi_dfs_frontier, multi_dfs_time = dfs(multi_world)

print("\nMulti-agent DFS")
print("Solution:", multi_dfs_path)
print("Expanded nodes:", multi_dfs_expanded)
print("Frontier nodes:", multi_dfs_frontier)
print("Processing time:", multi_dfs_time, "seconds")

if multi_dfs_path:
    print("Cost:", len(multi_dfs_path) - 1)

    agent_costs = calculate_agent_costs(multi_dfs_path)

    print("Cost per agent:")
    for agent_index, cost in enumerate(agent_costs):
        print(f"Agent {agent_index}: {cost}")

    print("Total movement cost:", sum(agent_costs))
else:
    print("No solution found.")

