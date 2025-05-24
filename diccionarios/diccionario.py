#un diccionario es un lugar en el cual se alamcenas keysclave valor asignacion (:), esta es mutable
diccionario = {"nombre":"juan",
"edad": 30,
"ciudad": "madrid",
1: "uno",
True:"hola"}#cree un diccionario
print(diccionario)#imprimi diccionario
print(diccionario["nombre"])#imprimi el elemento juan usando su clave
print(diccionario["ciudad"])#imprimi madrid con la clave ciudad
print(diccionario["edad"])#imprimi 30 con la clave edad
diccionario["nombre"]= "andres"#modifique nombre
print(diccionario["nombre"])
print(diccionario[1])
print(diccionario[True])
diccionario["profesion"] = ["sistemas", "arquitecto", "arqueologo", "futbolista"]#agrege un elemento
print(diccionario["profesion"])
diccionario.pop("ciudad")
del diccionario [True]
print(len (diccionario))
#diccionario.clear()
print(diccionario)