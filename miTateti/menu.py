from .jugador import Humano, Robot

class Menu:
    """
    Clase que se encarga de presentar las opciones al usuario 
    y de recibir sus respuestas

    Métodos:
        imprimir_titulo()
        imprimir_opciones(lista_opciones)
        
    """

    MAX_lENGHT = 80

    def imprimir_titulo(self):
        """
        Imprime el Título del juego
        """

        titulo = """
    -------------       ----      -------------  |--------|   -------------   ---- 
    |           |      /    \     |           |  |    ____|   |           |  |    |
    ----|   |----     /  /\  \    ----|   |----  |   !__      ----|   |----  |    |
        |   |        /  /__\  \       |   |      |    __!         |   |      |    |
        |   |       /   ____   \      |   |      |   !____        |   |      |    |
        |   |      /  /     \   \     |   |      |        |       |   |      |    |
        -----     /__/       \___\    -----      |--------|       |___|      |____|

        """
        print(titulo)


    def imprimir_opciones(self, lista_opciones):
        """
        Imprime una lista de opciones en pantalla
        """
        opciones = "#"*self.MAX_lENGHT + "\n"
        for i, opcion in enumerate(lista_opciones):
            opciones += f"#  {i} . " + opcion + " "*(self.MAX_lENGHT - 8 - len(opcion)) + "#\n"
        opciones += "#"*self.MAX_lENGHT + "\n"
        print(opciones)

    def elegir_opcion(self, lista_opciones):
        """
        regresa el índice de opción ingresada
        """
        # devolver respuesta del usuario
        n_opciones = len(lista_opciones)
        opcion = -1
        while opcion not in list(range(n_opciones)):
            opcion = int(input(f"SELECCIONA UNA OPCIÓN ENTRE 0 y {n_opciones-1}: "))
        return opcion

    def imprimir_texto(self, texto):
        """ 
        Imprime el texto rodeado de numerales : #

        ########################
        #   Texto              #
        ########################

        """
        impresion = "#"*self.MAX_lENGHT + "\n"
        impresion += "#   " + texto + " "*(self.MAX_lENGHT - len(texto) - 5)+ "#\n"
        impresion += "#"*self.MAX_lENGHT + "\n"
        print(impresion)

    def elegir_jugadores(self):
        """
        Imprime en menu de opciones de inicio
        """
        opciones = ["Jugar contra la PC",
                    "Jugar contra la PC [Imposible]",
                    "Dos Jugadores"]
        self.imprimir_opciones(opciones)
        opcion = self.elegir_opcion(opciones)

        if opcion == 0:
            jugadores = Humano(input("Cuál es tu nombre? ")), Robot(False)
        if opcion == 1:
            jugadores = Humano(input("Cuál es tu nombre? ")), Robot(True)
        if opcion == 2:
            jugadores = Humano(input("Nombre del Jugador X: ")), Humano(input("Nombre del Jugador O: "))
        
        self.imprimir_texto("¡COMIENZA EL JUEGO!")
        return jugadores
