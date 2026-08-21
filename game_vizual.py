import pygame


def visualize(world, path):
    pygame.init()
    
    CELL_SIZE = 80
    rows = len(world.grid)
    cols = len(world.grid[0])
    
    screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
    pygame.display.set_caption("Grid World")
    
    # Farger
    WHITE  = (255, 255, 255)  # fri celle
    BLACK  = (0, 0, 0)        # vegg
    GREEN  = (0, 200, 0)      # mål
    BLUE   = (0, 0, 255)      # agent/vei
    RED    = (255, 0, 0)      # start
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Tegn grid
        for row in range(rows):
            for col in range(cols):
                color = BLACK if world.grid[row][col] == 1 else WHITE
                pygame.draw.rect(screen, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, (200,200,200), (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
        
        # Tegn vei
        for state in path:
            row, col = state
            pygame.draw.rect(screen, BLUE, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Tegn start og mål
        pygame.draw.rect(screen, RED,   (world.start[1]*CELL_SIZE, world.start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GREEN, (world.goal[1]*CELL_SIZE,  world.goal[0]*CELL_SIZE,  CELL_SIZE, CELL_SIZE))
        
        pygame.display.flip()
    
    pygame.quit()