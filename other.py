import os
import sys
import signal
import time 
import sys
import os

pid = os.getpid()
received = False

def signal_usr1(signum, frame):
  "Callback invoked when signal received"
  global received
  received = True
  print 'CHILD %6s: Received USR1' % pid 
  sys.stdout.flush()
  sys.exit()


def main():
  print 'CHILD %6s: Setting up signal handler' % pid
  sys.stdout.flush()
  signal.signal(signal.SIGUSR1, signal_usr1)
  while True:
    time.sleep(1) 
    print 'hello %6s' % pid
    sys.stdout.flush()

if __name__ == '__main__':
  main()
