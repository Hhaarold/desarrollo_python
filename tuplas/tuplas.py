#coleccion ordenada de elementos la cual es inmutable
tupla = ()#se define con parentesis
tupla = (1,2,3,4,5)#es inmutable
tupla = tupla+(6,)#agregar elemento
print(tupla)
tupla = (1,2,3,4,5,6)
lista = list(tupla)
lista.remove(1)#eliminar elementos
tupla = tuple(lista)
print(tupla)
tupla = (1,2,3,4,5,6)
tupla =()#vaciar tupla
print(tupla)
tupla = (1,2,3,4,5,6)
print(len(tupla))#cantidad de elementos
print(tupla.count(8))
print(tupla.index(3))#imprime la posicion del elemeto dado
tupla = (1,2,3,4,5,6,7)
print(min(tupla))#imprime el minimo
print(max(tupla))#imprime el maximo
print(sum(tupla))#imprime la suma
tupla2 = ("mango","pera","uva")
tupla3 = tupla+tupla2#unir tuplas
print(tupla3)
print(tupla3[6:10])#imprime el numero en la ubicacion determinada
tupla4 = (1,(2,3,4),5)
print(tupla4)
print(tupla4[1][1:3][0])#imprime elementos dentro de elemento
tupla5=tuple("mango")#desenglosa palabras
print(tupla5)