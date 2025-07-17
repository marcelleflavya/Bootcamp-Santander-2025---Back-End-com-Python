#Uma empresa quer criar um organizador de eventos que 
# divida os participantes em grupos de acordo com o tema escolhido
# Dicionário para agrupar participantes por tema
eventos = {}


n = int(input().strip())

#Crie um loop para armazenar participantes e seus temas:
#
for _ in range(n):
    linha = input().strip()
    nome, tema = [x.strip() for x in linha.split(',')]

    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(nome)


for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
