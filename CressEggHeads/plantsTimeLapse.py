import os
import sys
from datetime import datetime
import time

isWindows = sys.platform.startswith('win32')
if not isWindows:
    pdirectory = '/home/pi/Pictures/LivingRoom/'
    vdirectory = '/home/pi/Videos/'
    vid_name = "timelapseLivingRoom_{0:%Y}-{0:%m}-{0:%d}.mp4".format(datetime.now())
    print ('Input Directory: ' + pdirectory)
    os.system('ffmpeg -r 2 -pattern_type glob -i ' + pdirectory + '/\'plants*.jpg\' -c:v libx264 -vf fps=25 -pix_fmt yuv420p ' + vdirectory + vid_name)
else:
    print ('This does not work yet work on Windows')

