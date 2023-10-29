---
---

# Jantar dos Filósofos

Este é um exemplo de implementação do clássico problema dos "Filósofos Jantando" em Python. O problema envolve cinco filósofos que compartilham uma mesa redonda com cinco garfos. Cada filósofo precisa de dois garfos para comer e, para evitar impasses, eles devem adquirir os garfos de forma inteligente. Nesta implementação, demonstraremos como evitar o impasse e garantir que os filósofos possam comer de forma eficaz.

## Arquivos

1. **jantar.py**: Este arquivo contém o código principal que simula o jantar dos filósofos. Ele cria cinco filósofos com nomes fictícios e os coloca em uma mesa com cinco garfos. Os filósofos alternam entre pensar e comer. O código também lida com a execução dos filósofos em threads e garante que eles não entrem em deadlock.

2. **filosofo.py**: Este arquivo define a classe Filósofo, que estende a classe Thread do Python. Cada filósofo é uma thread que executa as ações de pensar e comer. O método `comer` é onde a lógica de aquisição e liberação de garfos é implementada, evitando impasses.

3. **palito.py**: Este arquivo contém a implementação da classe Palito (ou garfo). Os palitos são os recursos compartilhados entre os filósofos, e esta classe define como eles são adquiridos e liberados.

## Como Funciona

O algoritmo implementa uma solução para evitar deadlock, permitindo que um filósofo desista de pegar um garfo se não conseguir pegar ambos os garfos em um determinado período. O código também define intervalos de tempo aleatórios para pensar e comer, tornando a simulação mais realista.

## Implementações

### Implementação sem controle de impasse

Nesta implementação, os filósofos simplesmente tentam pegar os palitos (garfos) um de cada vez, sem verificar se outros filósofos estão tentando pegar os mesmos palitos ao mesmo tempo. Isso pode levar a um impasse, onde todos os filósofos tentam pegar o mesmo palito simultaneamente. Não há mecanismos para evitar ou detectar deadlock nesta abordagem.

### Implementação com controle de impasse

Nesta implementação, foi introduzido um mecanismo para evitar impasses. Cada palito (garfo) é representado por um objeto de semáforo que permite a aquisição por um número limitado de filósofos de cada vez. Isso evita que vários filósofos tentem pegar o mesmo palito simultaneamente e ajuda a evitar impasses.

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


---
