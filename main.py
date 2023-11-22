from cliente import Cliente
from poliza import PolizaSalud, PolizaAutomovil

from funciones import *
import datetime



def main():

    print("""Bienvenido a Saman Seguros""")
    while True:
        option = input ("""Elija una opcion valida:
1. Registrar un Seguro

0. Salir     
--> """)
        
        if option == "1":
            registrar()
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "0":
            break







main()