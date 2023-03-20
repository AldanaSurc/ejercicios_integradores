"""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
- Un constructor.
- Los setters y getters para el nuevo atributo.
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
- Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta."""

from ejercicio7 import Cuenta

#Creamos la nueva clase que heredará de Cuenta
class CuentaJoven(Cuenta):

#Constructor
    def __init__(self, titular, cantidad=0, bonificacion=0, edad=""):
        super().__init__(titular,cantidad) #Llamo a la clase padre
        self.bonificacion = bonificacion
        self.edad = edad

#Getters (para los nuevos atributos, lo demás lo heredé de la clase padre)
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @property
    def edad(self):
        return self.__edad

#Setters (para los nuevos atributos, lo demás lo heredé de la clase padre)
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    @edad.setter
    def edad(self,edad):
        self.__edad = edad

#Mostrar datos CuentaJoven 

    def mostrar(self):
        print("Cuenta joven -->", "El titular de la cuenta es:", self.titular, ", la cantidad total de dinero que hay en la cuenta es:", self.cantidad, "y la bonificacion recibida es del", self.bonificacion, "%")

#Chequear si 18<edad<25, solo así puede tener una CuentaJoven 

    def es_titular_valido(self,edad):
        if (edad>=18) and (edad<25):
            print("La persona puede ser titular de una CuentaJoven")
        else:
            print("La persona no puede ser titular de una CuentaJoven")

#Retirar dinero solo si la persona puede ser titular de CuentaJoven
    def retirar(self,edad, cantidad):
        if (edad>=18) and (edad<25):
            cantidad > 0
            super().retirar(cantidad)
        else:
            print("La persona no puede retirar dinero porque no es titular de CuentaJoven")


#nueva_CuentaJoven = CuentaJoven("Aldana", 400, 10)
#nueva_CuentaJoven.mostrar()
#nueva_CuentaJoven.es_titular_valido(edad=18)
#nueva_CuentaJoven.retirar(edad=18,cantidad=200)