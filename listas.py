"""este es un espacio para hablar de listas"""
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]#meses del año
print(meses)#imprimo los meses del año
print(meses[0])#imprimo el elemento de la posicion 0
print(meses[11])#imprime el ultimo mes del año
print(meses[-1])#imprime el ultimo elemento de la lista
print(meses[2])#imprime el mes en la posicio 2
print(meses[0:2])#imprime los meses en el rango del [0:2]
print(meses[0:6])#imprime en un rango desde la posicion 0 a la 6
print(meses[3:6])#imprime en un rango determinado
meses.append("lunes")#agrega el elemento lunes
print(meses)
meses.pop(0)#borra el elemento en la posicion 0
print(meses)
meses.pop(-1)#borra el elemento en la ultima posicion
print(meses)
print(len(meses)) #muestra la longitud de la lista
meses.clear()#vacia la lista
print(meses)
del meses # se borra la lista meses
meses = [] # se crea la lista meses
meses.append("enero")#se agrega un elemento a meses
print(meses)
