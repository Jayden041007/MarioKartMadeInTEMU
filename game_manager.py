import pygame
from players import Player
from track.track import Track

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
        pygame.display.set_caption("2D Racing Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.track = Track()
        self.players = [
            Player("Player 1", (50, 300), (0, 0, 255), "wasd"),
            Player("Player 2", (50, 350), (255, 0, 0), "arrows")
        ]

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self):
        for player in self.players:
            player.update()

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        self.track.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)
        pygame.display.flip()