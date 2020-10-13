from time import sleep
from picamera import PiCamera, Color

import pygame, sys
import logging
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

#
logger = logging.getLogger (__name__)
logger.setLevel(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

# pygame variables
pygame.init()
logger.info("Initialize program")

windowwidth = 400
windowheight = 400

surface = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption('Change Camera Settings with Keyboard')

# How to quit our program
def quitProgram():
    global logger
    logger.info("Exiting the program")
    pygame.quit()
    sys.exit()

# Update the display message
def camMessage(effect, awb):
    global camera, effectNum, awbNum, effectMax, awbMax
    effect_txt = 'Effect(' + str(effectNum) + '/' + str(effectMax) + "): " + effect
    awb_txt = '\nAWB(' + str(awbNum) + '/' + str(awbMax) + "): " + awb
    camera.annotate_text = effect_txt + awb_txt

def changeCamSettings():
    global camera, effectNum, awbNum, effectMax, awbMax, logger
    effect = 'none'
    awb = 'auto'
    a = 0
    e = 0
    for currEffect in camera.IMAGE_EFFECTS:
        if e == effectNum:
            camera.image_effect = effect = currEffect
        e += 1
    for currAwb in camera.AWB_MODES:
        if a == awbNum:
            camera.awb_mode = awb = currAwb
        a += 1
    camMessage(effect, awb)
    sleep(1)

camera = PiCamera(resolution=(1096,972), framerate=30)
# Wait for the automatic gain control to settle
sleep(1)

camera.start_preview()
camera.annotate_background = Color('white')
camera.annotate_foreground = Color('black')
camera.annotate_text_size = 31

effectNum = 0
awbNum = 1
effectMax = len(camera.IMAGE_EFFECTS)
awbMax = len(camera.AWB_MODES)
alive = True
camMessage(camera.image_effect, camera.awb_mode)

try:
    while alive:
        try:
            # get list of all events that happened sincer the last redraw
            for event in GAME_EVENTS.get():
                # check the event type (for key being pressed))
                if event.type == pygame.KEYDOWN:
                    # check the key that was pressed
                    if event.key == pygame.K_LEFT:
                        effectNum -= 1
                        effectNum %= effectMax
                        # changeCamSettings()
                    if event.key == pygame.K_RIGHT:
                        effectNum += 1
                        effectNum %= effectMax
                        # changeCamSettings()
                    if event.key == pygame.K_UP:
                        awbNum += 1
                        awbNum %= awbMax
                        # changeCamSettings()
                    if event.key == pygame.K_DOWN:
                        awbNum -= 1
                        awbNum %= awbMax
                        # changeCamSettings()
                    if event.key == pygame.K_ESCAPE:
                        alive = False
                        camera.stop_preview()
                        quitProgram()
                # check the event type (for key being released)
                if event.type == pygame.KEYUP:
                    # nothing to do
                    changeCamSettings()
                # check for type being quit
                if event.type == GAME_GLOBALS.QUIT:
                    alive = False
                    camera.stop_preview()
                    quitProgram()
            sleep(1)
        except KeyboardInterrupt:
            logger.error ('User interrupted loop')
            camera.stop_preview()
            quitProgram()

    camera.stop_preview()
    quitProgram()
except KeyboardInterrupt:
    logger.error ('User interrupted program')
    camera.stop_preview()
    quitProgram()