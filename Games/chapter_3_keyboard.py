import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

# pygame variables
pygame.init()

windowwidth = 800
windowheight = 800

surface = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption('Python Keyboard')

# Square variables
playerSize = 20
playerX = (windowwidth / 2) - (playerSize /2)
playerY = (windowheight - playerSize)
playerVX = 1.0
playerVY = 0.0
jumpHeight = 25.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

# Keyboard variables
leftDown = False
rightDown = False
haveJumped = False

def move():
    global playerX, playerY, playerVX, playerVY, haveJumped, gravity

    # Move left
    if leftDown:
        # If we're already moving to the rigth, reset moving speed and invert direction
        if playerVX > 0.0:
            playerVX = moveSpeed
            playerVX = -playerVX
        # Make sure our square doesn't leave the window to the left
        if playerX > 0:
            playerX += playerVX # velocity is negative
    
    # Move right
    if rightDown:
        # If we're already moving to the left, reset moving speed again
        if playerVX < 0.0:
            playerVX = moveSpeed
        # Make sure our square doesn't leave the window to the right
        if playerX + playerSize < windowwidth:
            playerX += playerVX
    
    if playerVY > 1.0:
        playerVY *= 0.9
    else:
        playerVY = 0.0
        haveJumped = False
    
    # is our square in the air? Better add some gravity to bring it back down!
    if playerY < windowheight - playerSize: # meaning the player Y position is not at the bttm of screen
        playerY += gravity
        gravity *= 1.1
    else:
        playerY = windowheight - playerSize
        gravity = 1.0

    playerY -= playerVY

    if (playerVX > 0.0 and playerVX < maxSpeed) or (playerVX < 0.0 and playerVX > -maxSpeed):
        if not haveJumped and (leftDown or rightDown):
            playerVX *= 1.1 # move faster in the x direction

# How to quit our program
def quitGame():
    pygame.quit()
    sys.exit()

while True:
    # redraw the screen with all black
    surface.fill((0,0,0))
    # Draw the player as a rectangle/square
    pygame.draw.rect(surface, (255, 0, 0), 
    (playerX, playerY, playerSize, playerSize))

    # get list of all events that happened sincer the last redraw
    for event in GAME_EVENTS.get():
        # check the event type (for key being pressed))
        if event.type == pygame.KEYDOWN:
            # check the key that was pressed
            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not haveJumped:
                    haveJumped = True
                    playerVY += jumpHeight
            if event.key == pygame.K_ESCAPE:
                quitGame()
        # check the event type (for key being released)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_RIGHT:
                rightDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_UP:
                if  haveJumped:
                    haveJumped = False
        # check for type being quit
        if event.type == GAME_GLOBALS.QUIT:
                quitGame()
    
    move()
    
    pygame.display.update()