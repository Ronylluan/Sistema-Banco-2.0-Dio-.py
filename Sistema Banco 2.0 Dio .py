# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Variáveis globais para controle
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
numero_conta = 1

# Função para criar um novo usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Usuário com este CPF já cadastrado.")
            return
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

# Função para criar uma nova conta bancária
def criar_conta(cpf):
    global numero_conta
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
            numero_conta += 1
            return
    print("Erro: Usuário não encontrado. Conta não criada.")

# Função de depósito (apenas por posição)
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função de saque (apenas por nome)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

# Função de extrato (por posição e nome)
def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função para listar contas
def listar_contas():
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")

# Menu principal
def menu():
    menu_principal = """
    [u] Cadastrar Usuário
    [c] Cadastrar Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Listar Contas
    [q] Sair

    => """
    return input(menu_principal).lower()

# Loop principal
while True:
    opcao = menu()

    if opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "l":
        listar_contas()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
