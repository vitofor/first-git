import pygame
import random

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)


    def damage(self, amount):
        #infliger des degats
        self.health-= amount

        #verifier si sa vie est supp a 100
        if self.health <= 0:
            # reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health


    def update_health_bar(self,surface):
        #dessiner notre bar de vie
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 10, self.rect.y - 20, self.max_health, 5]) #attention si inverser ca ne fonctionne pas car affiche le premiere plan d'abord
        # l'arriere plan de la barre devie
        pygame.draw.rect(surface,(111,210,46),[self.rect.x + 10,self.rect.y -20,self.health, 5 ])


    def forward(self):
        # le  deplacement ne se fait que si il n'y a pas de colision avec le g
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en colision avec le joueur
        else:
            self.game.player.damage(self.attack)