import pygame,sys,random
from settings import Settings
from player import Player
from bullet import Bullet
from enemy import Enemy
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.playerobj=Player()
        self.bulletobj=Bullet()
        self.enemyobj=Enemy()
        self.enemyobj.createenemy()
        self.screen=pygame.display.set_mode((700,700))
        pygame.display.set_caption(self.settings.caption)
        self.clock = pygame.time.Clock()

    def showscore(self):
        self.show_score = self.settings.font.render("Score: " + str(self.settings.score), True, (255, 255, 255))
        self.screen.blit(self.show_score, (self.settings.scorex, self.settings.scorey))

    def rungame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_colour)
            self.screen.blit(self.playerobj.player,self.playerobj.player_rect)
            self.showscore()
            for i in range(self.enemyobj.ufocounter):
                if self.bulletobj.bullet_rect is not None:
                    if self.bulletobj.bullet_rect.colliderect(self.enemyobj.ufo_rectlist[i]):
                        self.enemyobj.ufox[i] = self.enemyobj.ufo_rectlist[i].x = random.randint(0, 700 - 32)
                        self.enemyobj.ufoy[i] = self.enemyobj.ufo_rectlist[i].y = random.randint(0, 100)
                        self.bulletobj.bulletstate = False
                        self.bulletobj.bullet_rect = None
                        self.bulletobj.bullet = None
                        self.settings.score += 1
                self.screen.blit(self.enemyobj.ufolist[i], self.enemyobj.ufo_rectlist[i])

            if self.bulletobj.bulletstate is True:
                self.screen.blit(self.bulletobj.bullet, self.bulletobj.bullet_rect)
                self.bulletobj.bulletY -= 5
                self.bulletobj.bullet_rect.y -= 5
            if self.bulletobj.bulletY == 0:
                self.bulletobj.bulletstate = False

            for i in range(self.enemyobj.ufocounter):
                self.enemyobj.ufox[i] += self.enemyobj.ufox_change[i]
                self.enemyobj.ufo_rectlist[i].x += self.enemyobj.ufox_change[i]
                if self.enemyobj.ufox[i] <= 0:
                    self.enemyobj.ufox_change[i] = 5
                    self.enemyobj.ufoy[i] += 32
                    self.enemyobj.ufo_rectlist[i].y += 32
                elif self.enemyobj.ufox[i] >= 700 - 32:
                    self.enemyobj.ufox_change[i] = -5
                    self.enemyobj.ufoy[i] += 32
                    self.enemyobj.ufo_rectlist[i].y += 32
                else:
                    pass

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.playerobj.player_rect.x -= 2
                self.playerobj.playerX -= 2
            if keys[pygame.K_RIGHT]:
                self.playerobj.player_rect.x += 2
                self.playerobj.playerX += 2
            if keys[pygame.K_SPACE] and self.bulletobj.bulletstate is False:
                self.bulletobj.createbullet(self.playerobj.playerX,self.playerobj.playerY)
            if self.playerobj.playerX >= 700 - 32:
                self.playerobj.player_rect.x = 700 - 32
                self.playerobj.playerX = 700 - 32
            if self.playerobj.playerX <= 0:
                self.playerobj.player_rect.x = 0
                self.playerobj.playerX = 0

            pygame.display.flip()
            self.clock.tick(60)
if __name__=="__main__":
    game=AlienInvasion()
    game.rungame()