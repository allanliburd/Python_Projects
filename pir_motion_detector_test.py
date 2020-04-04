#from gpiozero import MotionSensor
#from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from time import sleep

#pir = MotionSensor(4)
#button = Button(17)
camera = PiCamera(resolution=(1280, 720), framerate=30)
sleep(2)

directory = '/home/pi/Videos/Motion_Detected/'
directory2 = '/home/pi/Pictures/Stop_Motion/'

motion_detect = 0
if motion_detect:
    video_length = 11
    for i in range(2):
        #pir.wait_for_motion()
        print("Motion detected!")
        filename = "motion{0:%Y}-{0:%m}-{0:%d}_{0:%H}{0:%M}{0:%S}".format(datetime.now())
        camera.start_preview()
        camera.start_recording(directory + filename + '.h264')
        #pir.wait_for_no_motion()
        sleep(video_length)
        camera.capture(directory + filename + '.jpg')
        camera.stop_preview()
        camera.stop_recording()

stop_motion = 1
if stop_motion:
    max_frames = 23
    nFrame = 1
    wait_time = 5
    camera.start_preview()
    while (nFrame < max_frames):
        try:
            #button.wait_for_press()
            sleep(wait_time)
            print("Strike a Pose!")
            camera.capture(directory2 + 'frame%03d.jpg' % nFrame)
            nFrame += 1
        except KeyboardInterrupt:
            print ('Program interrupted...')
            break
    camera.stop_preview()
    print ('Done taking multi frames')
# Supposedly, the following commands create a video
# avconv -r 10 -i frame%03d.jpg -qscale 2 animation.h264
# However, ffmpeg is installed and can be used instead
# Subsequently, run the following command to play the video
# omxplayer animation.h264

