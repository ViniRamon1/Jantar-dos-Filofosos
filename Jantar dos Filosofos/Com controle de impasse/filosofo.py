from random import seed, random
from time import sleep
from threading import Thread, Lock
from palito import *

class Filosofo(Thread):
    def __init__(self, nome, garfo_esquerda, garfo_direita, semaforo_controle):
        Thread.__init__(self)
        self.nome = nome
        self.garfo_esquerda = garfo_esquerda
        self.garfo_direita = garfo_direita
        self.semaforo_controle = semaforo_controle 

    def run(self):
        while True:
            print(f"{self.nome} está meditando")
            sleep(random(0, 2))
            self.comer()

    def comer(self):
        garfo1, garfo2 = self.garfo_esquerda, self.garfo_direita

        with self.semaforo_controle:
            garfo1.pegar()
            garfo2.pegar()

            print(f"{self.nome} está comendo")
            sleep(random(0, 2))
            print(f"{self.nome} terminou de comer")

            garfo2.soltar()
            garfo1.soltar()


