import pygame
import os
import sys
from maze import levels
from player import Player

pygame.init()

# ====== FIX LOAD FILE KHI BUILD EXE ======
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ====== CẤU HÌNH ======
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 30  # phù hợp map 20x20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# ====== LOAD ẢNH ======
goal_img = pygame.image.load(resource_path("assets/fractionai.png"))
goal_img = pygame.transform.scale(goal_img, (TILE_SIZE, TILE_SIZE))

# ====== LEVEL SYSTEM ======
current_level = 0
maze = levels[current_level]
goal = (len(maze[0]) - 1, len(maze) - 1)

player = Player(0, 0, TILE_SIZE)

# ====== GAME LOOP ======
running = True
while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1

    # reset game
    if keys[pygame.K_r]:
        current_level = 0
        maze = levels[current_level]
        player.x, player.y = 0, 0
        goal = (len(maze[0]) - 1, len(maze) - 1)

    player.move(dx, dy, maze)

    screen.fill((0, 0, 0))

    # ====== VẼ MAZE ======
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # ====== VẼ ĐÍCH (ẢNH) ======
    screen.blit(goal_img, (goal[0]*TILE_SIZE, goal[1]*TILE_SIZE))

    # ====== VẼ PLAYER ======
    player.draw(screen)

    # ====== HIỂN THỊ LEVEL ======
    text = font.render(f"Level: {current_level+1}", True, (255, 255, 0))
    screen.blit(text, (10, 10))

    # ====== KIỂM TRA WIN ======
    if (player.x, player.y) == goal:
        current_level += 1

        if current_level < len(levels):
            maze = levels[current_level]
            player.x, player.y = 0, 0
            goal = (len(maze[0]) - 1, len(maze) - 1)
            print("LEVEL UP!")
        else:
            print("YOU WIN ALL LEVELS!")
            running = False

    pygame.display.flip()

pygame.quit()
