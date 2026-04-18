import pygame

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (size, size))

    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
            if maze[new_y][new_x] == 0:
                self.x = new_x
                self.y = new_y

    def draw(self, screen):
        screen.blit(self.image, (self.x*self.size, self.y*self.size))
