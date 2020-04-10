from picamera import PiCamera
from time import sleep

track = 1
if track:

    image_number = 0
    wait_time = 60 * 60 * 1
    print ("Wait time is = " + str(wait_time/60) + " minutes")
    n_frames = 50
    try:
        while image_number < n_frames:
            camera = PiCamera(resolution=((512, 512)), framerate=30)
            camera.start_preview()
            sleep(1)
            image_name = '/home/pi/Pictures/CressEggHead/image{0:04d}.jpg'.format(image_number)
            camera.capture(image_name)
            camera.stop_preview()
            camera.close() # allow cam to be used by a different script
            image_number += 1
            print ('Number of frames taken : ' + str(image_number))
            sleep(wait_time)
    except KeyboardInterrupt:
        print ('User interrupted program')
