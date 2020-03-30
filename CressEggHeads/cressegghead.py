from picamera import PiCamera
from time import sleep
camera = PiCamera(resolution=((512, 512)), framerate=30)

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Pictures/CressEggHead/image.jpg')
camera.stop_preview()

image_number = 0
while image_number < 49:
    sleep(1800)
    image_name = '/home/pi/Pictures/CressEggHead/image{0:04d}.jpg'.format(image_number)
    camera.capture(image_name)
    image_number += 1