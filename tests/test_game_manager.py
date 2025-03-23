import unittest
import pygame
from game_manager import GameManager

class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.game = GameManager()

    def test_handle_events_quit(self):
        quit_event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(quit_event)
        self.game.handle_events()
        self.assertFalse(self.game.running)

    def test_handle_events_escape(self):
        escape_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE})
        pygame.event.post(escape_event)
        self.game.handle_events()
        self.assertFalse(self.game.running)
    
    def test_update_players(self):
        try:
            self.game.update()
        except Exception as i:
            self.fail(f"Update method raised an exception: {i}")
    
    def test_render(self):
        try:
            self.game.render()
        except Exception as i:
            self.fail(f"Render method raised an exception: {i}")

if __name__ == "__main__":
    unittest.main()
