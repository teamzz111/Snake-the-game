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