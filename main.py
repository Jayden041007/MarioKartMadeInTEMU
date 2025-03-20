import pygame
from game_manager import GameManager

pygame.init()

if __name__ == "__main__":
    game = GameManager()
    game.run()