import pygame,random
class Enemy:
    def __init__(self):
        self.ufolist = [None] * 5
        self.ufo_rectlist = [None] * 5
        self.ufox = [None] * 5
        self.ufox_change = [5] * 5
        self.ufoy = [None] * 5
        self.ufocounter = 5
    def createenemy(self):
        for i in range(self.ufocounter):
            self.ufolist[i] = pygame.image.load("images/ufo.png")
            self.ufo_rectlist[i] = self.ufolist[i].get_rect()
            self.ufox[i] = self.ufo_rectlist[i].x = random.randint(0, 700 - 32)
            self.ufoy[i] = self.ufo_rectlist[i].y = random.randint(0, 100)