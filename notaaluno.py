nome = (input (f"Insira o nome do aluno: "))
nota1 = float (input (f"Insira a primeira nota do aluno: "))
nota2 = float (input (f"Insira a segunda nota do aluno: "))
nota3 = float (input (f"Insira a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) /3

if media>=7: print (f"O aluno {nome} tem a media {media} está aprovado ")
elif media>=4: print (f"O aluno {nome} tem a media {media} portanto está em recuperação ")
else: print (f"O aluno {nome} tem a media {media} portanto está reprovado")
