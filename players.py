# player.py - Handles player input and movement
import pygame
from vehicles.vehicle_base import Vehicle

class Player:
    def __init__(self, name, position, color, control_scheme, screen_width, screen_height):
        self.name = name
        self.vehicle = Vehicle(position, color)
        self.control_scheme = control_scheme
        self.screen_width = screen_width 
        self.screen_height = screen_height

    def update(self, track):
        keys = pygame.key.get_pressed()
        if self.control_scheme == "wasd":
            self.vehicle.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, track)
        else:
            self.vehicle.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, track)
        
        #Screen Boundaries
        if self.vehicle.x < 0:
            self.vehicle.x = 0
        elif self.vehicle.x > self.screen_width - self.vehicle.width:
            self.vehicle.x = self.screen_width - self.vehicle.width

        if self.vehicle.y < 0:
            self.vehicle.y = 0
        elif self.vehicle.y > self.screen_height - self.vehicle.height:
            self.vehicle.y = self.screen_height - self.vehicle.height


    def draw(self, screen):
        self.vehicle.draw(screen)