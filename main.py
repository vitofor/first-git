import pygame
import math
from player import Player
from game import Game
pygame.init()



#generer la fenetre du jeu
pygame.display.set_caption("comet fall game") #le nom de la fenetre
screen = pygame.display.set_mode((1080,720)) #la taille de la fenetre

#importer la background
background =pygame.image.load("assets/bg.jpg")

#importer charger la baniere
banner = pygame.image.load("assets/banner.png")
    #redimentioner la banniere
banner = pygame.transform.scale(banner,(500,500))
    #assiotiation a un rectangle
banner_rect = banner.get_rect()
    #math.ceil arondir la valeur car probleme avec float
banner_rect.x = math.ceil(screen.get_width() /4)



#importer charger notre boutton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() /3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2 )


#chager le jeu
game = Game()

clock = pygame.time.Clock()


running = True



while running:  #boucle de jeu

    #appliquer l'arriere plan du jeu
    screen.blit(background,(0,-200))

    #verifier si notre jeu à commencé
    if game.is_playing:
        # declenccher les intructions de la partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran d'acceuil l
        screen.blit(play_button, play_button_rect)
        screen.blit(banner,banner_rect)


    #mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme le jeu
    for event in pygame.event.get():
        # que l'evenement est
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #dectecter si le joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclanchée pour les projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souris est en collision avec le button
            if play_button_rect.collidepoint(event.pos):
                print("ouiii")
                game.start()

    clock.tick(60)

