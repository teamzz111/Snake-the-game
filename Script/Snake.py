import pygame
import time
import os, pygame
import random

def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)


Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Verde = (0, 128, 0)

ancho = 800
altura = 600


superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('Serpiente')


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
                    quit()
        background = load_image('25.jpg')
        superficie.blit(background, [0, 0])
        #superficie.fill(blanco)      
        message_to_screen("Pausa", Negro, -100)
        pygame.display.update()
        reloj.tick(5)


def puntos(score):
    text = font.render("Puntos: "+str(score), True, Negro)
    superficie.blit(text, [0,0])

def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        background = load_image('FONDO jp-01.png')
        superficie.blit(background, [0, 0])
        message_to_screen("Bienvenido, bienvenida", Negro, -100)
        message_to_screen("El objetivo del juego es controlar una serpiente usando", Azul, -50)
        message_to_screen("teclas flechas de movimiento para comer manzanas", Azul, 0)
        message_to_screen("Si la serpiente toca el borde o se toca a si misma, pierdes.", Negro, 50)
        message_to_screen("Para pausar partida, presiona tecla P.", Azul, 100)
        message_to_screen("Para continuar partida, presiona tecla C.", Azul, 150)
        message_to_screen("Para terminar de jugar y salir, presiona tecla Q.", Negro, 200)
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

    azarManzanaX = round(random.randrange(0, 300 - 20)/20.0)*20.0
    azarManzanaY = round(random.randrange(0, 300 - 20)/20.0)*20.0

    pulsar_sonido = pygame.mixer.Sound("song.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)
    

    
    while not gameExit:

        while gameOver == True:


      
            ##superficie.fill(blanco)
            superficie.blit(background, [0, 0])
            pulsar_sonido.stop()
            message_to_screen("Game Over", Negro, -50)
            message_to_screen("Para continuar presione C. Para terminar presione Q", Rojo, 50)
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
        ##superficie.fill(blanco)
        superficie.blit(background, [0, 0])

        pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 20, 20])

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
        puntos(largoSerpiente-1)
        pygame.display.update()

        

        if mover_x == azarManzanaX and mover_y == azarManzanaY: 
            pygame.mixer.music.load("Sonig.ogg")
            azarManzanaX = round(random.randrange(0, 300-20)/20.0)*20.0
            azarManzanaY = round(random.randrange(0, 300-20)/20.0)*20.0
            largoSerpiente += 1
            pygame.mixer.music.play(0)
            
        reloj.tick(CPS)


    pygame.quit()
    quit()

intro_juego()
gameLoop()