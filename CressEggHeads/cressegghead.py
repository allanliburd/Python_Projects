from picamera import PiCamera
from time import sleep
camera = PiCamera(resolution=((512, 512)), framerate=30)

track = 0
if track:
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Pictures/CressEggHead/image.jpg')
    camera.stop_preview()

    image_number = 0
    try:
        while image_number < 49:
            sleep(3600)
            image_name = '/home/pi/Pictures/CressEggHead/image{0:04d}.jpg'.format(image_number)
            camera.capture(image_name)
            image_number += 1
    except KeyboardInterrupt:
        print ('User interrupted program')
