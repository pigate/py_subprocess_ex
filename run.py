import subprocess
import sys
import time
import os
import signal

"""
can have processes communicate with each other via pipes
"""

#subprocess.call(['ls', '-l'], shell=True)
#subprocess.call('echo $HOME', shell=True)
#subprocess.call('echo $$ $BASHPID', shell=True)
#exit_code = subprocess.call('echo $$', shell=True)
proc = subprocess.Popen(['python', 'other.py'])
time.sleep(5)
print 'PARENT	: Signaling child'
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)

