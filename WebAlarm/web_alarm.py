from picamera import PiCamera
from time import sleep
import os
import datetime
import time
import webbrowser
# camera = PiCamera(resolution=((512, 512)), framerate=30)

# camera.start_preview()
# sleep(2)
# camera.capture('/home/pi/Pictures/AlarmClock/image.jpg')
# camera.stop_preview()

def web_oepn(url):
    print('Opening the following URL : ' + url)
    webbrowser.open_new_tab(url)

def alarm(current_time, alarm_time):
    time_delta = (alarm_time -  current_time).total_seconds()
    if (time_delta < 0):
        return 0
    print ('Need to sleep for ' + str(time_delta))
    time.sleep (time_delta)
    os.system('cvlc --audio --input-repeat 1 --play-and-exit /usr/share/scratch/Media/Sounds/Animal/Crickets.wav')
    print ('Waking up...')
    return 1

test = 1
if test:
    for hr in range(10, 18, 2):
        now = datetime.datetime.now()
        expTime = datetime.time(hr, 00, 0)
        alarm_time = datetime.datetime.combine(now.date(), expTime)
        print('current time : ' + str(now))
        print('expect alarm @ : ' + str(expTime))
        #print('alarm time : ' + str(alarm_time))
        if alarm (now, alarm_time):
            web_oepn('/home/pi/projects/JavaScript_Projects/toDo_List/index.html')

