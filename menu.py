#Codigo que permite importar el Path que se usara para saber la ruta de la base de datos
from pathlib import Path

#Se importan las funciones incluidas en paquete.Manejo_datos
from paquete.Manejo_datos import cargar_datos, mostrar_datos, introducir_datos, direccionar_programa, continuar_programa

#Direccion de la base de datos y nombre a darle
BASE_DIR = Path(__file__).resolve().parent
RUTA_BASE_DATOS = BASE_DIR / "base_de_datos.json"

#Funcion principal que conecta la clase, atributos y funciones incluidas en paquete
def main():
    if direccionar_programa():
        print("*******************************")
        base_datos = cargar_datos(RUTA_BASE_DATOS)
        if isinstance(base_datos, list):
            introducir_datos(RUTA_BASE_DATOS, base_datos)
            print("***************************")
            print("Los registros hasta ahora son:")
            mostrar_datos(base_datos)
            print("***************************")
            if continuar_programa() == True:
                main()
            else:
                #print("*******************************")
                #print ("Se cerro el programa")
                #print("*******************************")
                return
                   

#Se ejecuta la funcion main que devolvera el programa
main()