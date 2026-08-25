import argparse

from grid_world import GridWorld
from boards import (
    simple_multi_board,
    simple_multi_configs,
    moderate_multi_board,
    moderate_multi_configs,
    hard_multi_board,
    hard_multi_configs
)
from search import bfs, dfs, greedy, astar
from heuristics import (
    manhattan_distance,
    euclidean_distance,
    weighted_manhattan
)
from cost import calculate_agent_costs
from game_visual import visualize


BOARDS = {
    "simple": (simple_multi_board, simple_multi_configs),
    "moderate": (moderate_multi_board, moderate_multi_configs),
    "hard": (hard_multi_board, hard_multi_configs),
}


def run_multi_agent(search_method, result, world):
    """This function generates a report for the multi-agent pathfinding results.
    It takes the search method name and the result of the search algorithm as input."""
    path, _, _, _ = result
    agent_paths = [[state[0][agent_index] for state in path] for agent_index in range(len(path[0][0]))]
    visualize(search_method, world, agent_paths)


def parse_args():
    parser = argparse.ArgumentParser(description="Run multi-agent grid-world searches.")
    parser.add_argument(
        "--agents",
        type=int,
        choices=(2, 3, 4),
        default=4,
        help="number of agents (default: 4)",
    )
    parser.add_argument(
        "--difficulty",
        choices=tuple(BOARDS),
        default="simple",
        help="board difficulty (default: simple), simple, moderate, hard",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    board, configs = BOARDS[args.difficulty]
    config = configs[args.agents]
    world = GridWorld(board, config["start"], config["goal"])

    run_multi_agent("BFS", bfs(world), world)
    run_multi_agent("DFS", dfs(world), world)
    run_multi_agent("Greedy (Manhattan)", greedy(world, manhattan_distance), world)
    run_multi_agent("A* (Manhattan)", astar(world, manhattan_distance), world)
    run_multi_agent("A* (Euclidean)", astar(world, euclidean_distance), world)
    run_multi_agent("A* (weighted Manhattan)", astar(world, weighted_manhattan), world)


if __name__ == "__main__":
    main()
