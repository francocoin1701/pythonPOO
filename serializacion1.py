import pickle

class Vehiculo():

    def __init__(self,marca,modelo):

        self.marca = marca
        self.modelo = modelo
        self.ensendido = False
        self.acelerar = False
        self.frenar = False

    def ensendidoa(self):
        self.ensendido = True

    def acelerara(self):
        self.acelerar = True

    def frenara(self):
        self.frenar = True

    def estado(self):
        print("marca es: ",self.marca," el modelo es: ", self.modelo," se encuentra ensendido: ", self.ensendido," esta frenando: ",self.frenar," esta acelerando: ",self.acelerar)    

miVehiculo = Vehiculo("renault","323")
suVehiculo = Vehiculo("chanda","porqueria")
elVehiculodeel = Vehiculo("maschanda","masporqueria")


autos = [miVehiculo,suVehiculo,elVehiculodeel]

# para crear un archivo que contenga la lista autos que creamos arriva se hase lo siguiente

fichero = open("losAutos","wb")

pickle.dump(autos,fichero)

fichero.close()
del(fichero)

# para leer el archivo se hase lo siguiente

ficher = open("losAutos","rb")
textoFichero = pickle.load(ficher)
ficher.close()
del(ficher)

# escribimos por pantalla lo que se recupero en la variable textofichero

for i in textoFichero:
    print(i.estado())


