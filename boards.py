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


# Multi-agent Grid World with two agents and two goals.
multi_board = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

multi_start = (
    (
        (0, 0),  # Agent 0
        (4, 0)   # Agent 1
    ),
    0            # Agent 0 starts
)

multi_goal = (
    (4, 4),
    (0, 4)
)