#El segundo módulo debe crear instancias de Clientes.

import json

#Se importa la clase clientes

from .Usuarios import Clientes

def direccionar_programa():
    decision = input("Ingrese (I) para empezar el programa o (S) para salir: ").capitalize()
    if decision == "I":
        print("Se empezara el programa!")
        return True
    elif decision == "S":
        return False
    else:
        print("Se ingreso un valor invalido, vuelva a intentar")
        return direccionar_programa()

#Funcion que solicita el ingreso de datos
def introducir_datos(RUTA_BASE_DATOS, base_datos):
    #usuarios = {}
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    producto = input("Producto a comprar: ")
    cantidad = input("Cantidad a comprar: ")
    nuevo_cliente = Clientes(nombre,edad,producto,cantidad)
    print("Se realizo el registro con exito")
    base_datos.append(nuevo_cliente)
    guardar_datos(RUTA_BASE_DATOS, base_datos)

#Funcion que guarda los datos ingresados en un archivo json
def guardar_datos(RUTA_BASE_DATOS, base_datos:list):
    datos_serializados = [cliente.to_dict() for cliente in base_datos]
    with open(RUTA_BASE_DATOS, "w") as archivo:
        json.dump(datos_serializados, archivo, indent=4)
    return print("Se guardo la informacion del cliente en la base de datos")

#Funcion que verifica si la base de ya datos existe, carga los datos si es asi. De lo contrario solo devuelve una base de datos vacia
def cargar_datos(RUTA_BASE_DATOS):
    base_datos = []
    try:
        with open(RUTA_BASE_DATOS, "r") as archivo:
            base_datos_json = json.load(archivo)
            base_datos = [Clientes.from_dict(cliente) for cliente in base_datos_json]
    except json.decoder.JSONDecodeError:
        print("El archivo existe pero esta danado")
    except FileNotFoundError:
        print("El archivo no existe, no se cargan datos")
    return base_datos

#funcion que muestra los datos presentes en la base de datos hasta el momento
def mostrar_datos(base_datos):
    for cliente in base_datos:
        print(cliente)
    print()
    
def continuar_programa():
    continuar = input("Ingrese (Y) si desea continuar el programa o (N) en caso contrario:").capitalize()
    if continuar == "Y":
        print("*******************************")
        print("Se continuara con el programa!")
        print("*******************************")
        return True
    elif continuar == "N":
        print("*******************************")
        print ("Se cerro el programa")
        print("*******************************")
        return False
    else:
        print("*******************************")
        print("Respuesta invalida, se cierra el programa")
        print("*******************************")
        return False