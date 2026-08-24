import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_world import GridWorld
from search import bfs, dfs, astar, greedy
from heuristics import manhattan_distance, euclidean_distance, weighted_manhattan
from boards import multi_board, multi_start, multi_goal



class TestSearch(unittest.TestCase):
# =============================================================================
# MULTI-AGENT TESTS
# =============================================================================

    def multi_world(self):
        return GridWorld(multi_board, multi_start, multi_goal)

    # heuristic_cost should add up each agent's own distance to its own goal.
    # Agent 0 goes (0,0)->(4,4) = 8 and agent 1 goes (4,0)->(0,4) = 8.
    def test_multi_heuristic_cost_sums_per_agent(self):
        world = self.multi_world()
        h = world.heuristic_cost(world.initial_state, manhattan_distance)
        self.assertEqual(h, 16)

    # BFS is optimal for turn cost, so A* must match it. This is what shows
    # the summed heuristic is admissible in practice.
    def test_multi_astar_matches_bfs_cost(self):
        world = self.multi_world()
        bfs_path, _, _, _ = bfs(world)

        for heuristic in (manhattan_distance, euclidean_distance):
            astar_path, _, _, _ = astar(world, heuristic)
            self.assertEqual(len(astar_path) - 1, len(bfs_path) - 1)

    # The heuristic must never overestimate the true turn cost
    def test_multi_heuristics_admissible(self):
        world = self.multi_world()
        bfs_path, _, _, _ = bfs(world)
        actual_cost = len(bfs_path) - 1

        for heuristic in (manhattan_distance, euclidean_distance):
            h = world.heuristic_cost(world.initial_state, heuristic)
            self.assertLessEqual(h, actual_cost)

    # Greedy has to reach the goal, though it is not guaranteed to be optimal
    def test_multi_greedy_finds_solution(self):
        world = self.multi_world()
        path, _, _, _ = greedy(world, manhattan_distance)

        self.assertIsNotNone(path)
        self.assertTrue(world.is_goal(path[-1]))

    # Non-admissible weighted Manhattan should not expand more than Manhattan
    def test_multi_weighted_fewer_expansions(self):
        world = self.multi_world()
        _, exp_manhattan, _, _ = astar(world, manhattan_distance)
        _, exp_weighted, _, _ = astar(world, weighted_manhattan)

        self.assertLessEqual(exp_weighted, exp_manhattan)

    # An agent that is not on its goal and has no free neighbour cannot even
    # pass the turn, so the state is a dead end and there is no solution.
    # Here agent 0 sits at (0,0) in a one-wide corridor, blocked by agent 1.
    def test_multi_no_solution_when_boxed_in(self):
        corridor = [[0, 0, 0, 0]]
        world = GridWorld(
            corridor,
            ((0, 0), (0, 1)),
            ((0, 3), (0, 2))
        )

        self.assertEqual(world.get_neighbors(world.initial_state), [])

        for path, _, _, _ in (
            bfs(world),
            dfs(world),
            greedy(world, manhattan_distance),
            astar(world, manhattan_distance)
        ):
            self.assertIsNone(path)


if __name__ == "__main__":
    unittest.main()