import pygame
class Player:
    def __init__(self):
        self.player=pygame.image.load("images/space-ship.png")
        self.player_rect=self.player.get_rect()
        self.playerX = self.player_rect.x = 340
        self.playerY = self.player_rect.y = 600
