# Tenemos expresiones que se pueden evaluar en terminos booleanos 
# o dicotomicos
# Ejemplo

print(10 > 9)

# Esto nos permite hacer ejecuciones condiconales por ej:

def is_adult(age) : 
    if age >= 18:
        return True
    else:
       return False

gaby_age = 30
sole_age = 30

# Estas siguietes instrucciones las podemos leer como:
# Si (if) el resultado de is_adult ejecutada con la variable gaby_age
# es verdadero, entonces el programa imprime "¿Quieres una cerveza"
# De otro modo (else) imprime "Cantemos Chuchuwa?"|

if is_adult(sole_age) :
    print("¿Quieres una Cerveza?")
else:
    print("Cantemos Chuchuwa")

# elif es una abreviacion "else if" nos permite seguir evaluando expresiones, Podemos tener tantos como necesitamos .

if  sole_age > gaby_age:
    print("Sole es mayor que Gaby")
elif sole_age < gaby_age:
       print("Sole es menor que Gaby")
else:
    print("Tienen la misma edad Gaby y Sole")
    