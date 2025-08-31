import pygame

class Bullet:
    def __init__(self):
        self.bulletstate = False
        self.bullet = None
        self.bullet_rect = None
        self.bulletX = None
        self.bulletY = None
    def createbullet(self,playerX,playerY):
        self.bulletstate = True
        self.bullet = pygame.image.load("images/bullet.png")
        self.bullet_rect = self.bullet.get_rect()
        self.bulletX = self.bullet_rect.x = playerX
        self.bulletY = self.bullet_rect.y = playerY
