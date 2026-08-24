directions = [
    (-1,0), #up
    (1,0), #down
    (0,-1), #left
    (0,1) #right
]

class GridWorld():
    """This class represents a multi-agent grid world environment. 
    It contains the grid layout, start positions, and goal positions for each agent. 
    The class provides methods to check if all agents have reached their goals, 
    calculate heuristic costs, get neighboring states, and validate positions within the grid."""
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.state = (start, 0)
        
        if len(start) != len(goal):
            raise ValueError("Each agent must have one goal.")

        if len(set(start)) != len(start):
            raise ValueError("Two agents cannot start in the same position.")

        if len(set(goal)) != len(goal):
            raise ValueError("Two agents cannot have the same goal.")
        
        for position in start:
            row, col = position
            if not self.is_valid_position(row, col):
                raise ValueError("All start positions must be valid.")
        
        for position in goal:
            row, col = position
            if not self.is_valid_position(row, col):
                raise ValueError("All goal positions must be valid.")
        
        free_cells = sum(cell == 0 for row in grid for cell in row)
        if len(start) > free_cells:
            raise ValueError("There are more agents than free cells.")
                    
    def all_agents_at_goal(self, state):
        """This function checks if all agents have reached their respective goal positions in the grid world."""
        positions, _ = state
        return positions == self.goal

    def heuristic_cost(self, state, heuristic):
        """This function calculates the heuristic cost for a given state in the grid world.
        The heuristic cost is the sum of the estimated distances from each agent's current position to its goal position.""" 
        positions, _ = state
        return sum(
            heuristic(position, goal)
            for position, goal in zip(positions, self.goal)
        )

    def get_neighbors(self, state):
        """This function generates all valid neighboring states for a given state in the grid world.
        It considers the current agent's position and checks all possible moves (up, down, left, right) to generate new states.
        If the current agent has already reached its goal, it can stay in place and pass the turn to the next agent. 
        The function returns a list of valid neighboring states."""
        positions, current_agent = state
        neighbors = []
        row, col = positions[current_agent]

        if positions[current_agent] == self.goal[current_agent]:
            next_agent = (current_agent + 1) % len(positions)
            wait_state = (positions, next_agent)
            neighbors.append(wait_state)
        else:
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                new_position = (new_row, new_col)

                if self.is_valid_position(new_row, new_col):
                    if new_position not in positions:
                        new_positions = list(positions)
                        new_positions[current_agent] = new_position
                        next_agent = (current_agent + 1) % len(positions)
                        new_state = (tuple(new_positions), next_agent)
                        neighbors.append(new_state)

        return neighbors

    def is_valid_position(self, row, col):
        """This function checks if a given position (row, col) is valid within the grid world.
        A position is considered valid if it is within the bounds of the grid and is not a wall/block (represented by 1 in the grid)."""
        rows = len(self.grid)
        cols = len(self.grid[0])

        if row < 0 or row >= rows:
            return False

        if col < 0 or col >= cols:
            return False

        if self.grid[row][col] == 1:
            return False
        
        return True