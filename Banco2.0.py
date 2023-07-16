import os
import re

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.movimentacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentacoes.append({"tipo": "depósito", "valor": valor})
            limpar_tela()
            print(centralizar_texto("Depósito realizado com sucesso."))
            input(centralizar_texto("Pressione Enter para continuar..."))

    def sacar(self, valor):
        if self.saldo >= valor and valor <= 500:
            self.saldo -= valor
            self.movimentacoes.append({"tipo": "saque", "valor": valor})
            limpar_tela()
            print(centralizar_texto("Saque realizado com sucesso."))
            input(centralizar_texto("Pressione Enter para continuar..."))
        else:
            limpar_tela()
            print(centralizar_texto("Não foi possível realizar o saque."))
            input(centralizar_texto("Pressione Enter para continuar..."))

    def extrato(self):
        for movimentacao in self.movimentacoes:
            if movimentacao["tipo"] == "depósito":
                print(centralizar_texto(f"Depósito: R$ {movimentacao['valor']:.2f}"))
            elif movimentacao["tipo"] == "saque":
                print(centralizar_texto(f"Saque: R$ {movimentacao['valor']:.2f}"))
            elif movimentacao["tipo"] == "pix":
                origem = movimentacao["origem"]
                destino = movimentacao["destino"]
                print(centralizar_texto(f"Pix de {origem['nome']} - Conta {origem['conta']} para "
                                        f"{destino['nome']} - Conta {destino['conta']}: R$ {movimentacao['valor']:.2f}"))
        print(centralizar_texto(f"Saldo atual: R$ {self.saldo:.2f}"))

def centralizar_texto(texto):
    largura_terminal = os.get_terminal_size().columns
    espacos_esquerda = (largura_terminal - len(texto)) // 2
    return " " * espacos_esquerda + texto

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

usuarios = []
contas = []
numero_conta = 1
banco = None

def cadastrar_usuario():
    print(centralizar_texto("Faça agora seu cadastro no Banco Digital 2.0"))
    nome = input(centralizar_texto("Digite seu primeiro nome: "))
    sobrenome = input(centralizar_texto("Digite seu sobrenome: "))
    while len(sobrenome.strip()) == 0:
        print("Digite seu sobrenome para prosseguir.")
        sobrenome = input(centralizar_texto("Digite seu sobrenome: "))
    data_nascimento = input(centralizar_texto("Digite sua Data de Nascimento (ddmmaaaa): "))
    while not re.match(r'\d{8}', data_nascimento):
        print("Formato inválido. Digite sua Data de Nascimento no formato ddmmaaaa.")
        data_nascimento = input(centralizar_texto("Digite sua Data de Nascimento (ddmmaaaa): "))
    dia = data_nascimento[:2]
    mes = data_nascimento[2:4]
    ano = data_nascimento[4:]
    data_nascimento_formatada = f"{dia}/{mes}/{ano}"
    cpf = input(centralizar_texto("Digite seu CPF (xxxxxxxxxxx): "))
    while not re.match(r'\d{11}', cpf):
        print("CPF inválido. Digite seu CPF apenas com números.")
        cpf = input(centralizar_texto("Digite seu CPF (xxxxxxxxxxx): "))
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    endereco = input(centralizar_texto("Digite seu endereço (Rua, Cidade - UF): "))
    usuarios.append(Usuario(nome + " " + sobrenome, data_nascimento_formatada, cpf_formatado, endereco))
    print(centralizar_texto("Usuário cadastrado com sucesso."))
    input(centralizar_texto("Pressione Enter para continuar..."))

def criar_conta_corrente(usuario):
    global numero_conta
    nova_conta = ContaCorrente("0001", numero_conta, usuario)
    contas.append(nova_conta)
    numero_conta += 1
    print(centralizar_texto("Conta corrente criada com sucesso."))
    selecionar_conta(nova_conta)

