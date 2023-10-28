---

# Jantar dos Filósofos

Este é um exemplo de implementação do clássico problema dos "Filósofos Jantando" em Python. O problema envolve cinco filósofos que compartilham uma mesa redonda com cinco garfos. Cada filósofo precisa de dois garfos para comer e, para evitar impasses, eles devem adquirir os garfos de forma inteligente. Nesta implementação, demonstraremos como evitar o impasse e garantir que os filósofos possam comer de forma eficaz.

## Arquivos

1. **jantar.py**: Este arquivo contém o código principal que simula o jantar dos filósofos. Ele cria cinco filósofos com nomes fictícios e os coloca em uma mesa com cinco garfos. Os filósofos alternam entre pensar e comer. O código também lida com a execução dos filósofos em threads e garante que eles não entrem em deadlock.

2. **filosofo.py**: Este arquivo define a classe Filósofo, que estende a classe Thread do Python. Cada filósofo é uma thread que executa as ações de pensar e comer. O método `comer` é onde a lógica de aquisição e liberação de garfos é implementada, evitando impasses.

## Como Funciona

O algoritmo implementa uma solução para evitar deadlock, permitindo que um filósofo desista de pegar um garfo se não conseguir pegar ambos os garfos em um determinado período. O código também define intervalos de tempo aleatórios para pensar e comer, tornando a simulação mais realista.

## Execução

Para executar a simulação do jantar dos filósofos, siga estas etapas:

1. Certifique-se de ter Python instalado no seu sistema.

2. Execute o arquivo "jantar.py". Isso iniciará a simulação com os cinco filósofos.

    ```bash
    python jantar.py
    ```

## Observações

Esta implementação é uma simplificação do problema e não aborda todos os cenários possíveis. Implementações mais robustas podem ser desenvolvidas para lidar com casos mais complexos, como a prevenção de impasses em um ambiente mais realista.

---
