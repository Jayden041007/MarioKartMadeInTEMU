import pygame

class CheckpointManager:
    def __init__(self):
        self.checkpoints = []
        self.lap_counter = 0
        self.total_laps = 3
        self.current_checkpoint = 0

    def add_checkpoints(self, checkpoints):
        self.checkpoints = checkpoints

    def check_player_progress(self, player):
        vehicle_rect = pygame.Rect(player.vehicle.x, player.vehicle.y, player.vehicle.width, player.vehicle.height)
        
        # Check for checkpoint collision
        if self.current_checkpoint < len(self.checkpoints):
            if vehicle_rect.colliderect(self.checkpoints[self.current_checkpoint]):
                self.current_checkpoint += 1

                # Check if all checkpoints have been passed for a lap
                if self.current_checkpoint == len(self.checkpoints):
                    self.lap_counter += 1
                    self.current_checkpoint = 0  # Reset for next lap

    def reset(self):
        self.lap_counter = 0
        self.current_checkpoint = 0