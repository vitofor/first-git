import pygame
from projectile import Projectile

#creation class joueur
class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group() #chaque projectile lancer par lejoueur est stocker ici
        self.image = pygame.image.load('assets/player.png') #variable avec la surface
        self.rect = self.image.get_rect() # pour deplacer l'image
        self.rect.x = 400
        self.rect.y = 500


    def damage(self,amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            print("you are dead")
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y +15, self.max_health,7])  # attention si inverser ca ne fonctionne pas car affiche le premiere plan d'abord
        # l'arriere plan de la barre devie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y +15, self.health, 7])

    def launch_projectile(self):
        #nouvelle instance
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # que si le joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity

