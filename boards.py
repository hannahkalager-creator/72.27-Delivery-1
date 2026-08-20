# Simple Grid World with one agent and one goal.
# This is the initial version used to test the search algorithms
# before extending the implementation to multiple agents.
# Simple Grid World with one agent and one goal.
simple_board = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

simple_start = (0, 0)
simple_goal = (3, 3)


# More complex board for comparing search algorithms.
test_board = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0]
]

test_start = (0, 0)
test_goal = (5, 5)