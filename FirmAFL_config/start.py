import subprocess
import time
import os
import shutil
import sys

id=sys.argv[1]

cmdstr ="./run.sh"
subprocess.Popen(cmdstr,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
time.sleep(120)
cmdstr ="python test_%s.py" %id
os.system(cmdstr)
time.sleep(4)
cmdstr ="./user.sh"
os.system(cmdstr)	

