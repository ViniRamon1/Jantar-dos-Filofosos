from random import seed, random
from time import sleep
from threading import Thread, Lock
from palito import *

class Filosofo(Thread):
    def __init__(self, nome, palito_esquerda, palito_direita):
        Thread.__init__(self)
        self.nome = nome
        self.palito_esquerda = palito_esquerda
        self.palito_direita = palito_direita

    def run(self):
        while True:
            print(f"> {self.nome} está pensando")
            sleep(random(5, 15))
            self.comer()

    def comer(self):
        palito1, palito2 = self.palito_esquerda, self.palito_direita

        palito1.pegar()
        palito2.pegar()

        print(f"> {self.nome} começou a comer")
        sleep(random(0, 2))
        print(f"> {self.nome} parou de comer")

        palito1.soltar()
        palito2.soltar()
