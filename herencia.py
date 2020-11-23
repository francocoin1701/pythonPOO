class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancar = False
        self.frenar = False
        self.accelerar = False

    def arranca(self):
        self.arrancar = True

    def frenar(self):
        self.frenar = True

    def accelerar(self):
        self.accelerar = True

    def estado(self):
        print("todas las estupideses del estado")                 

class Moto(Vehiculo):
   
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "haciendo el caballito care verga"
        
    def estado(self):
        print("todas las estupideses del estado", self.hcaballito)


class Furgon(Vehiculo):
    def cargado(self, carga):
        self.cargando = carga
        if (self.cargando):
            return "el furgon esta cargando"
        else:
            return "el furgon esta vacio"    

class VElectrico(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    def carga(self):
        self.cargado = True


miMoto = Moto("yamaha","2018")
miMoto.caballito()
miMoto.estado()

miFurgon = Furgon("renault", "caterpila")
miFurgon.arranca()
miFurgon.estado()
print(miFurgon.cargado(True))

class biciElectri(VElectrico, Vehiculo):
    pass

biciEl = biciElectri("lumisolar", "spring")
biciEl.estado()