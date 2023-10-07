print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    3 - Saldo Disponível
    0 - Sair

    ================================

    """
)
saldo = 1000
opcao = -1

while opcao != 0:
    opcao = int(input("Digite o número da operação a ser realizada:\n"))

    if opcao == 1:
        deposito = float(input("Digite a quantia a ser depositada:\n"))
        if deposito >= 0:
            saldo += deposito
            print(f"Operação realizada com sucesso!\nNovo saldo: {saldo:.2f}")
        else:
            print("Valor digitado é inválido!\n")
    elif opcao == 2:
        saque = float(input("Digite a quantia a ser sacada:\n"))
        if saque >= 0:
            if saque <= saldo:
                saldo -= saque
                print(f"Operação realizada com sucesso!\nNovo saldo: {saldo:.2f}")
            else: 
                print("Operação inválida! Valor digitado é maior que o saldo em conta.\n")
        else:
            print("Valor digitado é inválido\n")
    elif opcao == 3:
        print(f"O seu saldo atual é: R${saldo:.2f}.\n")
    elif opcao > 0: 
        print("ERRO! A Operação digitada não existe.")
else:
    print(
    """
    ================================

                Obrigado!

    ================================

    """
)


