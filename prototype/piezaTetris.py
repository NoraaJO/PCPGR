from prototype import prototype

class PiezaTetris(prototype):
    """Clase Principal de objecto pieza"""
    def __init__(self, forma, color, posicion):
        self.forma = forma
        self.color = color
        self.posicion = posicion


    def rotarIzquiera(self):
        
        if self.posicion + 90 == 360:
            self.posicion = 0
        else:
            self.posicion += 90

    def rotarDerecha(self):
        
        if self.posicion - 90 == -90:
            self.posicion = 270
        else:
            self.posicion -= 90

    def pintarForma(self):

        return f"Forma: {self.forma}, Color: {self.color}"
 
    
