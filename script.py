'''Modify this file to play Gridmaus by script.'''

import subprocess

PROCESS = subprocess.call(['python.exe', 'main.py'], stdout=subprocess.PIPE)

print(PROCESS)
