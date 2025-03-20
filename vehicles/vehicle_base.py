import pygame

class Vehicle:
    def __init__(self, position, color):
        self.x, self.y = position
        self.speed = 12
        self.color = color
        self.width, self.height = 20, 40

    def move(self, keys, up, down, left, right):
        if keys[up]:
            self.y -= self.speed
        if keys[down]:
            self.y += self.speed
        if keys[left]:
            self.x -= self.speed
        if keys[right]:
            self.x += self.speed
        

        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))



