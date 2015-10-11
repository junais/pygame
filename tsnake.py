import random, pygame, sys
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 760
WINDOWHEIGHT = 600
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
ORANGE    = (255, 128,   0)
PURPLE   = (255,   0, 255)


BGCOLOR =BLACK 

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('TRICKY SNAKE')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    # Set a random start point.
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    startk1x = random.randint(5, CELLWIDTH - 6)
    startk1y = random.randint(5, CELLHEIGHT - 6)
    startk2x = random.randint(5, CELLWIDTH - 6)
    startk2y = random.randint(5, CELLHEIGHT - 6)
    startk3x = random.randint(5, CELLWIDTH - 6)
    startk3y = random.randint(5, CELLHEIGHT - 6)
    startk4x = random.randint(5, CELLWIDTH - 6)
    startk4y = random.randint(5, CELLHEIGHT - 6)
    startk5x = random.randint(5, CELLWIDTH - 6)
    startk5y = random.randint(5, CELLHEIGHT - 6)
    startk6x = random.randint(5, CELLWIDTH - 6)
    startk6y = random.randint(5, CELLHEIGHT - 6)
    startk7x = random.randint(5, CELLWIDTH - 6)
    startk7y = random.randint(5, CELLHEIGHT - 6)
    startk8x = random.randint(5, CELLWIDTH - 6)
    startk8y = random.randint(5, CELLHEIGHT - 6)
    snakeCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    killer1Coords = [{'x': startk1x,     'y': startk1y},
                  {'x': startk1x - 1, 'y': startk1y},
                  {'x': startk1x - 2, 'y': startk1y}]
    killer2Coords = [{'x': startk2x,     'y': startk2y},
                  {'x': startk2x - 1, 'y': startk2y},
                  {'x': startk2x - 2, 'y': startk2y}]
    killer3Coords = [{'x': startk3x,     'y': startk3y},
                  {'x': startk3x - 1, 'y': startk3y},
                  {'x': startk3x - 2, 'y': startk3y}]
    killer4Coords = [{'x': startk4x,     'y': startk4y},
                  {'x': startk4x - 1, 'y': startk4y},
                  {'x': startk4x - 2, 'y': startk4y}]
    killer5Coords = [{'x': startk5x,     'y': startk5y},
                  {'x': startk5x - 1, 'y': startk5y},
                  {'x': startk5x - 2, 'y': startk5y}]
    killer6Coords = [{'x': startk6x,     'y': startk6y},
                  {'x': startk6x - 1, 'y': startk6y},
                  {'x': startk6x - 2, 'y': startk6y}]
    killer7Coords = [{'x': startk7x,     'y': startk7y},
                  {'x': startk7x - 1, 'y': startk7y},
                  {'x': startk7x - 2, 'y': startk7y}]
    killer8Coords = [{'x': startk8x,     'y': startk8y},
                  {'x': startk8x - 1, 'y': startk8y},
                  {'x': startk8x - 2, 'y': startk8y}]                                                                                                                                
    direction = RIGHT
    soundObj = pygame.mixer.Sound('point.wav')
    soundHit = pygame.mixer.Sound('hit.wav')
    # Start the apple in a random place.
    apple = getRandomLocation()

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        if snakeCoords[HEAD]['x'] == -1 or snakeCoords[HEAD]['x'] == CELLWIDTH or snakeCoords[HEAD]['y'] == -1 or snakeCoords[HEAD]['y'] == CELLHEIGHT:
            soundHit.play()
            return # game over
        for snakeBody in snakeCoords[1:]:
            if snakeBody['x'] == snakeCoords[HEAD]['x'] and snakeBody['y'] == snakeCoords[HEAD]['y']:
                soundHit.play()
                return 

        for snakeBody in snakeCoords[1:]:
            if snakeBody['x']==killer1Coords[HEAD]['x'] and snakeBody['y']== killer1Coords[HEAD]['y']:
                soundHit.play()
                return

        for snakeBody in snakeCoords[1:]:
            if snakeBody['x']==killer2Coords[HEAD]['x'] and snakeBody['y']== killer2Coords[HEAD]['y']:
                soundHit.play()
                return      

        for snakeBody in snakeCoords[1:]:
            if snakeBody['x']==killer3Coords[HEAD]['x'] and snakeBody['y']== killer3Coords[HEAD]['y']:
                soundHit.play()
                return          

        for snakeBody in snakeCoords[1:]:
            if snakeBody['x']==killer4Coords[HEAD]['x'] and snakeBody['y']== killer4Coords[HEAD]['y']:
                soundHit.play()
                return        

                    
        if snakeCoords[HEAD]['x'] == apple['x'] and snakeCoords[HEAD]['y'] == apple['y']:
            soundObj.play()
            
            apple = getRandomLocation() # set a new apple somewhere
           # apple2 = getRandomLocation() # set a new apple somewhere
        else:
            del snakeCoords[-1]

        # move the snake by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snakeCoords[HEAD]['x'] - 1, 'y': snakeCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': snakeCoords[HEAD]['x'] + 1, 'y': snakeCoords[HEAD]['y']}
        snakeCoords.insert(0, newHead)
        background_image = pygame.image.load("image.jpg").convert()
        DISPLAYSURF.blit(background_image, [0, 0])
        #DISPLAYSURF.fill(BGCOLOR)
        drawsnake(snakeCoords)
        drawkillers(killer1Coords)
        drawkillers(killer2Coords)
        drawkillers(killer3Coords)
        drawkillers(killer4Coords)
        drawkillers(killer5Coords)
        drawkillers(killer6Coords)
        drawkillers(killer7Coords)
        drawkillers(killer8Coords)
        drawApple(apple)
        #drawApple(apple2)
        drawScore(len(snakeCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(2)
    background_image = pygame.image.load("snake1.jpeg").convert()
    DISPLAYSURF.blit(background_image, [0, 0])
    StartFont = pygame.font.Font('freesansbold.ttf', 150)
    Surf1 = StartFont.render('TRICKY', True, WHITE)
    Surf2 = StartFont.render('SNAKE', True, WHITE)
    Rect1 = Surf1.get_rect()
    Rect2 = Surf2.get_rect()
    Rect1.midtop = (WINDOWWIDTH / 2, 10)
    Rect2.midtop = (WINDOWWIDTH / 2, Rect1.height + 10 + 25)
    DISPLAYSURF.blit(Surf1, Rect1)
    DISPLAYSURF.blit(Surf2, Rect2)
    drawPressKeyMsg()
    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            pygame.mixer.music.stop()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
       
def terminate():
    pygame.quit()
    sys.exit()

def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('PLING', True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    DISPLAYSURF.blit(gameSurf, gameRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawsnake(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, WHITE, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, snakeInnerSegmentRect)


def drawkillers(killerCoords):
    #getRandomLocation()
    for coord in killerCoords:
        getRandomLocation()
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        killerSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF,ORANGE , killerSegmentRect)
        killerInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, PURPLE, killerInnerSegmentRect)



def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)

if __name__ == '__main__':
    main()