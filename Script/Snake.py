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
icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)
mover_x = 300
mover_y = 300
mover_x_cambio = 0
mover_y_cambio = 0
serp_tamano = 10
ancho = 800
altura = 500
cuadro = 15
gameOver = False
gameExit = False
font = pygame.font.SysFont('Arial', 25)

def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0],i[1], serp_tamano, serp_tamano])

def message_to_screen(msg, color):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (800) , (500)
    superficie.blit(textSur,textRect)
def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()
listaSerpiente = []
largoSerpiente = 1
    
azarManzanaX = round(random.randrange(0, 300 - 10)/10.0)*10.0
azarManzanaY = round(random.randrange(0, 300 - 10)/10.0)*10.0


reloj = pygame.time.Clock()

def puntos(score):
    text = font.render("Puntos: "+str(score), True, Negro)
    superficie.blit(text, [0,0])

def pausa():
    pausado = True
    while pausado:
        superficie.fill(Blanco)
        message_to_screen("Pausa", Negro)
        pygame.display.update()
        reloj.tck(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
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
                if event.key ==  pygame.K_q:
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
            pausa()

    if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
        gameExit = True
                    
    mover_x += mover_x_cambio
    mover_y += mover_y_cambio
    superficie.fill(Blanco)
    pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 10, 10]) 

    cabezaSerpiente = []

    cabezaSerpiente.append(mover_x)
    cabezaSerpiente.append(mover_y)
    listaSerpiente.append(cabezaSerpiente)
    if len(listaSerpiente) > largoSerpiente:
        del listaSerpiente[0]
    serpiente(serp_tamano, listaSerpiente)
    puntos(largoSerpiente-1)
    pygame.display.update()

    if mover_x == azarManzanaX and mover_y == azarManzanaY:
        azarManzanaX = round(random.randrange(0, 300 - 10)/10.0)*10.0
        azarManzanaY = round(random.randrange(0, 300 - 10)/10.0)*10.0
        largoSerpiente += 1
              
    reloj.tick(cuadro)
message_to_screen("Has perdido", Rojo)
pygame.display.update()
time.sleep(3)
    
pygame.quit()
quit()
