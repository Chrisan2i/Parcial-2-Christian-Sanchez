class Cliente:
    def __init__(self,id,nombre,apellido,dni,direccion,tlf):
        self.id = id 
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.tlf = tlf

    def show_cliente(self):
        print(f"""
Nombre: {self.nombre}
Apellido: {self.apellido}
Cedula: {self.id}
Direccion: {self.direccion}
Telefono: {self.tlf}""")