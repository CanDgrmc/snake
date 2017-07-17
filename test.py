
import pygame
import sys
import random
import time

errors=pygame.init()
if errors[1]>0:
    print('(!) Had {0} errors, Exiting...'.format(errors[1]))
    sys.exit(-1)
else:
    print('(+) Game Succesfully Initialized')

#Play Surface

surface=pygame.display.set_mode((720 , 460))
pygame.display.set_caption('Snake')

#Colors RGB

red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food

# FPS  Frames Per Second
FpsController = pygame.time.Clock()

# Important Variables
SnakePos = [100,50] # [x,y]
SnakeBody = [[100,50] , [90,50] , [80,50]]

FoodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
FoodSpawn = True

direction = 'RIGHT'
changto = direction

score=0

# GAME OVER function

def gameOver():
    myFont = pygame.font.SysFont('monaco' , 72)
    GOsurface=myFont.render('Al Gırdın Gırdın!', True , red)
    Gorect = GOsurface.get_rect()
    Gorect.midtop = (360,15)
    surface.blit(GOsurface,Gorect)
    pygame.display.flip()
    Score(0)
    time.sleep(4)
    pygame.quit() #window
    sys.exit()  #console


def Score(choice=1):
    myFont = pygame.font.SysFont('monaco', 24)
    sSurface = myFont.render('Score: {0}'.format(score), True, white)
    sRect = sSurface.get_rect()
    if choice:
        sRect.midtop = (80, 30)
        surface.blit(sSurface, sRect)

    else:
        sRect.midtop = (360, 120)
        surface.blit(sSurface, sRect)
        pygame.display.update()




##### Game Logic  #####

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changto = 'RIGHT'
            elif event.key == pygame.K_RIGHT or event.key == ord('a'):
                changto = 'LEFT'
            elif event.key == pygame.K_RIGHT or event.key == ord('s'):
                changto = 'DOWN'
            elif event.key == pygame.K_RIGHT or event.key == ord('w'):
                changto = 'UP'
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if changto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update Snake Position
    if direction == 'RIGHT':
        #[x,y]
        SnakePos[0] += 10
    if direction == 'LEFT':
        #[x,y]
        SnakePos[0] -= 10
    if direction == 'UP':
        #[x,y]
        SnakePos[1] -= 10
    if direction == 'DOWN':
        #[x,y]
        SnakePos[1] += 10

    # Snake Body Mechanism

    SnakeBody.insert(0,list(SnakePos))
    if SnakePos[0] == FoodPos[0] and SnakePos[1] == FoodPos[1]:
        FoodSpawn = False
        score+=10


    else:
        SnakeBody.pop()

    if FoodSpawn==False:
        FoodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]

    FoodSpawn = True

    surface.fill(black)
    for pos in SnakeBody:
        pygame.draw.rect(surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    for block in SnakeBody[1:]:
        if SnakePos[0] == block[0] and SnakePos[1] == block[1]:
            gameOver()
    pygame.draw.rect(surface,red,pygame.Rect(FoodPos[0], FoodPos[1], 10, 10))

    Score()
    pygame.display.flip() ## pygame.display.update()

    # Game Speed
    FpsController.tick(17)

    if(SnakePos[0] >= 720 or SnakePos[0] == 0 or SnakePos[1] >= 460 or SnakePos[1] == 0):
        gameOver()








