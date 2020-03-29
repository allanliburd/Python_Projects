#from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep

#pir = MotionSensor(4)
camera = PiCamera(resolution=(1280, 720), framerate=30)
sleep(2)

directory = '/home/pi/Videos/Detected/'

#while True:
for i in range(2):
    #pir.wait_for_motion()
    print("Motion detected!")
    filename = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}{0:%M}{0:%S}".format(datetime.now())
    camera.start_preview()
    #camera.start_recording(filename)
    #pir.wait_for_no_motion()
    sleep(4)
    camera.capture(directory + filename + '.jpg')
    camera.stop_preview()
    #camera.stop_recording()
    