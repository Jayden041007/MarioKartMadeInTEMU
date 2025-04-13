import pygame

class Track:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.track_surface = pygame.Surface((self.screen_width, self.screen_height))
        self.track_surface.fill((223, 195, 122))  # Background color

        self.track_width = int(self.screen_width * 0.8)  # 80% of screen width
        self.track_height = int(self.screen_height * 0.6)  # 60% of screen height

        self.center_x = (self.screen_width - self.track_width) // 2
        self.center_y = (self.screen_height - self.track_height) // 2

        self.slow_zone = pygame.Rect(self.center_x, self.center_y, self.track_width, self.track_height)

        pygame.draw.rect(self.track_surface, (0, 103, 22), self.slow_zone, 12)
        pygame.draw.line(self.track_surface, (0, 0, 0), (0, 280), (self.center_x, 280), 10)  # Finish line

    def draw(self, screen):
        screen.blit(self.track_surface, (0, 0))