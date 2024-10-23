def suma():
    
    try:
         a = int(input("Dime el valor de a: "))
         b = int(input("Dime el valor de b: "))
    
         c = a+b
     
         print("la respueta de la suma es", c)
            
           
            
    except ValueError:
        print("Ingresa un numero valido")
             
def resta():
   try:
         a = int(input("Dime el valor de a: "))
         b = int(input("Dime el valor de b: "))
    
         c = a-b
     
         print("la respueta de la resta es", c)
            
   except ValueError:
       print("Ingrese un numero valido")
       
def multiplicacion():
    try:
        a = int(input("Dime el valor de a: "))
        b = int(input("Dime el valor de b: "))
        
        c = a*b
        
        print("el resultado es:", c)
        
    except ValueError:
        print("Numero Invalido")
        
def divicion():
    try:
        a = int(input("dime el valor de a: "))
        b = int(input("dime el valor de b: "))
        
        c = a/b
        
        print("el resultado es:", c)
        
    except ValueError:
        print("Numero invalido")
        
def calculador():
    while True:
    
     print("(1)Suma. \n(2)Resta. \n(3)Multiplicacion. \n(4)Divicion.")
    
     formulario = input("Dime que deseas: ")
    
     if formulario == "1":
        suma()
     if formulario == "2":
        resta()
     if formulario == "3":
        multiplicacion()
     if formulario == "4":
        divicion()
        
        
if __name__ == '__main__':
       calculador()