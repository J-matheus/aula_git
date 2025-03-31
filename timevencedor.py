time1 = input("Informe o nome do primeiro time: ")
time2 = input("Informe o nome do segundo time: ")
time1gol = int(input("Informa a quantidade de gols: "))
time2gol = int(input("Informa a quantidade de gols: "))

if time1gol == time2gol:
    print(f"O jogo entre {time1} e {time2} foi empate")
else:
    if time1gol > time2gol: print("o time vencedor é {time1}")
    else: print(f"O time vencedor é {time2}")
