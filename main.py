from miTateti import Tablero, Menu

menu = Menu()
menu.imprimir_titulo()
jugadorX, jugadorO = menu.elegir_jugadores()
tablero = Tablero(jugadorX, 
                  jugadorO)

while tablero.jugando():
    # Se imprime el tablero
    tablero.imprimir()

    # El jugador hace su acción y se actualiza el estado del tablero
    jugador = tablero.siguiente_jugador()
    accion = jugador.jugar(tablero)
    tablero.actualizar_estado(accion)

tablero.imprimir()

if tablero.ganador:
    menu.imprimir_texto(f"¡¡LA VICTORIA ES PARA {tablero.ganador.nombre}!!")
else:
    menu.imprimir_texto("¡¡ES UN EMPATE!!")
input("\Pulsa ENTER para terminar")