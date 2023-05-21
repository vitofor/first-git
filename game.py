import pygame
from  player import  Player
from monster import Monster

class Game():
    #definir si notre jeu a commencé ou non

    def __init__(self):
        #genere le joueur
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #groupe de monster
        self.all_monster= pygame.sprite.Group()
        self.pressed={}

    def start(self):
        self.spawn_monster()
        self.spawn_monster()

        self.is_playing = True

    def game_over(self):
        #mettre le jeu en dans le menu et remttre a 0 les parametres
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self,screen):

        # appliquer l'image du joeur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre devie du joueur
        self.player.update_health_bar(screen)

        # recuper les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuper les monstres du jeu
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'image des projectile
        self.player.all_projectiles.draw(screen)  # .draw sert a mettre sur l'ecran l'ensemeble de element du groupe

        # aplliquer les images des projectiles
        self.all_monster.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False,pygame.sprite.collide_mask)
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)