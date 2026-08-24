import math

def manhattan_distance(state, goal):
    """This function calculates the Manhattan distance between the current state and the goal state.
    The Manhattan distance is the sum of the absolute differences of the Cartesian coordinates."""
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def euclidean_distance(state, goal):
    """This function calculates the Euclidean distance between the current state and the goal state.
    The Euclidean distance is the straight-line distance between two points in a 2D space"""
    return math.sqrt((state[0] - goal[0])**2 + (state[1] - goal[1])**2)


def weighted_manhattan(state, goal):
    """This function calculates a weighted Manhattan distance between the current state and the goal state.
    The weighted Manhattan distance is defined as twice the sum of the absolute differences of the Cartesian coordinates."""
    return 2 * (abs(state[0] - goal[0]) + abs(state[1] - goal[1]))