from threading import Semaphore

class Palito:
    def __init__(self):
        self.semaforo = Semaphore(1)  # Inicialmente, o semáforo permite apenas um filósofo por vez.

    def pegar(self):
        self.semaforo.acquire()

    def soltar(self):
        self.semaforo.release()
