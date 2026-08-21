import unittest

from grid_world import GridWorld
from search import bfs, dfs



class TestSearch(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()