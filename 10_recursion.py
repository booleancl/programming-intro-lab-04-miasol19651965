import time
# Es perfectamente posible llamar una funcion dentro de otra
# Lo hicimos cuando calculamos el volumen del cilindro.

# Pero tambien es perfectamente posible que una funcion se llame a si misma-
# Esto es una tecnica muy poderosa para ciertos problemas.


# funcion conteo regresivo

# KABUMM es una funcion de conteo regresivo
def countdown(number) :
    if number <= 0:
      print("KABUMM")
    else:
      print(number) 
      time.sleep(0.5)  
      countdown(number -1) 

countdown(5)

def super_sum(number):
  if number <= 0:
   return number
  else:

   returnnumber + super_sum(number -1)   

   print(super_sum(3))

   # Recursion infinita, sin condicion de salida, para nada util, entretenida
def infinite() :
  infinite()








    
        
