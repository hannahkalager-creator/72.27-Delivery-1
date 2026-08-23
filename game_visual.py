import pygame
from grid_world import GridWorld
import time

CELL_SIZE = 80

colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # magenta
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (255, 192, 203) # Pink
]


def draw_grid(screen, world, rows, cols):
    WHITE  = (255, 255, 255)
    BLACK  = (0, 0, 0)
    
    for row in range(rows):
        for col in range(cols):
            color = BLACK if world.grid[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (200,200,200), (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def draw_start_and_goal(screen, paths, agent_colors):
    for agent_index, path in enumerate(paths):
        start_row, start_col = path[0]
        goal_row, goal_col = path[-1]
        pygame.draw.rect(screen, agent_colors[agent_index], (start_col*CELL_SIZE + 10, start_row*CELL_SIZE + 10, CELL_SIZE - 20, CELL_SIZE - 20))
        pygame.draw.rect(screen, agent_colors[agent_index], (goal_col*CELL_SIZE + 10, goal_row*CELL_SIZE + 10, CELL_SIZE - 20, CELL_SIZE - 20))


def draw_transparent_path(screen, transparent_layer, paths, agent_colors):
    clock = pygame.time.Clock()
    max_steps = max(len(path) for path in paths)
        
    for step in range(max_steps):
        transparent_layer.fill((0, 0, 0, 0))
        for agent_index, path in enumerate(paths):
            red, green, blue = agent_colors[agent_index]
            transparent_path_color = (red, green, blue, 80)
            if step < len(path):
                row, col = path[step]
                if step > 0 and path[step] == path[step - 1]:
                    continue
                pygame.draw.rect(transparent_layer, transparent_path_color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        screen.blit(transparent_layer, (0, 0))
        pygame.display.flip()
        clock.tick(5)

"""
# Constructing the multipath for multiagents
agent_paths = [
        [
            state[0][agent_index]
            for state in multi_path
        ]
        for agent_index in range(len(multi_path[0][0]))
    ]
    visualize(multi_world, agent_paths)
"""

def visualize(world, paths):
    rows = len(world.grid)
    cols = len(world.grid[0])
    
    pygame.init()
    pygame.display.set_caption("Grid World")
    screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
    transparent_layer = pygame.Surface((cols * CELL_SIZE, rows * CELL_SIZE), pygame.SRCALPHA)
    
    agent_colors = colors[:len(paths)]
    draw_grid(screen, world, rows, cols)
    draw_start_and_goal(screen, paths, agent_colors)
    draw_transparent_path(screen, transparent_layer, paths, agent_colors)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()