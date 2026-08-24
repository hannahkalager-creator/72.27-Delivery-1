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
    )
)

multi_goal = (
    (4, 4),
    (0, 4)
)