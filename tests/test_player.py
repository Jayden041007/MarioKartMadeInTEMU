import unittest
from players import Player
from vehicles.vehicle_base import Vehicle

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer", (100, 100), (255, 255, 255), "wasd", 800, 600)
    
    def test_player_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.vehicle.x, 100)
        self.assertEqual(self.player.vehicle.y, 100)
        self.assertEqual(self.player.control_scheme, "wasd")
    
    def test_player_boundaries(self):
        self.player.vehicle.x = -10
        self.player.update(None)
        self.assertEqual(self.player.vehicle.x, 0)
        
        self.player.vehicle.x = 900
        self.player.update(None)
        self.assertEqual(self.player.vehicle.x, 800 - self.player.vehicle.width)
        
        self.player.vehicle.y = -10
        self.player.update(None)
        self.assertEqual(self.player.vehicle.y, 0)
        
        self.player.vehicle.y = 700
        self.player.update(None)
        self.assertEqual(self.player.vehicle.y, 600 - self.player.vehicle.height)
