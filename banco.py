saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input("""

Escolha uma opção:
      1 - Depositar
      2 - Sacar
      3 - Extrato
      4 - Sair 
""")

    if opcao == "1":
        valor = float(input("Quanto você deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito feito com sucesso")
        else:
            print("Não é aceito valor negativo ou zero")

    elif opcao == "2":
        valor = float(input("Quanto você deseja sacar? "))

        if valor <= 0:
            print("Valor inválido para saque")

        elif valor > saldo:
            print("O valor informado é maior do que o saldo da conta")

        elif valor > limite:
            print("Só é possível sacar até R$500,00")

        elif numero_saques >= LIMITE_SAQUES:
            print("Só é permitido fazer três saques por dia")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque feito com sucesso")

    elif opcao == "3":
        print("\n=== Extrato ===")
        if extrato:
            print(extrato)
        else:
            print("Não foram feitas movimentações na conta.")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Retorne para uma opção válida.")
