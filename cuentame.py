nn = 0
np = 0
c = 0
co = 1

while True:
    usuario = int(input("dime cualquier numero: "))
    
    if usuario == 0:
        c = c+1
    if usuario < 0:
        nn = nn+1
    if usuario > 0:
        np = np+1
        
    print("Numeros Positivos ", np, "Numeros Negativos ", nn, "Ceros ", c)
    
    co = int(input("Quieres continuar 1:Si, 2:No : "))
    
    if co == 2:
        break