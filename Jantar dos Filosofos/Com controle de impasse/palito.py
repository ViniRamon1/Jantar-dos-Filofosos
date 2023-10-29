
from threading import Semaphore

class Palito:
    def __init__(self):
        self.semaphore = Semaphore(1)  # Inicializa um semáforo com valor 1 (disponível)

    def pegar(self):
        self.semaphore.acquire()

    def soltar(self):
        self.semaphore.release()

