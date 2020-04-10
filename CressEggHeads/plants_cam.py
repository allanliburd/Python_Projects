from picamera import PiCamera
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

track = 1
if track:
    image_number = 0
    wait_time = 60 * 60 * 4 # 60 sec x 60 mn x H hours
    print ("Wait time is = " + str(wait_time/60) + " minutes")
    n_frames = 49
    try:
        while image_number < n_frames:
            pcam = PiCamera(resolution=(640, 512), framerate=30)
            image_name = "plants{0:%Y}-{0:%m}-{0:%d}_{0:%H}H{0:%M}M".format(datetime.now())
            pcam.start_preview()
            sleep(1)
            pcam.capture(pdirectory + image_name + '.jpg')
            pcam.stop_preview()
            pcam.close() # allow cam to be used by a different script
            image_number += 1
            print ('Number of frames taken : ' + str(image_number))
            sleep(wait_time)
    except KeyboardInterrupt:
        print ('User interrupted program')
