from threading import Lock

class Palito:
    def __init__(self):
        self.trava = Lock()

    def pegar(self):
        self.trava.acquire()

    def soltar(self):
        self.trava.release()
