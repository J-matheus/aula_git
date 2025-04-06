hora1 = int(input("Digite a hora de entrada 1: (exe: 3) " ))
minuto1 = int(input("Digite os minutos de entrada 1:(exe: 45) "))

hora2 = int(input("Digite a hora de entrada 2: (exe: 14) "))
minuto2 = int(input("Digite os minutos de entrada 2: (exe: 20) "))

total_minuto1 = hora1 * 60 + minuto1
total_minuto2 = hora2 * 60 + minuto2

resultado = total_minuto2 - total_minuto1 - 270

if resultado <0:
    resultado = resultado + 1440

hora_resultado = resultado // 60
minuto_resultado = resultado % 60

if minuto_resultado <10:
    print(f"Saída: {hora_resultado}:0{minuto_resultado}")
else:
    print(f"Saída: {hora_resultado}:{minuto_resultado}")
    