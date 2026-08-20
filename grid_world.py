#The GridWorld class represents the game board. 
# grid contains the layout of the board, start is where the agent starts, 
# and goal is where the agent is supposed to end up.

class GridWorld:
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

    def get_neighbors(self, state):
        #gets the current row and state of the agent
        row, col = state

        #the four possible movements, up, down, left, right
        directions = [
            (-1,0), #up
            (1,0), #down
            (0,-1), #left
            (0,1) #right
        ]

        neighbors = []

        for row_change, col_change in directions:
            new_row = row + row_change
            new_column = col + col_change

            if self.is_valid_position(new_row, new_column):
                neighbors.append((new_row, new_column))

        return neighbors


