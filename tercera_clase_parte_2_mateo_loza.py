lista_1 = ["C"
,
"C++"
,
"Python"
,
"Java"]

lista_2 = ["PHP"
,
"SQL"
,
"Visual Basic"]

print(lista_1[1:3])

print(len(lista_1))

print(lista_1 + lista_2)

lista_1.append("R")
print(lista_1)

lista_2.sort()

print(lista_2)

lista_2.reverse()
print(lista_2)

# Práctica Listas 1
# Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

mi_lista_1 = ["Numero1",2,3,"Numero4",6!=2]

print(mi_lista_1)

# Práctica Listas 2
# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
# medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.

medios_transporte_2 = ["avión","auto","barco","bicicleta"]

medios_transporte_2_2 = ["motocicleta"]

print(medios_transporte_2 + medios_transporte_2_2)

# Práctica Listas 3
# Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
# manzana
# banana
# mango
# cereza
# sandía

frutas_3= ["manzana","banana","mango","cereza","sandía"]
eliminado_3 = frutas_3.pop(2)

print(eliminado_3)

#-------------------------------------------------------------------

mi_diccionario = {"curso":"Python TOTAL"
,
"clase":"Diccionarios"}

mi_diccionario["recursos"] = ["notas"
,
"ejercicios"]

print(mi_diccionario.keys())
print(mi_diccionario.values())
print(mi_diccionario.items())


# Práctica Diccionarios 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
# nombre: Karen
# apellido: Jurgens
# edad: 35
# ocupacion: Periodista
# Los nombres de las claves y valores deben ser iguales a la consigna.

mi_dic_4 = {"nombre":"Karen","apellido":"Jurgens","edad":"35","ocupacion":"periodista"}

# Práctica Diccionarios 2
# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
#mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#print(mi_dict[])

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}


print(mi_dict["puntos"]["points2"][1])



# Práctica Diccionarios 3
# Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
# nombre: Karen
# apellido: Jurgens
# edad: 36
# ocupacion: Editora
# pais: Colombia
# para ello, no debes 
# cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

mi_dic_4["pais"] = "colombia"
 
print(mi_dic_4)

#---------------------------------------------------------------------

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

mi_tuple = (1,"dos", [3.33,"cuatro"], (5.0, 6))

lista_1 = list(mi_tuple)
print(lista_1)


a, b, c, d = mi_tuple

print(c)

# Práctica Tuples 1
# Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

tupla_1 = (1, 2, 3, 4, 5, 2, 2, 5, 7, 6, 2, 6, 1, 5, 3, 3, 6, 2, 4, 5, 5, 2, 2, 2, 1, 3)

print(tupla_1.count(2))


# Práctica Tuples 2
# Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
# mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_tupla_2 = (1, 2, 3, 2, 3, 1, 3, 2)

mi_lista = list(mi_tupla_2)

print(mi_lista)

# Práctica Tuples 3
# Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
# mi_tupla = (1, 2, 3, 4)

mi_tupla_3 = (1, 2, 3, 4)

a,b,c,d = mi_tupla_3

print(a,b,d)

