import pygame

class Track:
    def __init__(self):
        self.track_surface = pygame.Surface((1000, 800))
        self.track_surface.fill((223, 195, 122))
        pygame.draw.rect(self.track_surface, (0, 103, 22), (100, 100, 750, 400), 12)

    def draw(self, screen):
        screen.blit(self.track_surface, (0, 0))
