import pygame
from vehicles.vehicle_base import Vehicle

class Sports_Car(Vehicle):
    def __init__(self,position, color):
        super().__init__(position,color)
        self.slow_factor = 0.25
        self.default_speed = 24  # Faster than a normal vehicle
        self.speed = self.default_speed


    def move(self, keys, up, down, left, right, track):
        vehicle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if track.slow_zone.colliderect(vehicle_rect):
            self.speed = int(self.default_speed * self.slow_factor)
        else:
            self.speed = self.default_speed

        super().move(keys, up, down,left,right)