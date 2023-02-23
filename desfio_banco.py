menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 2

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("digite o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou, o valor informado é inválido")
    
    elif opcao == "s":
        valor = float(input("Digite o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque > limite_saque

        if excedeu_saldo:
            print("operação falhou! saldo insuficiente.")

        elif excedeu_limite:
            print("operação falhou! o valor do saque excede o limite diário de saques.")

        elif excedeu_saques:
            print("operação falhou! você atingiu o limite diário de saques!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saque += 1

        else:
            print("operação falhou! o valor informado é inválido.")
    

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("==================================")

    elif opcao == "q":
        break