import subprocess

"""
can have processes communicate with each other via pipes
"""

subprocess.call(['ls', '-l'], shell=True)
subprocess.call('echo $HOME', shell=True)
subprocess.call('echo $$ $BASHPID', shell=True)
subprocess.call('echo $$', shell=True)
