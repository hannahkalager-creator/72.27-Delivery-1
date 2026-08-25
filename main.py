from grid_world import GridWorld
from boards import (
    simple_multi_board,
    simple_multi_configs
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
    """This function generates a report for the multi-agent pathfinding results.
    It takes the search method name and the result of the search algorithm as input."""
    path, _, _, _ = result
    agent_paths = [[state[0][agent_index] for state in path] for agent_index in range(len(path[0][0]))]
    visualize(search_method, multi_world, agent_paths)


config = simple_multi_configs[2]
multi_world = GridWorld(
    simple_multi_board,
    config["start"],
    config["goal"]
)

report_multi_agent("BFS", bfs(multi_world))
report_multi_agent("DFS", dfs(multi_world))
report_multi_agent("Greedy (Manhattan)", greedy(multi_world, manhattan_distance))
report_multi_agent("A* (Manhattan)", astar(multi_world, manhattan_distance))
report_multi_agent("A* (Euclidean)", astar(multi_world, euclidean_distance))
report_multi_agent("A* (weighted Manhattan)", astar(multi_world, weighted_manhattan))
