#Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.
#Critério:
#Pacientes acima de 60 anos têm prioridade.
#Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
#Os demais pacientes são atendidos por ordem de chegada.

#Entrada
#Um número inteiro n, representando a quantidade de pacientes.
#n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
#nome: string representando o nome do paciente.
#idade: número inteiro representando a idade do paciente.
#status: string que pode ser "urgente" ou "normal".
# #"Saída
#A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
pacientes = []
for i in range(n):
    partes = [p.strip() for p in input().strip().split(",")]
    nome, idade, status = partes[0], int(partes[1]), partes[2].lower()
    pacientes.append((i, nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def prioridade(item):
    i, nome, idade, status = item
    if status == "urgente":
        # prioridade máxima, desempate por idade desc
        return (0, -idade, i)
    elif idade >= 60:
        # segunda prioridade, desempate por idade desc
        return (1, -idade, i)
    else:
        # demais: mantém ordem de chegada (mesmo valor secundário)
        return (2, 0, i)

pacientes_ordenados = sorted(pacientes, key=prioridade)

# TODO: Exiba a ordem de atendimento com título e vírgulas:
ordem = ", ".join(nome for _, nome, _, _ in pacientes_ordenados)
print(f"Ordem de Atendimento: {ordem}")