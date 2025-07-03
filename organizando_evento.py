# Dicionário para agrupar participantes por tema
eventos = {}


n = int(input().strip())


for _ in range(n):
    linha = input().strip()
    nome, tema = [x.strip() for x in linha.split(',')]

    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(nome)


for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
