import pygame
import random

class Obstacles:
    def __init__(self, screen_width, screen_height, num_obstacles=5):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_obstacles = num_obstacles
        self.rocks = self.generate_rocks()

    def generate_rocks(self):
        rocks = []
        for _ in range(self.num_obstacles):
            x = random.randint(50, self.screen_width - 70)
            y = random.randint(100, self.screen_height - 100)
            rocks.append(pygame.Rect(x, y, 30, 30))
        return rocks

    def draw(self, screen):
        for rock in self.rocks:
            pygame.draw.rect(screen, (128, 128, 128), rock)

    def check_collisions(self, player):
        vehicle_rect = pygame.Rect(player.vehicle.x, player.vehicle.y, player.vehicle.width, player.vehicle.height)
        for rock in self.rocks:
            if vehicle_rect.colliderect(rock):
                self.handle_collision(player)

    def handle_collision(self, player):
        player.vehicle.x -= 10 