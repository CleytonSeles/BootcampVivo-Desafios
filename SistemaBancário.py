menu = '''
        ==== CLS BANK ====
        
        Escolha uma opção: 
        [1] DEPÓSITO
        [2] SAQUE
        [3] EXTRATO
        [4] SAIR
        
        >> '''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Valor do depósito: R$"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido!")
    
    elif opcao == "2":
        valor = float(input("Valor do saque: R$"))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_numero_de_saques = numero_de_saques > LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            
        elif excedeu_numero_de_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_de_saques += 1
            
        else:
            print("Operação falhou! O valor informado é inválido!")
            

    elif opcao == "3":
        print("\n====== EXTRATO ======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=" * 20)
    
    elif opcao == "4":
        break   

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")

print("Volte sempre!!")
