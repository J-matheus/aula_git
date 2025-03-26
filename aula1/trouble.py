nome = input ("Insira o nome do aluno: ")
n1 = float (input ("Insira o primeira nota: "))
n2 = float (input ("Insira o segunda nota: "))

media =  (n1 + n2)/2

if  media<7:
    print(f"A media do aluno {nome} é {media}, portanto ele está reprovado")
else :
    print(f"A media do aluno {nome} é {media}, portanto ele está aprovado")
