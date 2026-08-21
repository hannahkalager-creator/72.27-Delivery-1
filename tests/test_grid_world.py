import unittest
from grid_world import GridWorld

#test 1: checks that get_neighbors returns
# the correct possible moves from the start
class TestGridWorld(unittest.TestCase):
    def test_neighbors_from_start(self):
        grid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]

        world = GridWorld(grid, (0,0), (2,2)) #makes a GridWorld with start (0,0) and goal (2,2)
        neigbors = world.get_neighbors((0,0)) 
        self.assertEqual(neigbors, [(1,0), (0,1)]) #makes sure that get_neighbors gives the same as we have written


    ## Test 2: checks that the agent cannot move into a wall
    def test_cannot_move_into_wall(self):
        grid = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        world = GridWorld(grid, (0, 0), (2, 2))

        neighbors = world.get_neighbors((0, 0))

        self.assertEqual(neighbors, [(1, 0)])


    #Test 3: checks that the agent can not go outside of grid
    def test_cannot_move_outside_grid(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        world = GridWorld(grid, (0, 0), (2, 2))

        # Positions outside the grid should not be valid
        self.assertFalse(world.is_valid_position(-1, 0))
        self.assertFalse(world.is_valid_position(0, -1))
        self.assertFalse(world.is_valid_position(3, 0))
        self.assertFalse(world.is_valid_position(0, 3))

if __name__ =="__main__":
    unittest.main()