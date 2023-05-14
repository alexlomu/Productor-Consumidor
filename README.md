# Productor-Consumidor
El link al repositorio es el siguiente: [GitHub](https://github.com/alexlomu/Productor-Consumidor)
Hemos creao un código que ressuelve el problema del prouctor-consumidor.
El código propuesto es el siguiente:

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
    
El output recibido es el siguiente:

    Productor produjo la crema 1
    Consumidor compró la crema 1
    Productor produjo la crema 2Consumidor compró la crema 2

    Productor produjo la crema 3
    Productor produjo la crema 4
    Consumidor compró la crema 3
    Productor produjo la crema 5
    Consumidor compró la crema 4
    Consumidor compró la crema 5
    Productor produjo la crema 6Consumidor compró la crema 6

    Productor produjo la crema 7Consumidor compró la crema 7

    Productor produjo la crema 8
    Consumidor compró la crema 8
    Productor produjo la crema 9
    Productor produjo la crema 10
    Consumidor compró la crema 9
    Consumidor compró la crema 10
    Productor produjo la crema 11
    Productor produjo la crema 12
    Consumidor compró la crema 11
    Consumidor compró la crema 12
    .
    .
    .
    Productor produjó la crema 50
    Consumidor compró la crema 50
