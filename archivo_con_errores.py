import random   

tirando_dados = True

#este bucle es para mantener al programa tirando los dados mientras que el input que se le de equivalga a 'si'


while tirando_dados:
    print ("Tirando los dados...")
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    print (f"Dado 1: {d1}\nDado 2: {d2}")


    tirar_dados = input("Tirar dados de nuevo (si/no)? ")
    print(tirar_dados)

    if tirar_dados != "si" and tirar_dados != "yes":
        tirando_dados = False