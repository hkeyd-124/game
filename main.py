import pygame
from maze import maze
from player import Player

pygame.init()

WIDTH, HEIGHT = 600, 600
TILE_SIZE = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

clock = pygame.time.Clock()

player = Player(0, 0, TILE_SIZE)
goal = (9, 9)

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

    player.move(dx, dy, maze)

    screen.fill((0, 0, 0))

    # vẽ maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # vẽ đích
    pygame.draw.rect(screen, (0, 255, 0),
                     (goal[0]*TILE_SIZE, goal[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    player.draw(screen)

    if (player.x, player.y) == goal:
        print("YOU WIN!")

    pygame.display.flip()

pygame.quit()
