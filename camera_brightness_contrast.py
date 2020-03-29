from time import sleep
from picamera import PiCamera, Color
import logging
camera = PiCamera(resolution=(720, 540), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)

logger = logging.getLogger (__name__)
logger.setLevel(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

camera.start_preview()
#camera.annotate_text = "Brightness: " + camera.brightness + "\nContrast: " + camera.contrast
sleep(4)
camera.stop_preview()

sleep(2)
camera.start_preview()
logger.debug("Go through the contrast levels")
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    #camera.brightness = i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()
sleep(2)
camera.start_preview()
logger.debug("Go through the brightness levels")
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    #camera.contrast = i
    sleep(0.1)
camera.stop_preview()
logger.debug("Done processing")
