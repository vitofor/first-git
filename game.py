import pygame
from  player import  Player
from monster import Monster
class Game():

    def __init__(self):
        #genere le joueur

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #groupe de monster
        self.all_monster= pygame.sprite.Group()
        self.pressed={}
        self.spawn_monster()
        self.spawn_monster()


    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False,pygame.sprite.collide_mask)
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)