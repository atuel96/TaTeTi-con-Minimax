class Tablero:
    """
    Clase dedicada a las funcionalidades del tablero.
    
    Inicialiar tablero: Tablero(jugador1, jugador2)

    Atributos:
        jugadorX : jugador1
        jugadorO : jugador2
        estado : diccionario con "lugares_libres", "lugares_ocupados_X", "lugares_ocupados_O", "numero_jugadas" y "juego_en_curso".
        ganador : None / jugador ganador

    Métodos:
        imprimir() : imprime el estado actual del tablero.
        actualizar_estado(accion)  : actualiza el estado del tablero.
        ver_acciones()  : muestra las acciones posibles para el estado actual del tablero.
        posible_victoria() : devuelve True or False en función de si aún es posible una victoria.
        sigiente_jugador()  : devuelve el jugador que jugará a continuación.
        jugando() : devuelve True or False en función de si el juego terminó o no.
        _verificar_victoria_o_empate()   : verifica si el juego llegó a un final y cual es el resultado.
    """

    COLUMNS = ["A", "B", "C"]
    ROWS = ["1", "2", "3"]

    def __init__(self, 
                jugador1,
                jugador2, 
                lugares_ocupados_X = [], 
                lugares_ocupados_O = [],
                n_jugadas = 0):
        """
        Inicializar jugadores.
        Un tablero solo puede crearse si hay dos jugadores presentes.
        """
        self.jugadorX = jugador1
        self.jugadorX.asignar("X")
        self.jugadorO = jugador2
        self.jugadorO.asignar("O")
        self.estado = {"lugares_libres" : [column + row for column in self.COLUMNS for row in self.ROWS],
                       "lugares_ocupados_X" : lugares_ocupados_X,
                       "lugares_ocupados_O" : lugares_ocupados_O,
                       "numero_jugadas" : n_jugadas,
                       "juego_en_curso" : True}
        self.estado["lugares_libres"] = [column + row for column in self.COLUMNS for row in self.ROWS
                                         if column + row not in lugares_ocupados_O + lugares_ocupados_X]
        
        self.ganador = None




    def imprimir(self):
        """
        Imprime el tablero en el estado actual. Ejemplo:
             
             A   B   C  
           #############
         1 # O | X | O #
           # ......... #
         2 #   | O |   #
           #.......... #
         3 #   | X | X #
           #############
        
        """
        tablero  = "     A   B   C  \n"
        tablero += "   #############\n" 

        for row in self.ROWS:
            row_symbols = []
            for col in self.COLUMNS:
                current_position = col + row
                if current_position in self.estado["lugares_ocupados_X"]:
                    row_symbols.append("X")
                    continue
                if current_position in self.estado["lugares_ocupados_O"]:
                    row_symbols.append("O")
                    continue
                row_symbols.append(" ")
            tablero += f" {row} # {row_symbols[0]} | {row_symbols[1]} | {row_symbols[2]} #\n"
            if row != 3:
                tablero += "   #.......... #\n"
        tablero += "   #############\n" 

        print(tablero)


    def actualizar_estado(self, accion):
        """
        Dada una acción válida, se actualiza el estado
        """

        if accion not in self.estado["lugares_libres"]:
            raise ValueError("Accion Inválida, prueba una acción válida o una que esté desocupada")
        
        simbolo = self.siguiente_jugador().ver_simbolo()
        if simbolo == "X":
            self.estado["lugares_ocupados_X"].append(accion)
        elif simbolo == "O":
            self.estado["lugares_ocupados_O"].append(accion)

        self.estado["lugares_libres"].remove(accion)
        self.estado["numero_jugadas"] += 1

        # verificar si el juego terminó
        self.jugando()

    def ver_acciones(self):
        """
        Devuelve la lista de acciones válidas en forma de lista.
        """
        return self.estado["lugares_libres"]
    
    def posible_victoria(self):
        """
        [función en consturcción, por el momento el resutlado es provisorio]
        Devuelve True/False
        """
        #return True
        return False if len(self.estado["lugares_libres"]) == 0 else True    

    def siguiente_jugador(self):
        """
        Devuelve 'X' o 'O' según el turno, utilizando el número de jugadas (X siempre va primero).
        """
        if self.estado["numero_jugadas"] % 2 == 0:
            return self.jugadorX
        else:
            return self.jugadorO
    
    def jugando(self):
        """
        Verifica si el juego sigue en curso
        Devuelve True si el juego sigue en curso, de lo contrario False.
        """       
        victoria_o_empate = self._verificar_victoria_o_empate()
        # Si hay victoria
        if victoria_o_empate != 0:
            self.estado["juego_en_curso"] = False
            if victoria_o_empate == 1:
                self.ganador = self.jugadorX
            elif victoria_o_empate == -1:
                self.ganador = self.jugadorO        
        # Si hay empate
        if self._verificar_victoria_o_empate() == 0 and not self.posible_victoria():
            self.estado["juego_en_curso"] = False

        return self.estado["juego_en_curso"]

    def _verificar_victoria_o_empate(self):
        """"
        Devuelve
        1  : Victoria de X
        0  : Empate o juego continua
        -1 : Victoria de O
        """
        matriz_estado = [[0, 0, 0] for _ in range(3)]
        for i, row in enumerate(self.ROWS):
            for j, col in enumerate(self.COLUMNS):
                if col+row in self.estado["lugares_ocupados_X"]:
                    matriz_estado[i][j] = 1
                    continue
                if col+row in self.estado["lugares_ocupados_O"]:
                    matriz_estado[i][j] = -1
                    
        # Victoria en filas:
        for row in matriz_estado:
            if sum(row) == 3:
                return 1
            if sum(row) == -3:
                return -1
            
        # Victoria en columnas:
        for col in range(3):
            if sum(matriz_estado[i][col] for i in range(3)) == 3:
                return 1
            if sum(matriz_estado[i][col] for i in range(3)) == -3:
                return -1
            
        # Victoria en Diagonal \:
        if sum([matriz_estado[i][i] for i in range(3)]) == 3:
            return 1
        if sum([matriz_estado[i][i] for i in range(3)]) == -3:
            return -1
        
        # Victoria en Diagonal /:
        if sum([matriz_estado[i][j] for i, j in zip(range(3), range(2,-1,-1))]) == 3:
            return 1
        if sum([matriz_estado[i][j] for i, j in zip(range(3), range(2,-1,-1))]) == -3:
            return -1
        
        # empate
        return 0
        
        

    