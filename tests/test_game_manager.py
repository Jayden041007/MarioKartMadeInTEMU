import pytest
import pygame
from game_manager import GameManager

@pytest.fixture
def game():
    return GameManager()

def test_handle_events_quit(game):
    quit_event = pygame.event.Event(pygame.QUIT)
    pygame.event.post(quit_event)
    game.handle_events()
    assert not game.running  # Check if game.running is False

def test_handle_events_escape(game):
    escape_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE})
    pygame.event.post(escape_event)
    game.handle_events()
    assert not game.running  # Check if game.running is False

def test_update_players(game):
    try:
        game.update()
    except Exception as e:
        pytest.fail(f"Update method raised an exception: {e}")

def test_render(game):
    try:
        game.render()
    except Exception as e:
        pytest.fail(f"Render method raised an exception: {e}")
