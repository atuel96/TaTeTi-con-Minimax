# TaTeTi con Algoritmo Minimax

Este repositorio contiene una implementación del juego TaTeTi utilizando el algoritmo [minimax](https://es.wikipedia.org/wiki/Minimax). El objetivo de este proyecto fue probar el algoritmo [minimax](https://es.wikipedia.org/wiki/Minimax) para crear una inteligencia artificial capaz de jugar TaTeTi de manera óptima.


![Menu de Inicio](https://github.com/atuel96/TaTeTi-con-Minimax/blob/main/imagenes/inicio.png)

Para una explicación sencilla del algoritmo se recomienda mucho ver [este video](https://youtu.be/D5aJNFWsWew?t=4321), del curso CS50 ofrecido por la univerdad de Harvard.

## Modo de Uso

Clonar este repositorio

```bash
git clone https://github.com/atuel96/TaTeTi-con-Minimax.git
```
o descargarlo.

* Requisitos: Python 3.6 en adelante, sin necesidad de librerias _third party_.

Una vez descargado, ejecutar `main.py`:

```bash
python main.py
```

## Cómo Jugar

### Notas sobre la implementación de Minimax

El algortimo minimax garantiza una solución óptima, pero escala exponencialmente en complejidad al agregar posibles estados. Por esta razón solo se implementó el algoritmo desde el segundo movimiento de la IA (su primer movimiento está _hardcodeado_ usando un _if statement_ de forma que sea óptimo).