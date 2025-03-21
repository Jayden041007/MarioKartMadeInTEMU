import pygame
from vehicles.vehicle_base import Vehicle

class _4WD(Vehicle):
    def __init__(self,position, color):
        super().__init__(position,color)
        self.slow_factor = 0.25

    def move(self, keys, up, down, left, right, track):
        vehicle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if track.slow.zone.pygame.Rect.colliderect(vehicle_rect):
            self.speed = int(self.default_speed * self.slow_factor)
        else:
            self.speed = self.default.speed

        super().move(keys, up, down,left,right)
