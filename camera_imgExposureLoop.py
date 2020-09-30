from time import sleep
from picamera import PiCamera, Color 
camera = PiCamera(resolution=(1280, 1280), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)

camera.start_preview()
camera.annotate_background = Color('yellow')
camera.annotate_foreground = Color('red')
camera.annotate_text_size = 69

# EXPOSURE: off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, fireworks

for exposure in camera.EXPOSURE_MODES:
    camera.exposure_mode = exposure
    camera.annotate_text = "Exposure: %s" % exposure
    sleep(3)
camera.stop_preview()
