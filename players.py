# player.py - Handles player input and movement
import pygame
from vehicles.vehicle_base import Vehicle

class Player:
    def __init__(self, name, position, color, control_scheme):
        self.name = name
        self.vehicle = Vehicle(position, color)
        self.control_scheme = control_scheme

    def update(self):
        keys = pygame.key.get_pressed()
        if self.control_scheme == "wasd":
            self.vehicle.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        else:
            self.vehicle.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    def draw(self, screen):
        self.vehicle.draw(screen)
