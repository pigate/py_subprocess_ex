import os
import sys
import signal

pid = os.getpid()
received = False

def signal_usr1(signum, frame):
  "Callback invoked when signal received"
  global received
  received = True
  print 'CHILD %6s: Received USR1' % pid 
  sys.stdout.flush()

print 'CHILD %6s: Setting up signal handler' % pid
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)

def main():
  while True:
    print 'hello %6s' % pid 

if __name__ == '__main__':
  main()
