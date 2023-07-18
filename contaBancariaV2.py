import textwrap

# FUNÇÕES -----------------------------------------------------------------------------------

def menu():
    menu = """\n

    --- MENU ---
    [s]\tSacar
    [d]\tDepositar
    [e]\tExtrato
    [nc]\tNova conta
    [l]\tListar contas
    [n]\tNovo usuário
    [q]\tSair
    Digite sua opção: """
    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print("Saldo insuficiente")

    elif valor > limite:
        print("Saque maior que o limite")
    
    elif numero_saques >= limite_saques:
        print("Número maximo de saques excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado!")
    
    else:
        print("Valor inválido.")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado!")
    else:
        print("Valor negativo")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("--- EXTRATO ---")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Digite o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Usuário criado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
          Agência:\t {conta['agencia']}
          C/C: \t\t {conta['numero_conta']}
          Titular:\t {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# MAIN --------------------------------------------------------------------------------------
def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []


  while True:
    op = menu()

    if op == "s":
        valor = float(input("Valor do saque: "))

        saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES,
        )

    elif op == "d":
        valor = float(input("Valor: "))

        saldo, extrato = depositar(saldo, valor, extrato)
        

    elif op == "e":
        exibir_extrato(saldo, extrato=extrato)
     
    elif op == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif op == "l":
        listar_contas(contas)

    elif op == "n":
        criar_usuario(usuarios)
    
    elif op == "q":
        break

    else:
        print("\nOpcao invalida\n")


main()