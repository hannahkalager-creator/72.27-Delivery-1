import pygame
from grid_world import GridWorld
import time

#first draft, most likley needs to be uodated for multiagent and multitarget etc
def visualize(world, path):
    pygame.init()
    
    CELL_SIZE = 80
    rows = len(world.grid)
    cols = len(world.grid[0])
    
    screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
    pygame.display.set_caption("Grid World")

    WHITE  = (255, 255, 255)
    BLACK  = (0, 0, 0)
    GREEN  = (0, 200, 0)
    BLUE   = (0, 0, 255)
    RED    = (255, 0, 0)
    YELLOW = (255, 255, 0)  # agent sin nåværende posisjon

    for step in range(len(path)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(WHITE)

        # Tegn grid
        for row in range(rows):
            for col in range(cols):
                color = BLACK if world.grid[row][col] == 1 else WHITE
                pygame.draw.rect(screen, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, (200,200,200), (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        # Tegn veien så langt
        for state in path[:step]:
            row, col = state
            pygame.draw.rect(screen, BLUE, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Tegn start og mål
        pygame.draw.rect(screen, RED,   (world.start[1]*CELL_SIZE, world.start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GREEN, (world.goal[1]*CELL_SIZE,  world.goal[0]*CELL_SIZE,  CELL_SIZE, CELL_SIZE))

        # Tegn agentens nåværende posisjon
        row, col = path[step]
        pygame.draw.rect(screen, YELLOW, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        time.sleep(0.3)  # forsinkelse mellom hvert trekk


    # Hold vinduet åpent etter at agenten er fremme
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()