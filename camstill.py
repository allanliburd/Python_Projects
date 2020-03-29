from time import sleep
from picamera import PiCamera, Color 
camera = PiCamera(resolution=(1280, 720), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)
# off,auto,sun,cloud,shade,tungsten,fluorescent,incandescent,flash,horizon,greyworld
camera.awb_mode = 'fluorescent'
# off,auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks
camera.exposure_mode = 'night'
# Finally, take several photos with the fixed settings
#camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])

# By default, the image resolution is set to the resolution of your monitor.
# The maximum resolution is 2592×1944 for still photos, and 1920×1080 for video recording.
camera.resolution = (2048, 1790)
camera.framerate = 15
camera.start_preview()
camera.annotate_background = Color('yellow')
camera.annotate_foreground = Color('blue')
camera.annotate_text = "Hello home!"
camera.annotate_text_size = 69
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(2)
# The default brightness is 50, and you can set it to any value between 0 and 100.
#camera.brightness = 70
#camera.capture('/home/pi/Pictures/max2.jpg')
camera.stop_preview()