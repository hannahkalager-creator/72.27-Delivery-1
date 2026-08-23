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
from heuristics import (
    manhattan_distance,
    euclidean_distance,
    weighted_manhattan
)

from game_visual import visualize


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


def report_multi_agent(label, result):
    path, expanded_nodes, frontier_nodes, processing_time = result

    print(f"\n{label}")
    print("Solution:", path)
    print("Expanded nodes:", expanded_nodes)
    print("Frontier nodes:", frontier_nodes)
    print("Processing time:", processing_time, "seconds")

    if not path:
        print("No solution found.")
        return

    print("Turn cost:", len(path) - 1)

    agent_costs = calculate_agent_costs(path)

    print("Movement cost per agent:")
    for agent_index, cost in enumerate(agent_costs):
        print(f"Agent {agent_index}: {cost}")

    print("Total movement cost:", sum(agent_costs))


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

visualize(world, [path])

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
visualize(world, [path])
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

# Run A* with Manhattan distance
astar_path, astar_expanded, astar_frontier, astar_time = astar(
    world, manhattan_distance
)

print("\nA* with Manhattan distance")
print("A* solution:", astar_path)
print("Expanded nodes:", astar_expanded)
print("Frontier nodes:", astar_frontier)
print("Processing time:", astar_time, "seconds")

if astar_path:
    print("A* cost:", len(astar_path) - 1)
else:
    print("No solution found.")

# Run A* with Euclidean distance
euclidean_path, euclidean_expanded, euclidean_frontier, euclidean_time = astar(
    world, euclidean_distance
)

print("\nA* with Euclidean distance")
print("A* solution:", euclidean_path)
print("Expanded nodes:", euclidean_expanded)
print("Frontier nodes:", euclidean_frontier)
print("Processing time:", euclidean_time, "seconds")

if euclidean_path:
    print("A* cost:", len(euclidean_path) - 1)
else:
    print("No solution found.")

# Run A* with weighted Manhattan
weighted_path, weighted_expanded, weighted_frontier, weighted_time = astar(
    world, weighted_manhattan
)

print("\nA* with weighted Manhattan")
print("A* solution:", weighted_path)
print("Expanded nodes:", weighted_expanded)
print("Frontier nodes:", weighted_frontier)
print("Processing time:", weighted_time, "seconds")

if weighted_path:
    print("A* cost:", len(weighted_path) - 1)
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
    print("Turn cost:", len(multi_path) - 1)
else:
    print("No solution found.")

if multi_path:
    bfs_agent_costs = calculate_agent_costs(multi_path)

    print("Movement cost per agent:")
    for agent_index, cost in enumerate(bfs_agent_costs):
        print(f"Agent {agent_index}: {cost}")

    print("Total movement cost:", sum(bfs_agent_costs))

agent_paths = [
        [
            state[0][agent_index]
            for state in multi_path
        ]
        for agent_index in range(len(multi_path[0][0]))
    ]
visualize(multi_world, agent_paths)

# Run DFS on the multi-agent Grid World
multi_dfs_path, multi_dfs_expanded, multi_dfs_frontier, multi_dfs_time = dfs(multi_world)

print("\nMulti-agent DFS")
print("Solution:", multi_dfs_path)
print("Expanded nodes:", multi_dfs_expanded)
print("Frontier nodes:", multi_dfs_frontier)
print("Processing time:", multi_dfs_time, "seconds")

if multi_dfs_path:
    print("Turn cost:", len(multi_dfs_path) - 1)

    dfs_agent_costs = calculate_agent_costs(multi_dfs_path)

    print("Movement cost per agent:")
    for agent_index, cost in enumerate(dfs_agent_costs):
        print(f"Agent {agent_index}: {cost}")

    print("Total movement cost:", sum(dfs_agent_costs))
else:
    print("No solution found.")

agent_paths = [
        [
            state[0][agent_index]
            for state in multi_path
        ]
        for agent_index in range(len(multi_path[0][0]))
    ]
visualize(multi_world, agent_paths)

report_multi_agent("Multi-agent BFS", bfs(multi_world))
report_multi_agent("Multi-agent DFS", dfs(multi_world))
report_multi_agent("Multi-agent Greedy (Manhattan)", greedy(multi_world, manhattan_distance))
report_multi_agent("Multi-agent A* (Manhattan)", astar(multi_world, manhattan_distance))
report_multi_agent("Multi-agent A* (Euclidean)", astar(multi_world, euclidean_distance))
report_multi_agent("Multi-agent A* (weighted Manhattan)", astar(multi_world, weighted_manhattan))

