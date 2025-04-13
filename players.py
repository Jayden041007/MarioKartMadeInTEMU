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
        self.lap_count = 0  # Initialize lap count
        self.crossed_finish_line = False  # Track if the player has crossed the finish line

    def select_car(self, direction):
        if direction == -1 and self.selected_car_index > 0:
            self.selected_car_index -= 1
        elif direction == 1 and self.selected_car_index < len(self.car_classes) - 1:
            self.selected_car_index += 1

    def update(self, track):
        if self.vehicle:
            keys = pygame.key.get_pressed()

            # Determine controls based on control scheme
            if self.control_scheme == "wasd":
                up, down, left, right = pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
            elif self.control_scheme == "arrows":
                up, down, left, right = pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT
            else:
                return  # Invalid control scheme

            self.vehicle.move(keys, up, down, left, right, track)
            self.check_finish_line(track)  # Check if the player crosses the finish line

            # Screen Boundaries
            if self.vehicle.x < 0:
                self.vehicle.x = 0
            elif self.vehicle.x > self.screen_width - self.vehicle.width:
                self.vehicle.x = self.screen_width - self.vehicle.width

            if self.vehicle.y < 0:
                self.vehicle.y = 0
            elif self.vehicle.y > self.screen_height - self.vehicle.height:
                self.vehicle.y = self.screen_height - self.vehicle.height

    def check_finish_line(self, track):
        finish_line_y = 280  # Y-coordinate of the finish line
        if self.vehicle.y < finish_line_y and not self.crossed_finish_line:
            self.lap_count += 1  # Increment lap count
            self.crossed_finish_line = True  # Mark that the finish line has been crossed
        elif self.vehicle.y >= finish_line_y:
            self.crossed_finish_line = False  # Reset the flag when the vehicle is below the finish line

    def draw(self, screen):
        if self.vehicle:
            self.vehicle.draw(screen)