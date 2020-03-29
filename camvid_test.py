from picamera import PiCamera
from time import sleep

camera = PiCamera(resolution=(1280, 720), framerate=20)
sleep(2)
camera.awb_mode = 'auto'
camera.exposure_mode = 'backlight'
#camera.rotation = 180
camera.start_preview(alpha=200)
camera.start_recording('/home/pi/Videos/video-2020-03-14.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
