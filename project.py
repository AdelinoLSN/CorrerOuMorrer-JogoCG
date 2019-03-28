# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from copy import copy as copy
import pygame
import sys
import time
import pygame.mixer
from pygame.locals import *

global matriz,vertices,faces,inicio
global direcao,Xp,Zp,i,j,inicio,cont
global mode, screen, l
cont = 0
l = -9.0
inicio = 0
Xp = 1.5
Zp = -124
i = 2
j = 123
para = False

#######################################################################################################
############################################### TELAS #################################################
pygame.init()

def exitgame():
    pygame.quit()
    sys.exit()

def top():
    clock = pygame.time.Clock()
    pygame.display.set_caption('Recorde')
    width, height = 510, 480
    screen = pygame.display.set_mode((width, height))

    #Fundo do pygame
    WHITE = (255, 255, 255)
    #Tamanho da fonte
    basicFont = pygame.font.SysFont(None, 40)

    arq = open("recorde.txt","r")
    a = []
    for i in arq:
        a.append(float(i.replace("\n","")))
    r = min(a)

    #Armazena o texto em uma variavel(Passando por parametro: TEXTO; VISIBILIDADE; COR
    nada1 = basicFont.render('######################', True, (0,0,0))
    nada3 = basicFont.render('Recorde = '+str(r), True, (0,0,0))
    nada5 = basicFont.render('######################', True, (0,0,0))
    sair =  basicFont.render('Sair -> ( esq )', True, (0,0,0))
    clock.tick(60)
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                exitgame()
        #desenha os textos na tela
        screen.blit(nada1, (width/4,20))
        screen.blit(nada3, (width/4,100))
        screen.blit(nada5, (width/4,180))
        screen.blit(sair, (width/4,300))

        pygame.display.flip()
        screen.fill(WHITE)


def telaPerdeu():
    clock = pygame.time.Clock()
    pygame.display.set_caption('Perdeu')
    width, height = 510, 480
    screen = pygame.display.set_mode((width, height))

    #Fundo do pygame
    WHITE = (255, 255, 255)
    #Tamanho da fonte
    basicFont = pygame.font.SysFont(None, 40)

    #Armazena o texto em uma variavel(Passando por parametro: TEXTO; VISIBILIDADE; COR
    nada1 = basicFont.render('######################', True, (0,0,0))
    nada3 = basicFont.render('-----Voce Perdeu------', True, (0,0,0))
    nada5 = basicFont.render('######################', True, (0,0,0))
    sair =  basicFont.render('Sair -> ( esq )', True, (0,0,0))
    clock.tick(60)
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                exitgame()
        #desenha os textos na tela
        screen.blit(nada1, (width/4,20))
        screen.blit(nada3, (width/4,100))
        screen.blit(nada5, (width/4,180))
        screen.blit(sair, (width/4,300))

        pygame.display.flip()
        screen.fill(WHITE)

def telaGanhouCasual():
    clock = pygame.time.Clock()
    pygame.display.set_caption('Ganhou')
    width, height = 510, 480
    screen = pygame.display.set_mode((width, height))

    #Fundo do pygame
    WHITE = (255, 255, 255)
    #Tamanho da fonte
    basicFont = pygame.font.SysFont(None, 40)

    #Armazena o texto em uma variavel(Passando por parametro: TEXTO; VISIBILIDADE; COR
    nada1 = basicFont.render('######################', True, (0,0,0))
    nada3 = basicFont.render('-----Voce Ganhou------', True, (0,0,0))
    nada5 = basicFont.render('######################', True, (0,0,0))
    sair =  basicFont.render('Sair -> ( esq )', True, (0,0,0))
    clock.tick(60)
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                exitgame()
        #desenha os textos na tela
        screen.blit(nada1, (width/4,20))
        screen.blit(nada3, (width/4,100))
        screen.blit(nada5, (width/4,180))
        screen.blit(sair, (width/4,300))
        
        pygame.display.flip()
        screen.fill(WHITE)

def telaGanhouCompetitivo(t):
    clock = pygame.time.Clock()
    pygame.display.set_caption('Ganhou')
    width, height = 510, 480
    screen = pygame.display.set_mode((width, height))

    #Fundo do pygame
    WHITE = (255, 255, 255)
    #Tamanho da fonte
    basicFont = pygame.font.SysFont(None, 40)

    #Armazena o texto em uma variavel(Passando por parametro: TEXTO; VISIBILIDADE; COR
    nada1 = basicFont.render('######################', True, (0,0,0))
    nada3 = basicFont.render('-----Voce Ganhou------', True, (0,0,0))
    nada5 = basicFont.render('######################', True, (0,0,0))
    nada6 = basicFont.render('Recorde = '+ str(t)+"s", True, (0,0,0))
    sair =  basicFont.render('Sair -> ( esq )', True, (0,0,0))
    clock.tick(60)
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                exitgame()
        #desenha os textos na tela
        screen.blit(nada1, (width/4,20))
        screen.blit(nada3, (width/4,100))
        screen.blit(nada5, (width/4,180))
        screen.blit(nada6, (width/4,220))
        screen.blit(sair, (width/4,300))  

        pygame.display.flip()
        screen.fill(WHITE)


