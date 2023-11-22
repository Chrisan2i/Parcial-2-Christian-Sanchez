class Poliza:
    def __init__(self,id_poliza,tipo_c,monto,fecha_i,fecha_v):
        self.id_poliza = id_poliza
        self.tipo_c = tipo_c
        self.monto = monto
        self.fecha_i = fecha_i
        self.fecha_v = fecha_v

    def show_poliza(self):
        pass

class PolizaSalud(Poliza):
    def __init__(self, id_poliza, monto, fecha_i, fecha_v,personas):
        super().__init__(id_poliza, "salud", monto, fecha_i, fecha_v)
        self.personas = personas

    def show_poliza(self):
        pass

class PolizaAutomovil(Poliza):
    def __init__(self, id_poliza, monto, fecha_i, fecha_v,tipo_vehiculo):
        super().__init__(id_poliza, "automovil", monto, fecha_i, fecha_v)
        self.tipo_vehiculo = tipo_vehiculo





