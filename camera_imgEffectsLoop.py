from time import sleep
from picamera import PiCamera, Color 
camera = PiCamera(resolution=(2048, 1790), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)

camera.start_preview()
camera.annotate_background = Color('yellow')
camera.annotate_foreground = Color('red')
camera.annotate_text_size = 69

# EFFECT: none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, 
#       : saturation, colorswap, washedout, posterize, colorpaint, colorbalance, cartoon, deinterlace1-2

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(2)
camera.stop_preview()