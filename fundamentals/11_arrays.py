# Los arreglos (lista) son una estructura de datos fundamental
# que permite agrupar valores .

first_array = ['Sacar la basura', 'peinarse', 'dormir', 'Secar la ropa']

# En python el primer elemento de un arreglo tiene posicion (indice) 0
print(first_array[0])

print(first_array[1])
print(first_array[2])
print(first_array[3])
# No existe el elemento con indice 4 y python da un error
#print(first_array[4])

# Podemos saber el largo de un arreglo o lista con la funcion pre definida len()
print(len(first_array))
# Ademas podemos agregar elemento al arreglo
first_array.append ('Comer')
first_array.append('dormir')

#
first_array.insert(0, 'levantarse')

# Podemos imprimir la lista completa al final del arreglo con append
print(first_array)





