import threading

def jobs1():
  global A, lock
  lock.acquire()
  for i in range(10):
    A += 1
    print('job1', A)
  lock.release()

def jobs2():
  global A, lock
  lock.acquire()
  for i in range(10):
    A += 10
    print('job2', A)
  lock.release()


if __name__ == '__main__':
  lock = threading.Lock()
  A = 0
  t1 = threading.Thread(target=jobs1)
  t2 = threading.Thread(target=jobs2)
  t1.start()
  t2.start()
  t1.join()
  t2.join()
