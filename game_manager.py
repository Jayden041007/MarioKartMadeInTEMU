import pygame
from players import Player
from track.track import Track

class GameManager:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("2D Racing Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.track = Track(self.screen_width, self.screen_height)
        self.players = [
            Player("Player 1", (50, 300), (0, 0, 255), "wasd", self.screen_width, self.screen_height),
            Player("Player 2", (80, 300), (255, 0, 0), "arrows", self.screen_width, self.screen_height,)
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
            player.update(self.track)

    def render(self):
        self.screen.fill((0, 0, 0))  
        self.track.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)
        pygame.display.flip()