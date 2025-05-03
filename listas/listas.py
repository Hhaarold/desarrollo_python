mi_lista_1 = []#primera forma para crear una lista
print (mi_lista_1)
mi_lista_2 = list()#segunda forma para crear una lista
print(mi_lista_2)
mi_lista_1.append(4)#para agragar un solo elemento
print(mi_lista_1)
x = "hola a todos"
mi_lista_1.extend([1, "hola", 0.1, 4, x])#para agregar multiples elementos
print(mi_lista_1)
mi_lista_1.remove("hola")#para quitar elementos de una lista
print(mi_lista_1)
mi_lista_1.pop(0)#quita un elemento de una posicion (sino se especifica elimina el elemento de la ultima posicion)
print(mi_lista_1)
print(len(mi_lista_1))#imprime la logitud de la lista
print(mi_lista_1.index(x))#imprime el elemento especificado
print(mi_lista_1.count(4))#imprime el numero de veces que aparece el elemento especificado
mi_lista_1.sort()#ordena la lista
print(mi_lista_1)
mi_lista_1.reverse#invierte la lista
print(mi_lista_1)
mi_lista_1.clear()#para vaciar una lista
print(mi_lista_1)
print(mi_lista_2)
del mi_lista_2# para borrar una lista
print(type(mi_lista_1))
