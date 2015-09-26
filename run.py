import subprocess

"""
can have processes communicate with each other via pipes
"""

#subprocess.call(['ls', '-l'], shell=True)
#subprocess.call('echo $HOME', shell=True)
#subprocess.call('echo $$ $BASHPID', shell=True)
#exit_code = subprocess.call('echo $$', shell=True)
subprocess.call(['python', 'other.py'])
