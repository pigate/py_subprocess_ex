import os

def main():
  while True:
    print 'hello ' + str(os.getpid())

if __name__ == '__main__':
  main()
