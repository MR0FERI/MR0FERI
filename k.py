print("Ha salido el sol y es un hermoso dia, donde piensas desayunar.")

usuario = int(input("Que opcion tomas: 1.Salir a Comer algo;  2.Quedarte en casa a comer: "))

if usuario == 1:
    print("Has decidido salir a comer algo, viste una cafeteria y un restaurante cerca")
    usuario = int(input("Donde vas a comer?: 1.Cafeteria; 2.Restaurante: "))

if usuario == 2:
    print("Has decidido comer en casa, tienes cereal y cafe, has decidido desayunar con eso.")
