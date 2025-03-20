import pygame

class Track:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.track_surface = pygame.Surface((self.screen_width, self.screen_height))
        self.track_surface.fill((223, 195, 122))  # Background color

        track_width = int(self.screen_width * 0.8)  # 80% of screen width
        track_height = int(self.screen_height * 0.6)  # 60% of screen height

        center_x = (self.screen_width - track_width) // 2
        center_y = (self.screen_height - track_height) // 2

        pygame.draw.rect(self.track_surface, (0, 103, 22), (center_x, center_y, track_width, track_height), 12)

    def draw(self, screen):
        screen.blit(self.track_surface, (0, 0))