def selecionar_conta(conta):
    global banco
    banco = conta
    nome_usuario = banco.usuario.nome.split()[0]
    print(centralizar_texto(f"Seja bem-vindo(a) {nome_usuario} ao Banco Digital 2.0"))
    input(centralizar_texto("Pressione Enter para continuar..."))

def exibir_menu():
    limpar_tela()
    print(centralizar_texto("==== BANCO DIGITAL 2.0 ===="))
    nome_usuario = banco.usuario.nome.split()[0]
    print(centralizar_texto(f"Boas-vindas {nome_usuario}"))
    print(centralizar_texto(f"Agência: {banco.agencia}   Conta: {banco.numero_conta}"))
    print(centralizar_texto("Selecione uma opção:"))
    print(centralizar_texto("1. Visualizar Saldo"))
    print(centralizar_texto("2. Realizar Depósito"))
    print(centralizar_texto("3. Realizar Saque"))
    print(centralizar_texto("4. Extrato"))
    print(centralizar_texto("5. Criar nova conta"))
    print(centralizar_texto("6. Mudar de conta"))
    print(centralizar_texto("7. PIX"))
    print(centralizar_texto("8. Sair / Mudar de usuário"))
    print(centralizar_texto("=========================="))

def realizar_operacao(opcao):
    if opcao == 1:
        limpar_tela()
        print(centralizar_texto("Saldo atual:"))
        print(centralizar_texto(f"R$ {banco.saldo:.2f}"))
        input(centralizar_texto("Pressione Enter para continuar..."))
    elif opcao == 2:
        limpar_tela()
        print(centralizar_texto("Digite o valor do depósito:"))
        print(centralizar_texto("(ou 0 para cancelar)"))
        valor = float(input(centralizar_texto("")))
        if valor != 0:
            banco.depositar(valor)
    elif opcao == 3:
        limpar_tela()
        print(centralizar_texto("Digite o valor do saque:"))
        print(centralizar_texto("(ou 0 para cancelar)"))
        valor = float(input(centralizar_texto("")))
        if valor != 0:
            banco.sacar(valor)
    elif opcao == 4:
        limpar_tela()
        print(centralizar_texto("Extrato:"))
        banco.extrato()
        input(centralizar_texto("Pressione Enter para continuar..."))
    elif opcao == 5:
        limpar_tela()
        criar_conta_corrente(banco.usuario)
    elif opcao == 6:
        limpar_tela()
        mudar_de_conta()
    elif opcao == 7:
        limpar_tela()
        transferir_pix()
    elif opcao == 8:
        limpar_tela()
        mudar_de_usuario()

def mudar_de_usuario():
    global banco
    print(centralizar_texto("Opção Sair / Mudar de usuário selecionada."))
    print()
    print(centralizar_texto("Escolha uma opção:"))
    print(centralizar_texto("1. Sair"))
    print(centralizar_texto("2. Criar Novo Usuário"))
    print(centralizar_texto("3. Mudar de usuário"))
    print(centralizar_texto("=========================="))
    opcao = int(input(centralizar_texto("Opção selecionada: ")))
    if opcao == 1:
        banco = None
        print(centralizar_texto("Obrigado por usar os serviços do Banco Digital 2.0!"))
        input(centralizar_texto("Pressione Enter para sair..."))
    elif opcao == 2:
        cadastrar_usuario()
        criar_conta_corrente(usuarios[-1])
        exibir_menu()
    elif opcao == 3:
        selecionar_usuario()
        exibir_menu()

def mudar_de_conta():
    print(centralizar_texto("Opção Mudar de conta selecionada."))
    print()
    print(centralizar_texto("Escolha uma conta:"))
    for i, conta in enumerate(contas):
        print(centralizar_texto(f"{i + 1}. Conta {conta.numero_conta}"))
    print(centralizar_texto("=========================="))
    opcao = int(input(centralizar_texto("Opção selecionada: ")))
    if 1 <= opcao <= len(contas):
        selecionar_conta(contas[opcao - 1])
        exibir_menu()

