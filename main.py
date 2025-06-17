menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 # Valor não pode ser modificado

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado deve ser positivo.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            if valor <= 0:
                print("Operação falhou! O valor informado deve ser positivo.")
                continue

            if valor > saldo:
                print("Operação falhou! Saldo insuficiente.")
            elif valor > limite:
                print("Operação falhou! Valor excede o limite por saque.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques atingido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        print("Saindo do sistema. Obrigado por usar nosso banco!")
        break

    else:
        print("Opção inválida. Tente novamente.")
