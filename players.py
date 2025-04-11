import pygame
from vehicles.vehicle_base import Vehicle
from vehicles.truck import Truck
from vehicles._4wd import FourWheelDrive
from vehicles.sports_car import SportsCar

class Player:
    def __init__(self, name, position, color, control_scheme, screen_width, screen_height):
        self.name = name
        self.position = position
        self.color = color
        self.control_scheme = control_scheme
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selected_car_index = 0  # Default to the first car
        self.car_classes = [SportsCar, Truck, FourWheelDrive]
        self.vehicle = None

    def select_car(self, direction):
        # Only change selection if it's within bounds
        if direction == -1 and self.selected_car_index > 0:
            self.selected_car_index -= 1
        elif direction == 1 and self.selected_car_index < len(self.car_classes) - 1:
            self.selected_car_index += 1

    def update(self, track):
        if self.vehicle:
            keys = pygame.key.get_pressed()
            if self.control_scheme == "wasd":
                self.vehicle.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, track)
            else:
                self.vehicle.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, track)

            # Screen Boundaries
            if self.vehicle.x < 0:
                self.vehicle.x = 0
            elif self.vehicle.x > self.screen_width - self.vehicle.width:
                self.vehicle.x = self.screen_width - self.vehicle.width

            if self.vehicle.y < 0:
                self.vehicle.y = 0
            elif self.vehicle.y > self.screen_height - self.vehicle.height:
                self.vehicle.y = self.screen_height - self.vehicle.height

    def draw(self, screen):
        if self.vehicle:
            self.vehicle.draw(screen)