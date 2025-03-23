import unittest
import pygame
from track.track import Track

class TestTrack(unittest.TestCase):
    def setUp(self):
        self.screen_width = 800
        self.screen_height = 600
        self.track = Track(self.screen_width, self.screen_height)
    
    def test_track_initialization(self):
        self.assertEqual(self.track.screen_width, self.screen_width)
        self.assertEqual(self.track.screen_height, self.screen_height)
        self.assertEqual(self.track.track_width, int(self.screen_width * 0.8))
        self.assertEqual(self.track.track_height, int(self.screen_height * 0.6))
    
    def test_slow_zone_dimensions(self):
        self.assertEqual(self.track.slow_zone.x, self.track.center_x)
        self.assertEqual(self.track.slow_zone.y, self.track.center_y)
        self.assertEqual(self.track.slow_zone.width, self.track.track_width)
        self.assertEqual(self.track.slow_zone.height, self.track.track_height)
    
    def test_draw_function(self):
        screen = pygame.Surface((self.screen_width, self.screen_height))
        try:
            self.track.draw(screen)
        except Exception as i:
            self.fail(f"Draw method raised an exception: {i}")
