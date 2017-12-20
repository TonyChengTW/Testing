import threading
import time

def t1_job():
  print('T1 start with %s\n' % threading.current_thread)
  for i in range(10):
    time.sleep(0.1)
  print('T1 finish\n')

def t2_job():
  print('T2 start with %s\n' % threading.current_thread)
  for i in range(10):
    time.sleep(0.2)
  print('T2 finish\n')

def main():
  thread_t1 = threading.Thread(target=t1_job, name='T1')
  thread_t2 = threading.Thread(target=t2_job, name='T2')
  thread_t1.start()
  thread_t2.start()
  thread_t1.join()
  print('main thread done\n')

if __name__ == '__main__':
  main()
