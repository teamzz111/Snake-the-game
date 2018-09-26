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

font = pygame.font.SysFont('Arial', 25)

def message_to_screen(msg, color):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (800) , (500)
    superficie.blit(textSur,textRect)
def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()
def gameLoop():
    pausado = True
    while pausado: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False
                mover_x = 300
                mover_y = 300
                mover_x_cambio = 0
                mover_y_cambio = 0
while not gameExit:

        while gameOver == True:
            superficie.fill(blanco)
        message_to_screen("Se acabó la partida", Negro, -50)
        message_to_screen("Para continuar presionar C, terminar presionar Q", Rojo, 50)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key pygame.K_q:
                    gameExit = True
                    gameOver = False
                if event.key == pygame.K_c:
                    gameLoop()

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
    
    pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 10, 10]) 
    superficie.fill(Blanco)
    pygame.display.update()
    reloj.tick(cuadro)