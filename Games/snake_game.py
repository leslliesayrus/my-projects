import pygame
from pygame.locals import *
import random

tamanho_tela = (600,600)
tamanho_pixel = 10

pygame.init()

def colisao(pos1, pos2):
    return pos1 == pos2

def off_limits(pos):
    if 0<= pos[0] < tamanho_tela[0] and 0<= pos[1] < tamanho_tela[1]:
        return False
    else:
        return True
def renascer_apple():
    x = random.randint(0, tamanho_tela[0])
    y = random.randint(0, tamanho_tela[1])
    return x // tamanho_pixel * tamanho_pixel, y // tamanho_pixel * tamanho_pixel

def restart():
    global snake_position
    global apple_position
    global snake_direction
    snake_position = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_position = renascer_apple()




tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('my_game')

snake_position = [(250,50), (260,50), (270,50)]
snake_surface = pygame.Surface((tamanho_pixel,tamanho_pixel))
snake_surface.fill((198, 36, 209))
snake_direction = K_LEFT

apple_position = renascer_apple()
apple_surface =pygame.Surface((tamanho_pixel, tamanho_pixel))
apple_surface.fill((227, 9, 24))



while True:
    pygame.time.Clock().tick(15)
    tela.fill((0, 0 ,0))
    for event in pygame.event.get():
        if event.type == QUIT : # or pygame.locals.quit
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_LEFT, K_DOWN, K_RIGHT]:
                snake_direction = event.key


    tela.blit(apple_surface, apple_position)


# para cada posicao da cobra:
    for pos in snake_position:
        tela.blit(snake_surface, pos) # desenhar na tela

    for i in range(len(snake_position)-1, 0, -1):
        if colisao(snake_position[0], snake_position[i]):
            restart()
        snake_position[i] = snake_position[i-1]



    if colisao(snake_position[0], apple_position):
        snake_position.append((-10,-10))
        apple_position = renascer_apple()

    if off_limits(snake_position[0]):
        restart()

    if snake_direction == K_UP:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] - tamanho_pixel)
    elif snake_direction == K_DOWN:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] + tamanho_pixel)
    elif snake_direction == K_LEFT:
        snake_position[0] = (snake_position[0][0] - tamanho_pixel, snake_position[0][1])
    elif snake_direction == K_RIGHT:
        snake_position[0] = (snake_position[0][0] + tamanho_pixel, snake_position[0][1])

    ## snake position [0] = (250,50) e snake_position [0][1] = 50 ##
    #snake_position[0] = snake_position[0][0] + 10, snake_position[0][1]


    pygame.display.update()

