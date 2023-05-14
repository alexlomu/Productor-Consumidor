import threading
import queue
import time
import random

q = queue.Queue(maxsize=10)

class Productor(threading.Thread):
    
    def run(self):
        item = 0
        while True and item<50:
            if not q.full():
                item += 1
                q.put(item)
                print(f"Productor produjo la crema {item}")
                time.sleep(random.random())
        time.sleep(1)

class Consumidor(threading.Thread):
    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                print(f"Consumidor compró la crema {item}")
                time.sleep(random.random())
        time.sleep(1)

productor = Productor()
consumidor = Consumidor()

productor.start()
consumidor.start()

productor.join()
consumidor.join()
