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
        self.last_selection_change_time = 0
        self.selection_change_delay = 200  # milliseconds
        self.winner = None

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
            elif event.type == pygame.KEYDOWN:
                if self.current_screen == "win" and event.key == pygame.K_r:
                    self.reset_game()  # Reset the game

        # Handle key events for car selection
        if self.current_screen == "car_selection":
            current_time = pygame.time.get_ticks()
            if current_time - self.last_selection_change_time > self.selection_change_delay:
                keys = pygame.key.get_pressed()
                # Player 1 controls
                if keys[pygame.K_w]:
                    self.players[0].select_car(-1)
                    self.last_selection_change_time = current_time
                if keys[pygame.K_s]:
                    self.players[0].select_car(1)
                    self.last_selection_change_time = current_time
                # Player 2 controls
                if keys[pygame.K_UP]:
                    self.players[1].select_car(-1)
                    self.last_selection_change_time = current_time
                if keys[pygame.K_DOWN]:
                    self.players[1].select_car(1)
                    self.last_selection_change_time = current_time

                # Check if both players have selected their cars
                if keys[pygame.K_RETURN] and all(player.selected_car_index is not None for player in self.players):
                    self.start_game()

    def start_game(self):
        # Load selected vehicles
        for player in self.players:
            selected_car_class = player.car_classes[player.selected_car_index]
            player.vehicle = selected_car_class(player.position, player.color)
        self.current_screen = "game"

    def update(self):
        if self.current_screen == "game":
            for player in self.players:
                player.update(self.track)

            # Check for win condition
            if self.players[0].lap_count >= 3:
                self.current_screen = "win"
                self.winner = self.players[0].name
            elif self.players[1].lap_count >= 3:
                self.current_screen = "win"
                self.winner = self.players[1].name

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
            
            self.render_lap_counts()  # Render lap counts
        elif self.current_screen == "win":
            self.render_win_screen(self.winner)  # Render win screen

        pygame.display.flip()

    def render_lap_counts(self):
        font = pygame.font.Font(None, 74)
        player1_lap_surface = font.render(f"{self.players[0].name}: Laps - {self.players[0].lap_count}", True, (255, 255, 255))
        player2_lap_surface = font.render(f"{self.players[1].name}: Laps - {self.players[1].lap_count}", True, (255, 255, 255))
        
        # Positioning for Player 1 on the left
        self.screen.blit(player1_lap_surface, (50, 50))  # Adjust position as needed
        
        # Positioning for Player 2 on the right
        self.screen.blit(player2_lap_surface, (self.screen_width - player2_lap_surface.get_width() - 50, 50))  # Adjust position as needed

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
            # Highlight selected car for Player 1
            color1 = (255, 255, 0) if self.players[0].selected_car_index == i else (255, 255, 255)
            option_surface1 = font.render(car, True, color1)
            self.screen.blit(option_surface1, (50, self.screen_height // 2 + i * 50))

            # Highlight selected car for Player 2
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

    def render_win_screen(self, winner):
        font = pygame.font.Font(None, 74)
        win_surface = font.render(f"{winner} wins!", True, (255, 255, 255))
        restart_surface = font.render("Press R to Restart", True, (255, 255, 255))
        
        self.screen.fill((0, 0, 0))  # Clear the screen
        self.screen.blit(win_surface, (self.screen_width // 2 - win_surface.get_width() // 2, self.screen_height // 4))
        self.screen.blit(restart_surface, (self.screen_width // 2 - restart_surface.get_width() // 2, self.screen_height // 2))
        
        pygame.display.flip()  # Update the display

    def reset_game(self):
        self.players[0].lap_count = 0
        self.players[1].lap_count = 0
        self.current_screen = "car_selection"