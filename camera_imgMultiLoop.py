from time import sleep
from picamera import PiCamera, Color 
camera = PiCamera(resolution=(640, 512), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)

camera.start_preview()
camera.annotate_background = Color('white')
camera.annotate_foreground = Color('black')
camera.annotate_text_size = 29

# EFFECT: none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, 
#       : saturation, colorswap, washedout, posterize, colorpaint, colorbalance, cartoon, deinterlace1-2
skip_effects = ['gpen','emboss', 'deinterlace1', 'deinterlace2']

# AWB: off, auto, sunlight, cloudy, shade, tungsten, flouorescent, incancedescent, flash, horizon, 
skip_awb = ['off', 'flash']

try:
    effectNum = 1
    awbNum = 1
    effectMax = len(camera.IMAGE_EFFECTS) - len(skip_effects)
    awbMax = len(camera.AWB_MODES) - len(skip_awb)
    for effect in camera.IMAGE_EFFECTS:
        if effect in skip_effects:
            continue
        camera.image_effect = effect
        effect_txt = 'Effect(' + str(effectNum) + '/' + str(effectMax) + "): " + effect
        for awb in camera.AWB_MODES:
            if awb in skip_awb:
                continue
            camera.awb_mode = awb
            awb_txt = '\nAWB(' + str(awbNum) + '/' + str(awbMax) + "): " + awb
            camera.annotate_text = effect_txt + awb_txt
            awbNum += 1
            sleep(2)
        effectNum += 1
        awbNum = 1
    camera.stop_preview()
except KeyboardInterrupt:
    print ('User interrupted program')