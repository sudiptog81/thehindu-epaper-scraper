import os
import glob
from time import sleep
from datetime import datetime
date = str(datetime.today().strftime('%d-%m-%Y'))
dir_name = '/media/volume-extra/theHindu/' + date
os.chdir(dir_name)
sleep(10)
files = glob.glob("*.pdf")
files.sort(key=os.path.getmtime)
filename = str(files[0])
command = 'mega-put \'' + dir_name + '/' + filename + '\'' + \
    ' \'/The Hindu ePaper/' + date + '/' + filename+ '\'' + ' -c'
os.system(command)
sleep(10)
command = 'rm \'' + dir_name + '\' -r'
os.system(command)

