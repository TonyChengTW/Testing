# output resulting using Queue instead of return()

import threading
import time
from queue import Queue

def job(listing, q):
  for i in range(len(listing)):
    listing[i] = listing[i]**2
  #return listing
  q.put(listing)

def multithreading():
  q = Queue()
  threads = []
  data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
  for i in range(4):
    t = threading.Thread(target=job, args=(data[i], q))
    t.start()
    threads.append(t)

  for thread in threads:
    thread.join()

  results= []

  for _ in range(4):
    results.append(q.get())

  print(results)

if __name__ == '__main__':
  multithreading()
