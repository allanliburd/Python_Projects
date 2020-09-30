from time import sleep
from picamera import PiCamera, Color 
camera = PiCamera(resolution=((1280, 2048)), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)

camera.start_preview()
camera.annotate_background = Color('yellow')
camera.annotate_foreground = Color('red')
camera.annotate_text_size = 69
# auto white balance (AWB)
# AWB: off, auto, sunlight, cloudy, shade, tungsten, flouorescent, incancedescent, flash, horizon, 

for awb in camera.AWB_MODES:
    camera.awb_mode = awb
    camera.annotate_text = "AWB MODE: %s" % awb
    sleep(3)
camera.stop_preview()

