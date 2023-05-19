import pygame

# definir la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #def constructeur
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 10 #vitesse du projectile
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))  #redimenssion de l'image du projectile
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x +120
        self.rect.y = player.rect.y +80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #faire tourner le projectile
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1 )
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self): # supprimer le projectile

        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile rentre en collision
        for monster in self.player.game.check_collision(self,self.player.game.all_monster):
            #supprimer le projectile
            self.remove()
            #infligez des dégats
            monster.damage(self.player.attack)


        #verifier si le projectile est plus sur l'ecran
        if self.rect.x > 1000:
             # supprimer le projectile (en dehors de l'ecran)
            self.remove()
