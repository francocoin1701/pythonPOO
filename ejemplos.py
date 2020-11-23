class Auto():
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__andando = False

    def arrancar(self, arranca):
        self.__andando = arranca
        if(self.__andando):
            print("el carro esta en movimiento")
        else:
            print("el carro esta parado")         

    def estado(self):
        if(self.__andando):
            print("el auto tiene", self.__ruedas,"ruedas, un ancho",self.__ancho," y un largo de ",self.__largo)
miCarro = Auto()
miCarro.arrancar(True)
miCarro.estado()