#Pergunta ao usuário seu nome
nome = input("Digite seu nome: ").strip().title()
primeiro_nome, segundo_nome = nome.split(" ")
#fala olá para o usuário
print(f"Olá, {primeiro_nome}")