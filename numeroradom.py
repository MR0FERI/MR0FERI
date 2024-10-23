import random

azar = random.randint(1, 100)

while True:
 usuario = int(input("Dime un numero al azar: "))
 
 if usuario == azar :
     print("has hacertado")
     break
 if usuario < azar:
     print("el numero es muy bajo, intentalo de nuevo")
 if usuario > azar:
     print("el numero es muy alto, intentalo de nuevo")

