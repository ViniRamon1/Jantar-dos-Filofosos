'''
5 filósofos e 5 garfos; é necessário 2 garfos para comer
Deadlock é evitado para nunca esperar um garfo com outro garfo na mão
Se falhar ao pegar o segundo garfo, o primeiro garfo é largado e os garfos são trocados
'''

from filosofo import Filosofo
from palito import Palito
from threading import Thread
import random
import time

def main():
    nomes = ("Monark", "Marco Goleiro", "Leaftime", "Neymar", "Aristoteles")
    palitos = [Palito() for _ in range(5)]
    mesa = [Filosofo(nomes[i], palitos[i], palitos[(i + 1) % 5]) for i in range(5)]

    for filosofo in mesa:
        filosofo.start()

if __name__ == '__main__':
    main()
