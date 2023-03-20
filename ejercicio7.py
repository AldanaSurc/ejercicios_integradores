"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
-Un constructor, donde los datos pueden estar vacíos.
-Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
-mostrar(): Muestra los datos de la cuenta.
-ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
-retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""

#Creación de clase
class Cuenta():

#Constructor
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad 

#Getters
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad
    
#Setters
    @titular.setter
    def titular(self,titular):
        self.__titular = titular
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad 

#Mostrar datos de la cuenta
    def mostrar(self):
        print ("El titular de la cuenta es:", self.titular, "y la cantidad total de dinero que hay en la cuenta es:", self.cantidad)

#Ingresar una cantidad a la cuenta, si es negativo no pasa nada.
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
        print("Luego del ingreso la cantidad de dinero total en la cuenta es:", self.__cantidad)

#Retirar una cantidad de la cuenta, puede estar en rojo (tener saldo negativo).
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad
        print("Luego del retiro la cantidad de dinero total en la cuenta es:", self.__cantidad)

#nueva_Cuenta = Cuenta("Aldana", 1000)
#nueva_Cuenta.mostrar()
#nueva_Cuenta.ingresar(cantidad=50)
#nueva_Cuenta.retirar(cantidad=100)

#nueva_Cuenta2 = Cuenta("Jose", 100)
#nueva_Cuenta2.mostrar()
#nueva_Cuenta2.ingresar(cantidad=20)
#nueva_Cuenta2.retirar(cantidad=10)