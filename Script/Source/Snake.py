# -*- coding: utf-8 -*-

import pygame
import time
import os, pygame
import random
import sys

def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)


Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 56, 48)
Azul = (0, 0, 255)
Verde = (0, 128, 0)
VerdeF = (76, 255, 0)
Lila = (174, 0, 255)
ancho = 1200
altura = 800


superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('Snake the game v1')


background = load_image('29.jpg')


superficie.blit(background, [0, 0])


reloj = pygame.time.Clock()

serp_tamano = 20
CPS = 15

font = pygame.font.SysFont("Arial", 35)
      

def pausa():
    pausado = True
   
    while pausado:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        background = load_image('FONDO jp-01.png')
        superficie.blit(background, [0, 0])
        #superficie.fill(blanco)      
        message_to_screen("ACTUALMENTE ESTÁS EN PAUSA", Negro, -100)
        message_to_screen("PARA CONTINUAR PRESIONA C", Negro, 0);
        message_to_screen("PARA SALIR PRESIONA Q", Negro, 50)
        pygame.display.update()
        reloj.tick(5)


def puntoss(puntos, rapidez):
    text = font.render("Puntos: "+str(puntos)+ " Rapidez: " + str(rapidez), True, Negro)
    superficie.blit(text, [0,0])
    

def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        background = load_image('FONDO jp-01.png')
        superficie.blit(background, [0, 0])
        message_to_screen("BIENVENIDO A SNAKE, THE GAME!", Negro, -150)
        message_to_screen("El objetivo del juego es controlar una serpiente usando", Azul, -100)
        message_to_screen("teclas flechas de movimiento para comer manzanas", Azul, -50)
        message_to_screen("Si la serpiente toca manzana verde, la rapidez aumenta en 1 ", Azul, 0)
        message_to_screen(" Si la serpiente toca manzana lila, la serpiente se alarga 10 cuadrados.", Negro,50)
        message_to_screen(" Si la serpiente toca manzana roja, ademas de crecer 1 cuadro, aumenta puntaje en 1",Azul, 100)
        message_to_screen(", y cada 3 puntos la rapidez aumenta en 1.", Negro, 150)
        message_to_screen("Si la serpiente toca bordes o a si misma, pierdes.", Azul, 200)
        message_to_screen("Para pausar partida, presiona tecla P.", Azul, 250)
        message_to_screen("Para continuar C, para terminar de jugar y salir, presiona tecla Q.", Negro, 300)
        pygame.display.update()
        reloj.tick(15)

def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0],i[1],serp_tamano,serp_tamano])

def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()
def message_to_screen(msg, color, y_displace=0):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (ancho/2), (altura/2)+ y_displace
    superficie.blit(textSur, textRect)
    #pantalla_texto = font.render(msg, True, color)
    #superficie.blit(pantalla_texto,[display_ancho/2, display_altura/2])

    
    
def gameLoop():
    gameExit = False
    gameOver = False

    mover_x = 300
    mover_y = 300

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1
    rapidez = 10
    puntos = 0

    azarManzanaX = round(random.randrange(0, ancho - 20)/20.0)*20.0
    azarManzanaY = round(random.randrange(0, altura - 20)/20.0)*20.0

    azarManzanaXV = round(random.randrange(0, ancho - 20)/20.0)*20.0
    azarManzanaYV = round(random.randrange(0, altura - 20)/20.0)*20.0

    azarManzanaXL = round(random.randrange(0, ancho - 20)/20.0)*20.0
    azarManzanaYL = round(random.randrange(0, altura - 20)/20.0)*20.0

    pulsar_sonido = pygame.mixer.Sound("song.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)
    

    
    while not gameExit:

        while gameOver == True:
            background = load_image('25.jpg')
            superficie.blit(background, [0, 0])
            pulsar_sonido.stop()
            message_to_screen("HAS PERDIDO", Blanco, 200)
            message_to_screen("Para volver a jugar presiona C", Rojo, 250)
            message_to_screen("Para salir presione Q", Rojo, 300)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
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
                elif event.key == pygame.K_p:
                    pulsar_sonido.set_volume(0.0)
                    pausa()
                    pulsar_sonido.set_volume(0.50)


                     
                
        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
            gameOver = True


        mover_x += mover_x_cambio
        mover_y += mover_y_cambio

        background = load_image('29.jpg')
        superficie.blit(background, [0, 0])

        pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 20, 20])
        pygame.draw.rect(superficie, VerdeF, [azarManzanaXV, azarManzanaYV, 20, 20])
        pygame.draw.rect(superficie, Lila, [azarManzanaXL, azarManzanaYL, 20, 20])
        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)
        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        for eachSegment in listaSerpiente[:-1]:
            if eachSegment == cabezaSerpiente:
                gameOver = True


        serpiente(serp_tamano,listaSerpiente)
        puntoss(puntos, rapidez)
        pygame.display.update()

        

        if mover_x == azarManzanaX and mover_y == azarManzanaY: 
            pygame.mixer.music.load("Sonig.ogg")
            azarManzanaX = round(random.randrange(0, ancho-20)/20.0)*20.0
            azarManzanaY = round(random.randrange(0, altura-20)/20.0)*20.0
            pygame.mixer.music.play(0)
            puntos = puntos + 1 
            if puntos % 3 == 0 and largoSerpiente != 1:
                rapidez += 1
            largoSerpiente += 1

        elif mover_x == azarManzanaXV and mover_y == azarManzanaYV: 
            rapidez += 1
            azarManzanaXV = round(random.randrange(0, ancho-20)/20.0)*20.0
            azarManzanaYV = round(random.randrange(0, altura-20)/20.0)*20.0
            pygame.mixer.music.load("Sonig.ogg")
            pygame.mixer.music.play(0)
        elif mover_x == azarManzanaXL and mover_y == azarManzanaYL: 
            azarManzanaXL = round(random.randrange(0, ancho-20)/20.0)*20.0
            pygame.mixer.music.load("Sonig.ogg")
            azarManzanaYL = round(random.randrange(0, altura-20)/20.0)*20.0
            largoSerpiente += 10
            pygame.mixer.music.play(0)

        reloj.tick(rapidez)


    pygame.quit()
    sys.exit()

intro_juego()
gameLoop()
