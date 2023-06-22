
##El primer módulo debe contener a la clase Clientes


#Clase cliente, con 4 atributos

class Clientes():
    

    def __init__(self, nombre, edad, producto, cantidad):
        self.nombre = nombre
        self.edad = edad
        self.producto = producto
        self.cantidad = cantidad
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "producto": self.producto,
            "cantidad": self.cantidad
        }
        
    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj['nombre'],
            dict_obj['edad'],
            dict_obj['producto'],
            dict_obj['cantidad']
        )
        
    def __str__(self):
        return f"[Nombre: {self.nombre}, Edad: {self.edad}, Producto: {self.producto}, Cantidad: {self.cantidad}]"
