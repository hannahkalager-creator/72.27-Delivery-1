import math

# Estimates the distance from the current state to the goal
# using only horizontal and vertical movements.
def manhattan_distance(state, goal):
    row_difference = abs(state[0] - goal[0])
    column_difference = abs(state[1] - goal[1])
    return row_difference + column_difference

# Estimates the straight-line distance from the current state to the goal.
# Always admissible since the straight-line distance never exceeds the actual path cost.
def euclidean_distance(state, goal):
    return math.sqrt((state[0] - goal[0])**2 + (state[1] - goal[1])**2)

# Non-admissible: can overestimate, but may find solutions faster
def weighted_manhattan(state, goal):
    return 2 * (abs(state[0] - goal[0]) + abs(state[1] - goal[1]))