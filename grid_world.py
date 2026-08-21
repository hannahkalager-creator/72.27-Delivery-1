#The GridWorld class represents the game board. 
# grid contains the layout of the board, start is where the agent starts, 
# and goal is where the agent is supposed to end up.

# Initial single-agent implementation of Grid World.
# The implementation will later be extended to support multiple agents.

class GridWorld:

                    #the four possible movements, up, down, left, right
    directions = [
        (-1,0), #up
        (1,0), #down
        (0,-1), #left
        (0,1) #right
    ]

    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal




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

    # Checks if the current state is the goal
    def is_goal(self, state):
        return state == self.goal

    
    def get_neighbors(self, state):
        #gets the current row and state of the agent
        row, col = state


        neighbors = []

        for row_change, col_change in self.directions:
            new_row = row + row_change
            new_column = col + col_change

            if self.is_valid_position(new_row, new_column):
                neighbors.append((new_row, new_column))

        return neighbors


class MultiAgentGridWorld(GridWorld):
    def __init__(self, grid, start, goal):
        super().__init__(grid, start, goal) #inherits from GridWorld

        # Each agent must have one goal
        if len(start) != len(goal):
            raise ValueError("Each agent must have one goal.")

        # Two agents cannot start in the same position
        if len(set(start)) != len(start):
            raise ValueError("Two agents cannot start in the same position.")

        # Count how many free cells there are in the grid
        free_cells = sum(
            cell == 0
            for row in grid
            for cell in row
        )

        if len(start) > free_cells:
            raise ValueError("There are more agents than free cells.")

        # Check that all start positions are valid
        for position in start:
            row, col = position

            if not self.is_valid_position(row, col):
                raise ValueError("All start positions must be valid.")


        if len(set(goal)) != len(goal):
            raise ValueError("Two agents cannot have the same goal.")

        
        # Check that all goal positions are valid
        for position in goal:
            row, col = position

            if not self.is_valid_position(row, col):
                raise ValueError("All goal positions must be valid.")
                    
    # Checks if all agents have reached their assigned goals
    def is_goal(self, state):
        positions, current_agent = state
        return positions == self.goal


    def get_neighbors(self, state):
        positions, current_agent = state
        neighbors = []

        row, col = positions[current_agent]

        for row_change, col_change in self.directions:
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