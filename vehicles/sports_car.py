import pygame
from vehicles.vehicle_base import Vehicle

class SportsCar(Vehicle):
    def __init__(self, position, color):
        super().__init__(position, color)
        self.speed_boost = 1.5  
        self.slow_factor = 0.25  

    def move(self, keys, up, down, left, right, track):
        vehicle_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if track.slow_zone.colliderect(vehicle_rect):
            speed = int(self.default_speed * self.slow_factor)  
        else:
            speed = int(self.default_speed * self.speed_boost) 

        if keys[up]:
            self.y -= speed
        if keys[down]:
            self.y += speed
        if keys[left]:
            self.x -= speed
        if keys[right]:
            self.x += speed
