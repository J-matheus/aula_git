nome = input ("Insira o nome do empregado: ")
idade = int (input (f"Insira a idade do empregado: "))
salario = float (input(f"Insira o salário do empregado: "))
aumento = float (input (f"Insira valor de aumento do empregado: "))
valoraumento = salario*aumento/100
novosalario = salario+valoraumento
print(f"O empregado {nome} tem {idade} e recebe {salario}"
      f" Você recebeu um aumento de {aumento} seu novo salario é de {novosalario: .2f}")