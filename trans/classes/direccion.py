class Direccion:
    def __init__(self, calle, numero, piso, puerta, ciudad, pais, cp):
        self.calle = calle
        self.numero = numero
        self.piso = piso
        self.puerta = puerta
        self.ciudad = ciudad
        self.pais = pais
        self.cp = cp

    def __str__(self):
        return f'{self.calle} {self.numero}, {self.piso} {self.puerta},{self.cp}, {self.ciudad}{self.pais}'