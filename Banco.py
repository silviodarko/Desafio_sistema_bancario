import os


class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            limpar_tela()
            print(centralizar_texto("Depósito realizado com sucesso."))

    def sacar(self, valor):
        if self.saldo >= valor and valor <= 500 and len(self.saques) < 3:
            self.saldo -= valor
            self.saques.append(valor)
            limpar_tela()
            print(centralizar_texto("Saque realizado com sucesso."))
        else:
            limpar_tela()
            print(centralizar_texto("Não foi possível realizar o saque."))

    def extrato(self):
        if not self.depositos and not self.saques:
            print(centralizar_texto("Não foram realizadas movimentações."))
        else:
            print(centralizar_texto("Extrato:"))
            for deposito in self.depositos:
                print(centralizar_texto(f"Depósito: R$ {deposito:.2f}"))
            for saque in self.saques:
                print(centralizar_texto(f"Saque: R$ {saque:.2f}"))
            print(centralizar_texto(f"Saldo atual: R$ {self.saldo:.2f}"))


# Função auxiliar para centralizar o texto
def centralizar_texto(texto):
    largura_terminal = os.get_terminal_size().columns
    espacos_esquerda = (largura_terminal - len(texto)) // 2
    return " " * espacos_esquerda + texto


# Função auxiliar para limpar a tela
def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Criação do objeto Banco
banco = Banco()

# Mensagem de boas-vindas
limpar_tela()
print(centralizar_texto("==== BANCO DIGITAL ===="))
print(centralizar_texto("Seja bem-vindo(a) ao Banco Digital!"))
input(centralizar_texto("Pressione Enter para continuar..."))

# Loop principal do programa
while True:
    limpar_tela()
    print(centralizar_texto("==== BANCO DIGITAL ===="))
    print(centralizar_texto("Selecione uma opção:"))
    print(centralizar_texto("1. Visualizar Saldo"))
    print(centralizar_texto("2. Realizar Depósito"))
    print(centralizar_texto("3. Realizar Saque"))
    print(centralizar_texto("4. Extrato"))
    print(centralizar_texto("5. Sair"))
    print(centralizar_texto("======================="))
    opcao = input(centralizar_texto("Opção selecionada: "))

    if opcao == "1":
        limpar_tela()
        print(centralizar_texto("Saldo atual:"))
        print(centralizar_texto(f"R$ {banco.saldo:.2f}"))
        input(centralizar_texto("Pressione Enter para continuar..."))
    elif opcao == "2":
        limpar_tela()
        print(centralizar_texto("Digite o valor do depósito:"))
        print(centralizar_texto("(ou 0 para cancelar)"))
        valor = float(input(centralizar_texto("")))
        if valor != 0:
            banco.depositar(valor)
            input(centralizar_texto("Pressione Enter para continuar..."))
    elif opcao == "3":
        limpar_tela()
        print(centralizar_texto("Digite o valor do saque:"))
        print(centralizar_texto("(ou 0 para cancelar)"))
        valor = float(input(centralizar_texto("")))
        if valor != 0:
            banco.sacar(valor)
            input(centralizar_texto("Pressione Enter para continuar..."))
    elif opcao == "4":
        limpar_tela()
        print(centralizar_texto("Extrato:"))
        banco.extrato()
        input(centralizar_texto("Pressione Enter para continuar..."))
    elif opcao == "5":
        limpar_tela()
        print(centralizar_texto("Deseja mesmo sair?"))
        print(centralizar_texto("(1-Sim / 2-Não)"))
        confirmacao = input(centralizar_texto(""))
        if confirmacao == "1":
            limpar_tela()
            print(centralizar_texto("Obrigado por usar os serviços do Banco Digital!"))
            break
    else:
        limpar_tela()
        print(centralizar_texto("Opção inválida. Por favor, selecione uma opção válida."))
        input(centralizar_texto("Pressione Enter para continuar..."))
