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
            Player("Player 2", (80, 300), (255, 0, 0), "arrows", self.screen_width, self.screen_height)
        ]

        self.current_screen = "home"
        self.car_options = ["Sports Car", "Truck", "4WD"]
        self.start_button_rect = None
        self.controls_button_rect = None

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.current_screen == "home":
                    if self.start_button_rect.collidepoint(mouse_pos):
                        self.current_screen = "car_selection"
                    elif self.controls_button_rect.collidepoint(mouse_pos):
                        self.current_screen = "controls"

    def update(self):
        if self.current_screen == "game":
            for player in self.players:
                player.update(self.track)

    def render(self):
        self.screen.fill((0, 0, 0))
        
        if self.current_screen == "home":
            self.render_home()
        elif self.current_screen == "car_selection":
            self.render_car_selection()
        elif self.current_screen == "controls":
            self.render_controls()
        elif self.current_screen == "game":
            self.track.draw(self.screen)
            for player in self.players:
                player.draw(self.screen)

        pygame.display.flip()

    def render_home(self):
        font = pygame.font.Font(None, 74)
        title_surface = font.render("2D Racing Game", True, (255, 255, 255))
        start_surface = font.render("Start Game", True, (255, 255, 255))
        controls_surface = font.render("Controls", True, (255, 255, 255))
        
        self.start_button_rect = start_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.controls_button_rect = controls_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 100))

        self.screen.blit(title_surface, (self.screen_width // 2 - title_surface.get_width() // 2, self.screen_height // 4))
        self.screen.blit(start_surface, self.start_button_rect.topleft)
        self.screen.blit(controls_surface, self.controls_button_rect.topleft)

    def render_car_selection(self):
        font = pygame.font.Font(None, 74)
        player1_surface = font.render("Player 1: Choose your car", True, (255, 255, 255))
        player2_surface = font.render("Player 2: Choose your car", True, (255, 255, 255))

        self.screen.blit(player1_surface, (50, self.screen_height // 4))
        self.screen.blit(player2_surface, (self.screen_width // 2 + 50, self.screen_height // 4))

        for i, car in enumerate(self.car_options):
            color1 = (255, 255, 0) if self.players[0].selected_car_index == i else (255, 255, 255)
            option_surface1 = font.render(car, True, color1)
            self.screen.blit(option_surface1, (50, self.screen_height // 2 + i * 50))

            color2 = (255, 255, 0) if self.players[1].selected_car_index == i else (255, 255, 255)
            option_surface2 = font.render(car, True, color2)
            self.screen.blit(option_surface2, (self.screen_width // 2 + 50, self.screen_height // 2 + i * 50))

        # Start button
        start_button_surface = font.render("Start", True, (255, 255, 255))
        self.start_button_rect = start_button_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 200))
        self.screen.blit(start_button_surface, self.start_button_rect.topleft)

    def render_controls(self):
        font = pygame.font.Font(None, 74)
        controls_surface = font.render("Controls:", True, (255, 255, 255))
        player1_controls = font.render("Player 1 - WASD", True, (255, 255, 255))
        player2_controls = font.render("Player 2 - Arrow keys", True, (255, 255, 255))
        
        back_button_surface = font.render("Back", True, (255, 255, 255))
        back_button_rect = back_button_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 150))

        self.screen.blit(controls_surface, (self.screen_width // 2 - controls_surface.get_width() // 2, self.screen_height // 4))
        self.screen.blit(player1_controls, (self.screen_width // 2 - player1_controls.get_width() // 2, self.screen_height // 2))
        self.screen.blit(player2_controls, (self.screen_width // 2 - player2_controls.get_width() // 2, self.screen_height // 2 + 50))
        self.screen.blit(back_button_surface, back_button_rect.topleft)

        # Back button functionality
        if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
            mouse_pos = pygame.mouse.get_pos()
            if back_button_rect.collidepoint(mouse_pos):
                self.current_screen = "home"