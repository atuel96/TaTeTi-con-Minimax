from random import choice
from .tablero import Tablero



class Jugador:
    """
    Clase base de un jugador, ya sea humano o robot

    Métodos:
        Asignar() : asigna el símbolo del jugador al momento de crear el tablero
        ver_simbolo() : devuelve el símbolo del jugador
    """
    def __init__(self):
        self.simbolo = " "

    def asignar(self, simbolo):
        self.simbolo = simbolo

    def ver_simbolo(self):
        return self.simbolo
    

class Humano(Jugador):
    """
    Un jugador controlado por un Humano
    
    Métodos:
        jugar() Prompt de acción al jugador    
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def jugar(self, tablero):
        """
        Prompt de acción al jugador
        input: El tablero de juego, para ver las acciones disponibles
        output: acción válida en el tablero
        """
        print(f"Es turno de {self.nombre} ({self.ver_simbolo()})!")
        while True:
            ejemplo_accion_1 = choice(tablero.ver_acciones())
            ejemplo_accion_2 = choice(tablero.ver_acciones()).lower()
            accion = input(f"Escribe tu acción (Columna + fila, ej: {ejemplo_accion_1}, {ejemplo_accion_2}): ").capitalize().strip()
            if accion in tablero.ver_acciones():
                return accion
            print("Acción Inválida. Por favor vuelve a intentarlo.")


class Robot(Jugador):
    """
    Jugador Robot

    Métodos:
        jugar(tablero) : realiza una acción válida, aleatoria o utilizando minimax_alg() según la dificultad
        minimax_alg(tablero) : implementación del algoritmo minimax que utiliza dos funciones auxiliares; min_alg() y max_alg()

    """
    def __init__(self, dificultad_imposible = False):
        """
        Robot(dificulatd_imposible : True/False)
        """
        self.nombre = "JugaBot"
        self.dificultad_imposible = dificultad_imposible

    def jugar(self, tablero):
        """
        Realiza una acción válida en función del tablero de juego.

        En modo fácil la acción es aleatoria
        En modo dificil se utiliza algún algoritmo como MinMax [EN PROCESO]
        """

        # Modo fácil es random:
        print(f"Juega {self.nombre}!")
        if not self.dificultad_imposible:
            return choice(tablero.ver_acciones())
    
        # Modo min max, excepto para el primer movimiento:
        if tablero.estado["numero_jugadas"] == 1 :
            return "B2" if "B2" in tablero.estado["lugares_libres"] else "A1"

        return self.minimax_alg(tablero)

        
        # Dificulatd imposible

    def minimax_alg(self, tablero):
        """ 
        Implementación del algoritmo minimax
        Ingresa el tablero y crea tableros virtuales con cada acción posible para elegir la mejor acción
        se utilizan las funciones auxiliares min_alg() y max_alg()
        """
        valores = []
        for accion in tablero.ver_acciones():

            valores.append(max_alg(Tablero(jugador1=tablero.jugadorX,
                                jugador2=tablero.jugadorO,
                                n_jugadas=tablero.estado["numero_jugadas"]+1,
                                lugares_ocupados_X=tablero.estado["lugares_ocupados_X"],
                                lugares_ocupados_O=tablero.estado["lugares_ocupados_O"]+[accion])))
            if valores[-1] == -1:
                return accion
        return tablero.ver_acciones()[valores.index(min(valores))]
                


# Funciones min y max del algoritmo minimax
        
def max_alg(tablero):
    """"
    Evalua el resultado del tablero virtual
    regresa el máximo valor entre -1, 0 y 1
    """

    # si el juego está terminado, se devuelve uno de los valores: 1, 0, -1
    if not tablero.jugando():
        return tablero._verificar_victoria_o_empate()
    
    # sino se vuelve a llamar la función para todos los tableros posibles
    posibilidades = []

    for accion in tablero.ver_acciones():
        posibilidades.append(min_alg(Tablero(tablero.jugadorX,
                                tablero.jugadorO,
                                lugares_ocupados_X=tablero.estado["lugares_ocupados_X"] + [accion],
                                lugares_ocupados_O=tablero.estado["lugares_ocupados_O"],
                                n_jugadas=tablero.estado["numero_jugadas"] + 1)
        ))
    return max(posibilidades)

def min_alg(tablero):
    """"
    Evalua el resultado del tablero virtual
    regresa el mínimo valor entre -1, 0 y 1
    """

    # si el juego está terminado, se devuelve uno de los valores: 1, 0, -1
    if not tablero.jugando():
        return tablero._verificar_victoria_o_empate()
    
    # sino se vuelve a llamar la función para todos los tableros posibles
    posibilidades = []

    for accion in tablero.ver_acciones():
        posibilidades.append(max_alg(Tablero(tablero.jugadorX,
                                tablero.jugadorO,
                                lugares_ocupados_X=tablero.estado["lugares_ocupados_X"],
                                lugares_ocupados_O=tablero.estado["lugares_ocupados_O"]+ [accion],
                                n_jugadas=tablero.estado["numero_jugadas"] + 1)
        ))
    return min(posibilidades)
        
