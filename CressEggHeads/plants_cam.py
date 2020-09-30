from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

pdirectory = '/home/pi/Pictures/CressEggHead/'
test = 0
if test:
    print ('test cam')
    # pcam = PiCamera(resolution=(1280, 1024), framerate=30)
    # pcam.start_preview()
    # sleep(5)
    # pcam.capture(pdirectory + 'plants.jpg')
    # pcam.stop_preview()

# EXPOSURE: off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, fireworks
# AWB:      off, auto, sunlight, cloudy, shade, tungsten, flouorescent, incancedescent, flash, horizon
# EFFECT:   none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur,
#       :   saturation, colorswap, washedout, posterize, colorpaint, colorbalance, cartoon, deinterlace1-2

track = 1
if track:
    image_number = 0
    wait_time = 60 * 60 * 0 # 60 sec x 60 mn x H hours
    print ("Wait time is = " + str(wait_time/60) + " minutes")
    n_frames = 1
    try:
        while image_number < n_frames:
            pcam = PiCamera(resolution=(640, 512), framerate=30)
            currentTime = datetime.now()
            timestamp = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}H{0:%M}M".format(currentTime)
            image_name = "plants" + timestamp
            pcam.start_preview()
            sleep(11)
            if currentTime.hour > 17 or currentTime.hour < 7:
                pcam.exposure_mode = 'verylong'
                # pcam.awb_mode = 'auto'
                # pcam.image_effect = 'none'
            else:
                # pcam.exposure_mode = 'verylong'
                pcam.awb_mode = 'sunlight'
                # pcam.image_effect = 'none'
            #pcam.annotate_background = Color('white')
            pcam.annotate_foreground = Color('black')
            pcam.annotate_text_size = 32
            pcam.annotate_text = "Timestamp: %s" % timestamp
            pcam.capture(pdirectory + image_name + '.jpg')
            pcam.stop_preview()
            pcam.close() # allow cam to be used by a different script
            image_number += 1
            print (image_name)
            print ('Number of frames taken : ' + str(image_number))
            sleep(wait_time)
    except KeyboardInterrupt:
        print ('User interrupted program')
