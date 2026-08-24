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
# ── MULTI-AGENT BOARDS ─────────────────────────────────────────

simple_multi_board = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
simple_multi_configs = {
    2: {"start": (((0,0),(0,4)), 0),                    "goal": ((4,4),(4,0))},
    3: {"start": (((0,0),(0,4),(4,0)), 0),              "goal": ((4,4),(4,2),(2,4))},
    4: {"start": (((0,0),(0,4),(4,0),(4,4)), 0),        "goal": ((4,2),(4,1),(2,4),(0,2))},
}

moderate_multi_board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
moderate_multi_configs = {
    2: {"start": (((0,0),(0,6)), 0),                         "goal": ((6,6),(6,0))},
    3: {"start": (((0,0),(0,6),(6,0)), 0),                   "goal": ((6,6),(6,4),(4,6))},
    4: {"start": (((0,0),(0,6),(6,0),(6,6)), 0),             "goal": ((6,4),(6,2),(0,4),(0,2))},
   
}

hard_multi_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
hard_multi_configs = {
    2: {"start": (((0,0),(0,8)), 0),                          "goal": ((8,8),(8,0))},
    3: {"start": (((0,0),(0,8),(8,0)), 0),                    "goal": ((8,8),(8,4),(4,8))},
    4: {"start": (((0,0),(0,8),(8,0),(8,8)), 0),              "goal": ((8,4),(8,6),(0,2),(0,6))},
    
}