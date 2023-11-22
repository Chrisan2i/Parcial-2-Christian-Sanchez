class Factura:
    def __init__(self,nombre,monto,tipo):
        self.nombre = nombre
        self.monto = monto
        self.tipo = tipo

    def show_factura(self):
        print(f"""
Nombre: {self.nobre}
Monto: {self.monto}
Tipo: {self.tipo}""")

