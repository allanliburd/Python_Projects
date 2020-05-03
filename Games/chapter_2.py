import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

windowwidth = 640
windowheight = 480
halfWindowW = windowwidth / 2
halfWindowH = windowheight / 2
surface = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption('Python Shapes!')

# chunk 02
greenSquareX = windowwidth / 4
greensquareY = windowheight / 4
# chunk 03
blueSquareX  = 0.0
blueSquareY  = 0.0
blueSquareVX = 1
blueSquareVY = 1
# chunk 04
rectX = windowwidth / 2
rectY = windowheight / 2
rectWidth = 50
rectHeight = 50
# chunk 05
squareRed   = random.randint(0, 255)
squareGreen = random.randint(0, 255)
squareBlue  = random.randint(0, 255)

# enable/disable chunks of code
chunk_01 = False
chunk_02 = True
chunk_03 = True
chunk_04 = True
chunk_05 = False

# Go through at most max iterations
MAX_ITER = 1000
num_iter = 0

while (num_iter < MAX_ITER):
    num_iter += 1
    # this line clears the screen
    #surface.fill((0, 0, 0))
    # chuck 01
    if chunk_01:
        pygame.draw.rect(surface, (255, 0, 0), (random.randint(0, windowwidth), random.randint(0, windowheight), 10, 10))
    # chunk 02
    if chunk_02:
        pygame.draw.rect(surface, (0, 255, 0), (greenSquareX, greensquareY, 10, 10))
        greenSquareX += 1
        greenSquareX %= windowwidth
        greensquareY += 1
        greensquareY %= windowheight
    # chunk 03
    if chunk_03:
        pygame.draw.rect(surface, (0, 0, 255), (blueSquareX, blueSquareY, 10, 10))
        blueSquareX += blueSquareVX
        blueSquareX %= windowwidth
        blueSquareY += blueSquareVY
        blueSquareY %= windowheight
        blueSquareVX += 0.1
        blueSquareVY += 0.1
        blueSquareVX %= 19
        blueSquareVY %= 23
    # chunk 04
    if chunk_04:
        pygame.draw.rect(surface, (squareRed, squareGreen, 00), (rectX - rectWidth / 2, rectY - rectHeight /2, rectWidth, rectHeight))
        rectWidth  += 1
        rectWidth  %= halfWindowW
        rectHeight += 1
        rectHeight %= halfWindowH
    # chunk 05
    if chunk_05:
        pygame.draw.rect(surface, (squareRed, squareGreen, squareBlue), (50, 50, windowwidth / 2, windowheight / 2))
        squareRed   += 1
        squareRed   %= 255
        squareGreen += 1
        squareGreen %= 255
        squareBlue  += 1
        squareBlue  %= 255
    
    # close the program if QUIT is requested
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    # update the screen
    pygame.display.update()