def selecionar_usuario():
    print(centralizar_texto("Selecione um usuário:"))
    for i, usuario in enumerate(usuarios):
        print(centralizar_texto(f"{i + 1}. {usuario.nome}"))
    print(centralizar_texto("=========================="))
    opcao = int(input(centralizar_texto("Opção selecionada: ")))
    if 1 <= opcao <= len(usuarios):
        selecionar_conta_usuario(usuarios[opcao - 1])

def selecionar_conta_usuario(usuario):
    print(centralizar_texto("Selecione uma conta:"))
    for i, conta in enumerate(contas):
        if conta.usuario == usuario:
            print(centralizar_texto(f"{i + 1}. Conta {conta.numero_conta}"))
    print(centralizar_texto("=========================="))
    opcao = int(input(centralizar_texto("Opção selecionada: ")))
    if 1 <= opcao <= len(contas):
        selecionar_conta(contas[opcao - 1])
        exibir_menu()

def transferir_pix():
    print(centralizar_texto("Transferência PIX"))
    print()
    print(centralizar_texto("Escolha uma opção:"))
    print(centralizar_texto("1. Transferir por CPF"))
    print(centralizar_texto("2. Transferir por Conta"))
    print(centralizar_texto("=========================="))
    opcao = int(input(centralizar_texto("Opção selecionada: ")))
    if opcao == 1:
        transferir_pix_cpf()
    elif opcao == 2:
        transferir_pix_conta()

def transferir_pix_cpf():
    print(centralizar_texto("Transferência PIX por CPF"))
    print()
    cpf_destino = input(centralizar_texto("Digite o CPF de destino: "))
    valor = float(input(centralizar_texto("Digite o valor a ser transferido: R$ ")))
    conta_origem = {"nome": banco.usuario.nome, "conta": banco.numero_conta}
    conta_destino = None
    for conta in contas:
        if conta.usuario.cpf == cpf_destino:
            conta_destino = {"nome": conta.usuario.nome, "conta": conta.numero_conta}
            break
    if conta_destino is not None:
        banco.saldo -= valor
        banco.movimentacoes.append({"tipo": "pix", "valor": valor, "origem": conta_origem, "destino": conta_destino})
        print(centralizar_texto("Transferência PIX realizada com sucesso."))
    else:
        print(centralizar_texto("CPF de destino não encontrado."))
    input(centralizar_texto("Pressione Enter para continuar..."))

def transferir_pix_conta():
    print(centralizar_texto("Transferência PIX por Conta"))
    print()
    conta_destino = int(input(centralizar_texto("Digite o número da conta de destino: ")))
    valor = float(input(centralizar_texto("Digite o valor a ser transferido: R$ ")))
    conta_origem = {"nome": banco.usuario.nome, "conta": banco.numero_conta}
    conta_destino = None
    for conta in contas:
        if conta.numero_conta == conta_destino:
            conta_destino = {"nome": conta.usuario.nome, "conta": conta.numero_conta}
            break
    if conta_destino is not None:
        banco.saldo -= valor
        banco.movimentacoes.append({"tipo": "pix", "valor": valor, "origem": conta_origem, "destino": conta_destino})
        print(centralizar_texto("Transferência PIX realizada com sucesso."))
    else:
        print(centralizar_texto("Conta de destino não encontrada."))
    input(centralizar_texto("Pressione Enter para continuar..."))

# Mensagem de boas-vindas
limpar_tela()
print(centralizar_texto("==== BANCO DIGITAL 2.0 ===="))
print(centralizar_texto("Seja bem-vindo(a) ao Banco Digital 2.0"))
input(centralizar_texto("Pressione Enter para continuar..."))

# Cadastro de usuário
limpar_tela()
cadastrar_usuario()

# Criação de conta corrente
limpar_tela()
criar_conta_corrente(usuarios[-1])

while True:
    exibir_menu()
    opcao = int(input(centralizar_texto("Opção selecionada: ")))

    if opcao == 8:
        limpar_tela()
        mudar_de_usuario()
    else:
        realizar_operacao(opcao)
