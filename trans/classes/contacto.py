class Contacto:
    def __init__(self, email, telefono):
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"Email: {self.email}, Telefono: {self.telefono}"
