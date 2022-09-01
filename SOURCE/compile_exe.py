'''
Script to run the pyinstaller and compile software for specific operating systems
## If build fails chipmunk may need to be built first
 #python setup.py build_chipmunk
'''

#import subprocess

import PyInstaller.__main__
import os

# Set flags true or false to compile different software elements
FULL_GUI = True
COMMAND_LINE = True

directory = os.getcwd()

icon_file =  "Icons\MapMaster_Icon256.ico"
splash_file = directory + "\Icons\MapMaster_Icon_Large.jpg"


def compile():

    return 0


#    '--splash ' + splash_file,
#     '-i ' + icon_file,

#'-p G:\skyrora\python\safety_distance_calculator\source'
#    '-i \source\icon.ico'



PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '-windowed',
    '--clean',
    '-n MapMaster DMs Screen',
    '-i' + icon_file
])

