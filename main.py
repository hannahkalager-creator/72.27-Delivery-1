from grid_world import GridWorld
from boards import (
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
from cost import calculate_agent_costs
from game_visual import visualize


def report_multi_agent(search_method, result):
    path, expanded_nodes, frontier_nodes, processing_time = result

    print(f"\n{search_method}")
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
    
    agent_paths = [[state[0][agent_index] for state in path] for agent_index in range(len(path[0][0]))]
    
    visualize(search_method, multi_world, agent_paths)

multi_world = GridWorld(
    multi_board,
    multi_start,
    multi_goal
)

report_multi_agent("BFS", bfs(multi_world))
report_multi_agent("DFS", dfs(multi_world))
report_multi_agent("Greedy (Manhattan)", greedy(multi_world, manhattan_distance))
report_multi_agent("A* (Manhattan)", astar(multi_world, manhattan_distance))
report_multi_agent("A* (Euclidean)", astar(multi_world, euclidean_distance))
report_multi_agent("A* (weighted Manhattan)", astar(multi_world, weighted_manhattan))
