import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_world import GridWorld
from search import bfs, dfs, astar, greedy
from heuristics import manhattan_distance, euclidean_distance, weighted_manhattan
from boards import test_board, test_start, test_goal



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
        


if __name__ == "__main__":
    unittest.main()