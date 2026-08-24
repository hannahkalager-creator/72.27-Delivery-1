# The GridWorld class represents the game board. 
# grid contains the layout of the board, start is where the agent starts, 
# and goal is where the agent is supposed to end up.

directions = [
    (-1,0), #up
    (1,0), #down
    (0,-1), #left
    (0,1) #right
]

class GridWorld():
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.current_agent = 0
        self.initial_state = (start, self.current_agent)
        
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
                    
    # Checks if all agents have reached their assigned goals
    def is_goal(self, state):
        positions, _ = state
        return positions == self.goal

    # Sums each agent's estimated distance to its own goal. A turn moves one agent one
    # cell, so the sum drops by at most 1 per turn and never overestimates.
    def heuristic_cost(self, state, heuristic):
        positions, _ = state
        return sum(
            heuristic(position, goal)
            for position, goal in zip(positions, self.goal)
        )

    def get_neighbors(self, state):
        positions, current_agent = state
        neighbors = []

        row, col = positions[current_agent]

        # If the current agent has already reached its goal,
        # it can stay in place and pass the turn to the next agent.
        if positions[current_agent] == self.goal[current_agent]:
            next_agent = (current_agent + 1) % len(positions)

            wait_state = (
                positions,
                next_agent
            )

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

                        new_state = (
                            tuple(new_positions),
                            next_agent
                        )

                        neighbors.append(new_state)

        return neighbors

    def is_valid_position(self, row, col):
            # Checks if a position is valid on the board
            rows = len(self.grid)
            # Gets the number of rows in the grid
            cols = len(self.grid[0])
            # Gets the number of columns in the grid
    
            if row < 0 or row >= rows:
                return False
            # Returns False if the row is outside the grid
    
            if col < 0 or col >= cols:
                return False
            # Returns False if the column is outside the grid
    
            if self.grid[row][col] == 1:
                return False
            # Returns False if the position is a wall/block
    
        # Otherwise, the agent can move to this position
            return True