from piezaTetris import PiezaTetris
import random
class JuegoTetris:

    def __init__(self, colores, formas):
        self.tablero = []
        self.piezaActual = PiezaTetris(random.choice(formas), 
                                       random.choice(colores), 0)
        self.piezaSiguiente = PiezaTetris(random.choice(formas), 
                                          random.choice(colores), 0)
    def crearPieza(self, formas, colores):
        color = random.choice(colores)
        forma = random.choice(formas)
        self.tablero.append(self.piezaActual)
        self.piezaActual = self.piezaSiguiente
        self.piezaSiguiente = self.piezaActual.copy(forma = forma, color= color, posicion= 0)
        print("Nueva pieza creada!!!")
    def rotarPieza(self, opcion):  
        if opcion == '1':
            self.piezaActual.rotarIzquiera()        
        else:
            self.piezaActual.rotarDerecha()                
        print("\nPieza actual: "+self.piezaActual.pintarForma())
    def mainJuego(self, formas, colores):
        sigue = True
        print("\n-----------Inicia el juego.-----------")
        while sigue == True:
            print("\n-----------Menu acciones.-----------")
            print(f"pieza Actual: {self.piezaActual.pintarForma()}")
            print(f"Siguiente Pieza: {self.piezaSiguiente.pintarForma()}")
            print("\nMenú de acciones")
            print("1. Crear Otra pieza.")
            print("2. Rotar pieza. ")
            print("3. Terminar Juego")
            opcion = input("Seleccione una acción: ")
            if opcion == "1":
                self.crearPieza(formas, colores)
            elif opcion == "2":
                while True:
                    print("\n-----------Rotar Pieza.-----------")
                    print("1. Izquierda.")
                    print("2. Derecha.")
                    print("3. Cancelar.")
                    opcion = input("Seleccione una accion: ")
                    if opcion in ['1', '2']:
                        self.rotarPieza(opcion)
                    elif opcion == '3':
                        break
                    else:
                        print("!Opción Invalida.\n")
            elif opcion == '3':            
                break
            else:
                print("Opción Invalida")
        print("Gracias Por Jugar!!")


if __name__== "__main__":
    formas = ["J", "L", "T", "Z", "S", "E", "O"]
    colores =["Rosa", "Roja", "Verde", "Azul", "Morado"]
    juego = JuegoTetris(colores, formas)
    juego.mainJuego(formas, colores) 