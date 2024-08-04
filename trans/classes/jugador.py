from trans.classes.nombre import Nombre
from trans.classes.direccion import Direccion
from trans.classes.contacto import Contacto

class Jugador (Nombre, Direccion, Contacto):
    def __init__(self, minombre, apellidos, calle, numero, piso, puerta, ciudad, pais, cp, telefono, email):
        Nombre.__init__(self, minombre, apellidos)
        Direccion.__init__(self, calle, numero, piso, puerta, ciudad, pais, cp)
        Contacto.__init__(self, telefono, email)

    def __str__(self):
        return f' {Nombre.__str__(self)} {Direccion.__str__(self)} {Contacto.__str__(self)}'
    def get_dictionary(self):
        return {
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'calle': self.calle,
            'numero': self.numero,
            'piso': self.piso,
            'puerta': self.puerta,
            'ciudad': self.ciudad,
            'pais': self.pais,
            'cp': self.cp,
            'telefono': self.telefono,
            'email': self.email
            }