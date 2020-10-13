from time import sleep
from picamera import PiCamera, Color
import logging
camera = PiCamera(resolution=(720, 540))
# Wait for the automatic gain control to settle
sleep(2)

logger = logging.getLogger (__name__)
logger.setLevel(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

def CamMessage():
    global camera
    camera.annotate_text =  "Contrast: " + str(camera.contrast)
    camera.annotate_text += "\nBrightness: " + str(camera.brightness)
    camera.annotate_text += "\nSaturation: " + str(camera.saturation)


logger.info("Start processing")
logger.debug("Preview camera before changes")
camera.annotate_background = Color('white')
camera.annotate_foreground = Color('black')
camera.annotate_text_size = 29
CamMessage()
camera.annotate_text += "\nFrameRate Range (low: " + str(camera.framerate_range.low) + ", high: " + str(camera.framerate_range.high) + ")"
camera.start_preview()

try:
    sleep(4)
except KeyboardInterrupt:
    logger.warning ('\n\tUser interrupted preview')
camera.stop_preview()

sleep(2)
camera.start_preview()
logger.debug("Go through the contrast levels")
try:
    for i in range(-100, 100, 2):
        #camera.brightness = i
        camera.contrast = i
        CamMessage()
        sleep(0.3)
except KeyboardInterrupt:
    logger.warning ('\n\tUser interrupted contrast loop')
camera.stop_preview()

sleep(2)
camera.start_preview()
logger.debug("Go through the brightness levels")
camera.contrast = 0 # reset to default contrast
try:
    for i in range(100):
        camera.brightness = i
        CamMessage()
        sleep(0.2)
except KeyboardInterrupt:
    logger.warning ('\n\tUser interrupted brightness loop')
camera.stop_preview()

sleep(2)
camera.start_preview()
logger.debug("Go through the saturation levels")
camera.brightness = 50 # reset to default brightness
try:
    for i in range(-100, 100, 2):
        camera.saturation = i
        CamMessage()
        sleep(0.2)
except KeyboardInterrupt:
    logger.warning ('\n\tUser interrupted brightness loop')
camera.stop_preview()

logger.info("Done processing")
