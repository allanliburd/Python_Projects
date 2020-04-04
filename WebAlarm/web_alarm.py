from time import sleep
import os
import sys
import datetime
import time
import webbrowser
# camera = PiCamera(resolution=((512, 512)), framerate=30)

# camera.start_preview()
# sleep(2)
# camera.capture('/home/pi/Pictures/AlarmClock/image.jpg')
# camera.stop_preview()

def web_open(url):
    print('Opening the following URL : ' + url)
    webbrowser.open_new_tab(url)

def alarm(current_time, alarm_time):
    time_delta = (alarm_time -  current_time).total_seconds()
    if (time_delta < 0):
        return 0
    print ('Need to sleep for ' + str(time_delta))
    time.sleep (time_delta)
    if not isWindows:
        os.system('cvlc --audio --input-repeat 1 --play-and-exit /usr/share/scratch/Media/Sounds/Animal/Crickets.wav')
    print ('Waking up...')
    return 1

isWindows = sys.platform.startswith('win32')
isMacOs = sys.platform.startswith('darwin')
isLinux = sys.platform.startswith('linux')
print ("OS Platform : " + sys.platform)
print ("OS Name : " + os.name)
#os.path.join()
test = 1
if test:
    for hr in range(10, 18, 2):
        now = datetime.datetime.now()
        expTime = datetime.time(hr, 00, 0)
        alarm_time = datetime.datetime.combine(now.date(), expTime)
        print('current time : ' + str(now))
        print('expect alarm @ : ' + str(expTime))
        #print('alarm time : ' + str(alarm_time))
        if alarm (now, alarm_time) == 0:
            if isWindows:
                web_open("F:\github_repos\JavaScript_Projects\\toDo_List\index.html")
            else:
                web_open('/home/pi/projects/JavaScript_Projects/toDo_List/index.html')

