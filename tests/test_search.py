import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_world import GridWorld, GridWorld
from search import bfs, dfs, astar, greedy
from heuristics import manhattan_distance, euclidean_distance, weighted_manhattan
from boards import test_board, test_start, test_goal
from boards import multi_board, multi_start, multi_goal



class TestSearch(unittest.TestCase):
# =============================================================================
# BFS TESTS
# =============================================================================

    def test_bfs_start_is_goal(self):
        grid = [
            [0, 0],
            [0, 0]
        ]

        # Start and goal are the same position
        world = GridWorld(grid, (0, 0), (0, 0))

        path, expanded_nodes, frontier_nodes, processing_time = bfs(world)

        # Since start and goal are the same, no movement is needed
        self.assertEqual(path, [(0, 0)])
        self.assertEqual(expanded_nodes, 1)
        self.assertEqual(frontier_nodes, 0)
        self.assertEqual(len(path) - 1, 0)

    #testing when there is no solution/ not possible to reach the goal
    def test_bfs_no_solution(self):
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]

        world = GridWorld(grid, (0, 0), (0, 2))

        path, expanded_nodes, frontier_nodes, processing_time = bfs(world)

        # assertIsNone checks that no path was found.
        # Since there is no possible path to the goal, the test should pass.
        self.assertIsNone(path) 
# =============================================================================
# DFS TESTS
# =============================================================================

    def test_dfs_start_is_goal(self):
        grid = [
            [0, 0],
            [0, 0]
        ]

        # Start and goal are the same position
        world = GridWorld(grid, (0, 0), (0, 0))

        path, expanded_nodes, frontier_nodes, processing_time = dfs(world)

        # DFS should immediately recognize that it is already at the goal
        self.assertEqual(path, [(0, 0)])
        self.assertEqual(expanded_nodes, 1)
        self.assertEqual(frontier_nodes, 0)
        self.assertEqual(len(path) - 1, 0)

    def test_dfs_no_solution(self):
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]

        world = GridWorld(grid, (0, 0), (0, 2))

        path, expanded_nodes, frontier_nodes, processing_time = dfs(world)

        # Checks that DFS returns no path when the goal cannot be reached.
        self.assertIsNone(path)
# =============================================================================
# Astar TESTS
# =============================================================================
    #Testing if A* correctly identifies when the start is the same as the goal
    def test_astar_start_is_goal(self):
        grid = [[0, 0], [0, 0]]
        world = GridWorld(grid, (0, 0), (0, 0))
        path, _, _, _ = astar(world, manhattan_distance)
        self.assertEqual(path, [(0, 0)])
    
    #Testing if A* finds the optimal path in a simple grid with one obstacle
    #BFS is guaranteed to find the optimal path in an unweighted grid, so we can compare the lengths of the paths found by A* and BFS
    def test_astar_optimal_path(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        world = GridWorld(grid, (0, 0), (2, 2))
        
        astar_path1, _, _, _ = astar(world, manhattan_distance)
        astar_path2, _, _, _ = astar(world, euclidean_distance)
        bfs_path, _, _, _ = bfs(world)
        
        # A* should find same cost as BFS (both optimal)
        self.assertEqual(len(astar_path1) - 1, len(bfs_path) - 1)
        self.assertEqual(len(astar_path2) - 1, len(bfs_path) - 1)

    #Testing if A* correctly identifies when there is no solution in a grid where the goal is unreachable
    def test_astar_no_solution(self):
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        world = GridWorld(grid, (0, 0), (0, 2))
        path1, _, _, _ = astar(world, manhattan_distance)
        path2, _, _, _ = astar(world, euclidean_distance)
        path3, _, _, _ = astar(world, weighted_manhattan)
        self.assertIsNone(path1)
        self.assertIsNone(path2)
        self.assertIsNone(path3)
# =============================================================================
# HEURISTIC TESTS
# =============================================================================
    
    #Testing if the Manhattan distance heuristic is admissible; it should never overestimates the true cost to reach the goal.
    #Comparing h(start) with the actual cost of the optimal path found by BFS
    def test_manhattan_admissible(self):
        world = GridWorld(test_board, test_start, test_goal)
        bfs_path, _, _, _ = bfs(world)
        actual_cost = len(bfs_path) - 1
        h = manhattan_distance(test_start, test_goal)
        self.assertLessEqual(h, actual_cost)

    #Same check but fot the Euclidean distance heuristic
    def test_euclidean_admissible(self):
        world = GridWorld(test_board, test_start, test_goal)
        bfs_path, _, _, _ = bfs(world)
        actual_cost = len(bfs_path) - 1
        h = euclidean_distance(test_start, test_goal)
        self.assertLessEqual(h, actual_cost)

    #Testing if the Manhattan distance heuristic dominates the Euclidean distance heuristic
    def test_manhattan_dominates_euclidean(self):
        h_manhattan = manhattan_distance(test_start, test_goal)
        h_euclidean = euclidean_distance(test_start, test_goal)
        # The Manhattan distance should always be greater than or equal to the Euclidean distance.
        self.assertGreaterEqual(h_manhattan, h_euclidean)

    # Weighted Manhattan is non-admissible: may find suboptimal solutions
    # but typically expands fewer nodes than admissible heuristics
    def test_weighted_manhattan_fewer_expansions(self):
        world = GridWorld(test_board, test_start, test_goal)
        _, exp_manhattan, _, _ = astar(world, manhattan_distance)
        _, exp_weighted, _, _ = astar(world, weighted_manhattan)

        self.assertLessEqual(exp_weighted, exp_manhattan)
        

# =============================================================================
# MULTI-AGENT TESTS
# =============================================================================

    def multi_world(self):
        return GridWorld(multi_board, multi_start, multi_goal)

    # heuristic_cost should add up each agent's own distance to its own goal.
    # Agent 0 goes (0,0)->(4,4) = 8 and agent 1 goes (4,0)->(0,4) = 8.
    def test_multi_heuristic_cost_sums_per_agent(self):
        world = self.multi_world()
        h = world.heuristic_cost(world.start, manhattan_distance)
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
            h = world.heuristic_cost(world.start, heuristic)
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
            (((0, 0), (0, 1)), 0),
            ((0, 3), (0, 2))
        )

        self.assertEqual(world.get_neighbors(world.start), [])

        for path, _, _, _ in (
            bfs(world),
            dfs(world),
            greedy(world, manhattan_distance),
            astar(world, manhattan_distance)
        ):
            self.assertIsNone(path)


if __name__ == "__main__":
    unittest.main()