def menu():
    clock = pygame.time.Clock()
    pygame.display.set_caption('Correr ou Morrer')
    width, height = 510, 480
    screen = pygame.display.set_mode((width, height))

    #Fundo do pygame
    WHITE = (255, 255, 255)
    #Tamanho da fonte
    basicFont = pygame.font.SysFont(None, 40)

    #Armazena o texto em uma variavel(Passando por parametro: TEXTO; VISIBILIDADE; COR
    novo = basicFont.render('Casual -> ( C )', True, (0,0,0))
    instru = basicFont.render('Competitivo -> ( K )', True, (0,0,0))
    record = basicFont.render('Recorde -> ( R )', True, (0,0,0))
    sair =  basicFont.render('Sair -> ( Esc )', True, (0,0,0))

    clock.tick(60)
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                exitgame()

        #desenha os textos na tela
        screen.blit(novo, (width/4,10))
        screen.blit(instru, (width/4,100))
        screen.blit(record, (width/4,200))
        screen.blit(sair, (width/4,300))

         #Verifica se alguma tecla foi pressionada
        if event.type == KEYUP and event.key == K_c:
            main(0)

        elif event.type == KEYUP and event.key == K_r:
            top()


        elif event.type == KEYUP and event.key == K_k:
            main(1)

        #Atualiza a Tela
        pygame.display.flip()
        screen.fill(WHITE)


#######################################################################################################
#################################### Leitura da Textura ###############################################

#Faz a leitura da imagem (textura parede)
def loadTexture(imagem):          
    textureSurface = pygame.image.load(imagem)            
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width() #tamanho
    height = textureSurface.get_height() #tamanho
    glEnable(GL_TEXTURE_2D) # Habilita a geração da textura
    texid = glGenTextures(1) # ID da textura atual
    glBindTexture(GL_TEXTURE_2D, texid) #especifica textura utilizada
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                    0, GL_RGBA, GL_UNSIGNED_BYTE, textureData) # target,nivel de detalhe, numero de valor de cor,tamanho da imagem, border, tipo de valor de cor esperado

    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    return texid
            

#######################################################################################################
########################################## Musica #####################################################
# adicionar musica
def tocar():
    file = "r.wav"
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
#######################################################################################################
############################### Criacao/modificacao do mapa ###########################################   

def criandoMapa(fase): # Cria o mapa partindo de uma matriz
    global matriz
    arquivo = open(fase,"r")
    matriz = arquivo.readlines()
    arquivo.close()
    
    for i in xrange(len(matriz)):
        matriz[i] = (matriz[i].replace('\n','')).split(',')
        for j in xrange(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    
    vertices = [[0,0,0],[0,1,0],[1,0,0],[1,1,0],[1,0,-1],[1,1,-1],[0,0,-1],[0,1,-1]]
    faces = [[0,2,4,6],[1,3,5,7],[0,1,3,2],[2,3,5,4],[4,5,7,6],[6,7,1,0]]

    return matriz, vertices, faces

# Função "principal"
def draw():
    global l
    light_diffuse = [1.0, 1.0, 1.0, 1.0]    # cor da luz
    light_position = [l, 2.0, l, 2]   # posição da luz
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); # limpa o buffer
    
    glEnable(GL_DEPTH_TEST);
    glLoadIdentity()
    loadTexture("bricks.bmp") #carrega a primeira textura
    glEnable(GL_NORMALIZE) # normaliza a normal de todo o objeto
    glShadeModel(GL_SMOOTH) # define que a "troca" de sombra deve ser suave (smooth)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)     # luz básica
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)   # configura a posição da luz
    glEnable(GL_LIGHTING)   # habilita a iluminação
    glEnable(GL_LIGHT0)     # "liga" a luz
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE) 
    glEnable(GL_COLOR_MATERIAL)

    glTranslatef(Xp, -0.5, Zp); # posição da "câmera"
    glRotatef(0, 1,0,0);  # posiciona o mundo de forma visivel
    glRotatef(270, 0,1,0);  # posiciona o mundo de forma visivel
    global matriz,vertices,faces
    vetor = [[0,0],[1,0],[1,1],[0,1]] #vetor auxiliar para textura
    fases = ['fase-1','fase-2']
    
    matriz, vertices,faces = criandoMapa(fases[0])
    j = 0
    for x in xrange(len(matriz)):
        for z in xrange(len(matriz[0])):
            glBegin(GL_QUADS)
            for f in faces:
                if matriz[x][z] == 1:
                    glColor3f(0.5,0.5,0.5)                # Cria o mapa partindo da matriz
                    for i in xrange(len(f)):
                        glTexCoord2f(vetor[i][0], vetor[i][1])      #aplicação da textura
                        glVertex3f((vertices[f[i]][0]+x),(vertices[f[i]][1]),(vertices[f[i]][2]+z))

            glEnd()
            glFlush()
    loadTexture("u.bmp") #carrega a segunda textura
    for x in xrange(len(matriz)):
        for z in xrange(len(matriz[x])):
            glBegin(GL_QUADS)
            f = faces[0]                             # faz o chão
            vetor = [[0,0],[1,0],[1,1],[0,1]]  #vetor auxiliar para textura
            for i in xrange(len(f)):
                glColor3f(1.0,1.0,1.0)
                glTexCoord2f(vetor[i][0], vetor[i][1]) #aplicação da textura
                glVertex3f((vertices[f[i]][0]+x),(vertices[f[i]][1]),(vertices[f[i]][2]+z))
            glEnd()
            glFlush()

    #load3()
    for x in xrange(len(matriz)):
        for z in xrange(len(matriz[x])):
            glBegin(GL_QUADS)
            f = faces[0]                             # faz o chão
            vetor = [[0,0],[1,0],[1,1],[0,1]]  #vetor auxiliar para textura
            for i in xrange(len(f)):
                glColor3f(1.0,1.0,1.0)
                #glTexCoord2f(vetor[i][0], vetor[i][1]) #aplicação da textura
                glVertex3f((vertices[f[i]][0]+x),(vertices[f[i]][1]+1),(vertices[f[i]][2]+z))
            glEnd()
            glFlush()

    glutSwapBuffers()
    if not para and mode == 0:    # se for o modo casual e não parou o jogo continua movendo
        glutIdleFunc(keep_moving) 

