import pickle

# creamos un fichero con una lista de nombres

lista_nombres = ["pedro","sorangel","patricia","lina"]

fichero_binario = open("lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()
del(fichero_binario)

# leemos el fichero con la lista de nombres que se encuentra en codigo binario pues esta serializado

fichero_binario = open("lista_nombres", "rb")

fichero_binario1 = pickle.load(fichero_binario)

fichero_binario.close()
del(fichero_binario)

print(fichero_binario1)
