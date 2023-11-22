from cliente import Cliente
from poliza import PolizaSalud,PolizaAutomovil
from factura import Factura
import datetime


def date_base():
    db = {
        "clientes":[],
        "poliza":[]
    }
    return db

def registrar():
    db = date_base() 
    

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input ("Ingrese su cedula: ")
    direccion = input("Ingrese su direccion: ")
    tlf = input ("Ingrese su telefono: ")

    
    Registro_poliza(db,nombre,apellido,dni,direccion,tlf)

def Registro_poliza(db,nombre,apellido,dni,direccion,tlf):
    cont= 0
    while True:
        tipo_poliza = ("""Que poliza desea: 
1. Salud
2. Automovil

0 Ninguna
--> """)
        if tipo_poliza == "1":
            polizaSalud(db,1,nombre,apellido,dni,direccion,tlf)
            cont +=1
        elif tipo_poliza == "2":
            polizaAutomovil(db,1,nombre,apellido,dni,direccion,tlf)
            cont+=1
        elif tipo_poliza == "3":
            pass

        elif tipo_poliza == "4":
            break
    if cont >= 2:
        print()

def polizaSalud(db,id,nombre,apellido,dni,direccion,tlf):
    personas = []
    cont = 0
    mont=[]
    while True:
        personas = int(input ("Cuantas personas desea agregar: "))
        if personas != 0:
            while cont == personas:
                for i in range(personas+1):
                    edad = input(f"Cuantos años tiene la persona {i+1}: ")
                    personas.append(edad)
                    cont+=1

        if cont != 0:
            for p in personas:
                if p < 10:
                    mont.append(20)
                    
                elif p > 10 and p < 21:
                    mont.append(30)
                
                elif p > 20 and p < 41 :
                    mont.append(50)
                    
                elif p > 40 :
                    mont.append(70)
                    

            date=datetime.datetime.now()
            datef=datetime.datetime.year()

            

            factura=Factura(nombre,sum(mont), "Poliza de Salud")
            
            print("Factura")
            factura.show_factura()
            option = input("""desea pagar: 
1. Si
2. NO""")
            if option == "1":
                db["clientes"].append(Cliente(id, nombre, apellido, dni, direccion,tlf))
                db["poliza"].append(PolizaSalud(1,100,str(date),str(datef)))
                print("gracias por su compra")

            elif option == "2":
                break

def polizaAutomovil(db,id,nombre,apellido,dni,direccion,tlf):
    mont=[]
    while True:
        tipo_v=input("""Que vehiculo desea asegurar:
1. Moto
2. Carro
3. Camioneta

0. Solo eso                   
--> """)
        
        if tipo_v == "1":
            mont.append(15)
        elif tipo_v == "2":
            mont.append(20)
        elif tipo_v == "2":
            mont.append(30)

        date=datetime.datetime.now()
        datef=datetime.datetime.year()

            

        factura=Factura(nombre,sum(mont), "Poliza de Automovil")
            
        print("Factura")
        factura.show_factura()
        option = input("""desea pagar: 
1. Si
2. NO""")
        if option == "1":
            db["clientes"].append(Cliente(id, nombre, apellido, dni, direccion,tlf))
            db["poliza"].append(PolizaSalud(1,100,str(date),str(datef)))
            print("gracias por su compra")

        elif option == "2":
            break

        
            
        


    

        

                







            


    