########################################################################################################
################################### Regras do jogo e movimentação ######################################

def keys(key,x,y):  
    global Xp,Zp,matriz,i,j,para,inicio,cont,l
    if not para: #se não perdeu ou ganhou
        if Zp > -2.1 and cont < 1: # se chegou no final do estagio 
            pygame.mixer.music.stop()
            fim = time.time() #salva o tempo
            cont = 1
            arquivo = open("recorde.txt","a")
            arquivo.write(str(fim-inicio) + '\n')
            arquivo.close()
            glutHideWindow()
            telaGanhouCompetitivo(fim - inicio)
        elif key == 'w':
            if mode !=0: #Só ativa o w se for o modo competitivo
                if inicio == 0:
                    inicio = time.time() # começa a marcar o tempo
                if(matriz[j-1][i]==0): #verifica se é parede ou não
                    Zp += 1
                    j -= 1
                else:
                    pygame.mixer.music.stop()
                    glutHideWindow() 
                    telaPerdeu()
                    para = True
        elif key == 'd': #movimento pra direita
            if(matriz[j][i-1]==0):#verifica se é parede ou não
                Xp -= 1
                i -= 1
        elif key == 'a': #movimento pra esquerda
            if(matriz[j][i+1]==0):#verifica se é parede ou não
                Xp += 1
                i += 1
        elif key == '.':
            l -= 1
        elif key == ',':
            l += 1
        glutPostRedisplay() #Faz a tela se "redesenhada"
        

# faz o movimento continuo nomodo casual
def keep_moving():
    global Zp, j, i, para
    speed = 0.4      # velocidade da "camera"
    if(Zp > -2.5 ): # se chegou ao fim do estagio ganhou
        pygame.mixer.music.stop()
        para = True
        glutIdleFunc(None) 
        glutHideWindow()      
        telaGanhouCasual()
        
    elif(matriz[j-1][i]==0): #verifica se é parede
        Zp += speed
        divi = int(abs(Zp))/1
        mod = abs(Zp) - float(divi)
        if (mod < speed):
            j -= 1
    else:                  # se bateu na parede 
        if mode == 0:
            glutIdleFunc(None)
            para = True
            pygame.mixer.music.stop()
            glutHideWindow()
            telaPerdeu()


    glutPostRedisplay()
################################################################################################
    
def main(m): # função de chama todas as outras (principal),recebe o modo como parametro
    global mode,inicio
    mode = m
    glutInit()

    tocar() # começa a musica
    glutInitWindowSize(1366, 768) #tamanho da tela

    glutInitWindowPosition(0, 0) #posição da tela
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    

    glutCreateWindow("Run") # nome da tela
    glutDisplayFunc(draw)  #Chama afunção draw
    glutKeyboardFunc(keys) #ativa os comando do teclado

    glClearColor(0.0, 0.0, 0.5, 0.0) # cor do fundo
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,1.6,1,50) # angulo de visão em y, proporção da tela em x, zNear, zFar
    glMatrixMode(GL_MODELVIEW)
    glutMainLoop()


menu()
