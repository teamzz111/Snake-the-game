#LIBRARIES
import pygame
import random
import time

#COLOURS
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)


#INITIAL GAME
pygame.init()
superficie = pygame.display.set_mode((800,500))
pygame.display.set_caption('Serpiente')

mover_x = 300
mover_y = 300
mover_x_cambio = 0
mover_y_cambio = 0
serp_tamano = 10
ancho = 800
altura = 500
cuadro = 15

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mover_x_cambio = -serp_tamano
            mover_y_cambio = 0
        elif event.key == pygame.K_RIGHT:
            mover_x_cambio = serp_tamano
            mover_y_cambio = 0
        elif event.key == pygame.K_UP:
            mover_y_cambio = -serp_tamano
            mover_x_cambio = 0
        elif event.key == pygame.K_DOWN:
            mover_y_cambio = serp_tamano
            mover_x_cambio = 0


    if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
        gameExit = True