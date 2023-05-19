import pygame
from player import Player
from game import Game
pygame.init()



#generer la fenetre du jeu
pygame.display.set_caption("comet fall game") #le nom de la fenetre
screen = pygame.display.set_mode((1080,720)) #la taille de la fenetre

#importer la background
background =pygame.image.load("assets/bg.jpg")


#chager le jeu
game = Game()

clock = pygame.time.Clock()


running = True



while running:  #boucle de jeu

    #appliquer l'arriere plan du jeu
    screen.blit(background,(0,-200))

    # appliquer l'image du joeur
    screen.blit(game.player.image, game.player.rect)

    #actualiser la barre devie du joueur
    game.player.update_health_bar(screen)

    #recuper les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuper les monstres du jeu
    for  monster in game.all_monster:
        monster.forward()
        monster.update_health_bar(screen)



    # appliquer l'image des projectile
    game.player.all_projectiles.draw(screen) #.draw sert a mettre sur l'ecran l'ensemeble de element du groupe

    # aplliquer les images des projectiles
    game.all_monster.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print((game.player.rect.x))


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

    clock.tick(60)

