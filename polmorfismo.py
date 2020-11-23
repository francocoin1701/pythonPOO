class Auto():
    def desplazamiento(self):
        print("se desplaza con 4 ruedas")

class Camion():
    def desplazamiento(self):
        print("se desplaza con seis ruedas")

class moto():
    def desplazamiento(self):
        print("se desplaza con dos ruedas")


def desplazamientonVehiculo(vehiculo):
    vehiculo.desplazamiento()                        


miVehiculo = moto()

desplazamientonVehiculo(miVehiculo)