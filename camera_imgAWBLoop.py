from time import sleep
from picamera import PiCamera, Color 
camera = PiCamera(resolution=(1260, 895))
# Wait for the automatic gain control to settle
sleep(2)

camera.start_preview()
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('white')
camera.annotate_text_size = 69
# auto white balance (AWB)
# AWB: off, auto, sunlight, cloudy, shade, tungsten, flouorescent, incancedescent, flash, horizon, 

try:
    awbNum = 1
    awbMax = len(camera.AWB_MODES)
    for awb in camera.AWB_MODES:
        camera.awb_mode = awb
        camera.annotate_text = 'AWB MODE(' + str(awbNum) + '/' + str(awbMax) + "): " + awb
        camera.annotate_text += '\nResolution: ' + str(camera.resolution)
        awbNum += 1
        sleep(3)
    camera.stop_preview()
except KeyboardInterrupt:
    print ('User interrupted program')
