from time import sleep
from picamera import PiCamera, Color 
camera = PiCamera(resolution=(1260, 895), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)

camera.start_preview()
camera.annotate_background = Color('white')
camera.annotate_foreground = Color('red')
camera.annotate_text_size = 69

# EFFECT: none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, 
#       : saturation, colorswap, washedout, posterize, colorpaint, colorbalance, cartoon, deinterlace1-2

try:
    effectNum = 1
    effectMax = len(camera.IMAGE_EFFECTS)
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = 'Image Effect(' + str(effectNum) + '/' + str(effectMax) + "): " + effect
        camera.annotate_text += '\nResolution: ' + str(camera.resolution)
        effectNum += 1
        sleep(3)
    camera.stop_preview()
except KeyboardInterrupt:
    print ('User interrupted program')