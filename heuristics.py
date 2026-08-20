# Estimates the distance from the current state to the goal
# using only horizontal and vertical movements.

def manhattan_distance(state, goal):
    row_difference = abs(state[0] - goal[0])
    column_difference = abs(state[1] - goal[1])

    return row_difference + column_difference
