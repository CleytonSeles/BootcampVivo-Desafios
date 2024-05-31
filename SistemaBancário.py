import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Usuário
    [5]\tNova Conta
    [6]\tListar Contas
    [7]\tSair
    
    => """
    return input(textwrap.dedent(menu))

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print(f"\n=== Depósito no valor de R${valor:.2f} realizado com sucesso! ===")
    else: 
        print("\n@@@ Operação falhou! Valor informado é inválido! @@@")
    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, numero_de_saques, limite_saques):
    
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= limite_saques
    excedeu_saldo = valor > saldo
    
    if excedeu_limite:
        print("\n@@ Operação falhou! Você excedeu o limite diário de saque. @@")
    elif excedeu_saques:
        print("\n@@ Operação falhou! Você o limite de saques diário. @@")
    elif excedeu_saldo:
        print("\n@@ Operação falhou! Saldo insuficiente. @@")    
    elif valor > 0:
        saldo -= valor
        numero_de_saques += 1
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        print(f"\n=== Saque no valor de R${valor:.2f} realizado com sucesso! ===")
    else:
        print("\n@@ Operação falhou! Valor informado é inválido! @@")
            
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n======== EXTRATO ========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print("=" * 24)
    
def criar_usuário(usuarios):
    cpf = input("Informe o seu CPF(SOMENTE NÚMEROS): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("\n@@ Usuário já exixtente! @@")
        return
    
    nome = input("Informe o seu nome completo: ").rstrip().lstrip().title()
    data_nascimento = input("Informe sua data de nascimento(dia/mês/ano): ").strip()
    endereco = input("Informe seu endereço completo(logradouro, número - bairro - cidade/UF): ").rstrip().lstrip()
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=== Usuário cridado com sucesso! ===")
    
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = input("Informe o seu CPF(SOMENTE NÚMEROS): ")
    usuario = filtrar_usuarios(cpf, usuarios)   
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario}
    
    print("@@ Usuário não encontrado! Fluxo de criação de conta encerrado. @@")
    
def listar_contas(contas):
    for conta in contas:
        lista = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_da_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(lista))
    
def main(): 
    saldo = 0
    limite = 500
    extrato = ''
    numero_de_saques = 0
    usuarios = []
    contas = []
    
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    
    while True:
        
        opcao = menu()
        
        if opcao == "1":
            valor = float(input("Valor do depósito: R$"))
            
            saldo, extrato = depositar(valor, saldo, extrato)
            
        elif opcao == "2":
            valor = float(input("Valor do saque: R$"))
            
            saldo, extrato = sacar(
                valor=valor,
                saldo=saldo,
                extrato=extrato, 
                limite=limite, 
                numero_de_saques=numero_de_saques, 
                limite_saques=LIMITE_SAQUES,
            )
                
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuário(usuarios)
        
        elif opcao == "5":
            numero_da_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_da_conta, usuarios) 
            
            if conta:
                contas.append(conta) 
        
        elif opcao == "6":
            listar_contas(contas)
        
        elif opcao == "7":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()
