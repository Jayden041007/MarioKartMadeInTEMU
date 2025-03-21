import pygame

class Vehicle:
    def __init__(self, position, color):
        self.x, self.y = position
        self.default_speed = 12
        self.speed = self.default_speed
        self.color = color
        self.width, self.height = 20, 40

    def move(self, keys, up, down, left, right,track):

        vehicle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if track.slow_zone.colliderect(vehicle_rect):
            self.speed = self.default_speed // 2  
        else:
            self.speed = self.default_speed

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