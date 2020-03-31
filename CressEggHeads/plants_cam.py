from picamera import PiCamera
from time import sleep
#from cressegghead import camera
pcam = PiCamera(resolution=(512, 512), framerate=30, )

pcam.start_preview()
sleep(5)
pcam.capture('/home/pi/Pictures/CressEggHead/plants.jpg')
pcam.stop_preview()

track = 1
if track:
    image_number = 0
    wait_time = 3600
    n_frames = 49
    try:
        while image_number < n_frames:
            sleep(wait_time)
            image_name = '/home/pi/Pictures/CressEggHead/plants{0:04d}.jpg'.format(image_number)
            pcam.capture(image_name)
            image_number += 1
            print ('Number of frames taken : ' + image_number)
    except KeyboardInterrupt:
        print ('User interrupted program')
