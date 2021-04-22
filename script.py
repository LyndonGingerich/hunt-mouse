'''Modify this file to play Gridmaus by script.'''

import subprocess

PROCESS = subprocess.run(['python.exe', 'main.py'], stin=subprocess.PIPE, capture_output=True)

print(PROCESS)
