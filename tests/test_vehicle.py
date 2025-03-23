import unittest
import pygame
from vehicles.vehicle_base import Vehicle
from track.track import Track

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.screen_width = 800
        self.screen_height = 600
        self.track = Track(self.screen_width, self.screen_height)
        self.vehicle = Vehicle((100, 100), (255, 0, 0))

    def test_vehicle_initialization(self):
        self.assertEqual(self.vehicle.x, 100)
        self.assertEqual(self.vehicle.y, 100)
        self.assertEqual(self.vehicle.speed, self.vehicle.default_speed)
        self.assertEqual(self.vehicle.color, (255, 0, 0))
        self.assertEqual(self.vehicle.width, 20)
        self.assertEqual(self.vehicle.height, 40)

    def test_vehicle_speed_in_slow_zone(self):
        self.vehicle.x = self.track.center_x
        self.vehicle.y = self.track.center_y

        keys = [False] * 323  
        self.vehicle.move(keys, up=False, down=False, left=False, right=False, track=self.track)

        self.assertEqual(self.vehicle.speed, self.vehicle.default_speed // 2)

    def test_vehicle_movement(self):
        keys = [False] * 323  
        keys[pygame.K_UP] = True
        keys[pygame.K_RIGHT] = True

        initial_x, initial_y = self.vehicle.x, self.vehicle.y

        self.vehicle.move(keys, up=True, down=False, left=False, right=True, track=self.track)

        self.assertEqual(self.vehicle.y, initial_y - self.vehicle.speed)
        self.assertEqual(self.vehicle.x, initial_x + self.vehicle.speed)

    def test_vehicle_no_movement(self):
        keys = [False] * 323

        initial_x, initial_y = self.vehicle.x, self.vehicle.y

        self.vehicle.move(keys, up=False, down=False, left=False, right=False, track=self.track)

        self.assertEqual(self.vehicle.x, initial_x)
        self.assertEqual(self.vehicle.y, initial_y)
