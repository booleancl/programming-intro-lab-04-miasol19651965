# Podemos crear o definir nuestras propias funciones
# Lo hacemos con la palabra especial "def "y el cuerpo
# La funcion debe ir corractamenta indentado

def chuchuwa(inst) :
  print("chuchuwa chuchuwa chuchuwa wa wa!")
  print("chuchuwa chuchuwa chuchuwa wa wa!")
  print("Atencion!, Compania:")
  print(inst)

print(chuchuwa)
print(type(chuchuwa))

# El llamado de la funcion
chuchuwa("Manos al frente")
chuchuwa("Hombro hacia atras")

#Las funciones deben llamarse o ejucutarse con los mismos parametros que se definio.
chuchuwa("Lenguaje afuera")

#  Si la funcion no tiene un valor de retorno , nos entregara none que es representar nada.
print(result)