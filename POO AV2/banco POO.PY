import random

class ContaCorrente:
    def __init__(self, nome_titular, senha):
        self.nome_titular = nome_titular
        self.numero_conta = random.randint(100, 999)
        self.__senha = senha
        self.__saldo_corrente = 0.0
        self.bloqueada = False

    def validar_senha(self, senha):
        return self.__senha == senha

    def alterar_saldo_corrente(self, valor):
        self.__saldo_corrente += valor

    def get_saldo_corrente(self):
        return self.__saldo_corrente

    def depositar(self, valor):
        if valor >= 10.0:
            self.alterar_saldo_corrente(valor)
            print("Depósito realizado com sucesso!")
        else:
            print("O depósito inicial deve ser no mínimo R$ 10,00.")

    def sacar(self, valor):
        if valor > self.__saldo_corrente:
            print("Saldo insuficiente.")
        else:
            self.alterar_saldo_corrente(-valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def aplicar(self, conta_poupanca, valor):
        if valor > self.__saldo_corrente:
            print("Saldo insuficiente para aplicação.")
        else:
            self.alterar_saldo_corrente(-valor)
            conta_poupanca.alterar_saldo_poupanca(valor)
            print(f"Aplicação de R$ {valor:.2f} para poupança realizada com sucesso!")


class ContaPoupanca(ContaCorrente):
    def __init__(self, nome_titular, senha):
        super().__init__(nome_titular, senha)
        self.__saldo_poupanca = 0.0

    def alterar_saldo_poupanca(self, valor):
        self.__saldo_poupanca += valor

    def get_saldo_poupanca(self):
        return self.__saldo_poupanca

    def resgatar(self, valor):
        if valor > self.__saldo_poupanca:
            print("Saldo insuficiente na poupança.")
        else:
            self.alterar_saldo_poupanca(-valor)
            self.alterar_saldo_corrente(valor)
            print(f"Resgate de R$ {valor:.2f} da poupança realizado com sucesso!")

    def extrato(self):
        print("\n=== Extrato ===")
        print(f"Titular: {self.nome_titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo Conta Corrente: R$ {self.get_saldo_corrente():.2f}")
        print(f"Saldo Conta Poupança: R$ {self.get_saldo_poupanca():.2f}")
        print("================")


# Interface de usuário
def criar_conta():
    nome = input("Digite o nome completo do titular: ")
    while True:
        senha = input("Crie uma senha numérica de 4 dígitos: ")
        if len(senha) == 4 and senha.isdigit():
            senha = int(senha)
            break
        else:
            print("A senha deve ter exatamente 4 dígitos numéricos.")
    
    conta = ContaPoupanca(nome, senha)
    while True:
        deposito_inicial = float(input("Faça o depósito inicial (mínimo R$ 10,00): "))
        if deposito_inicial >= 10:
            conta.depositar(deposito_inicial)
            print(f"Conta criada com sucesso! Número da conta: {conta.numero_conta}")
            return conta
        else:
            print("O depósito inicial deve ser no mínimo R$ 10,00.")


def autenticar(conta):
    tentativas = 3
    while tentativas > 0:
        senha = int(input("Digite sua senha: "))
        if conta.validar_senha(senha):
            return True
        else:
            tentativas -= 1
            print(f"Senha incorreta. Tentativas restantes: {tentativas}")
    conta.bloqueada = True
    print("Conta bloqueada. Dirija-se à agência com documento com foto.")
    return False


def menu():
    conta = criar_conta()

    while True:
        print("\n=== Menu ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Aplicar para Poupança")
        print("4. Resgatar da Poupança")
        print("5. Extrato")
        print("6. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            valor = float(input("Digite o valor a depositar: "))
            conta.depositar(valor)

        elif opcao == 2:
            if autenticar(conta):
                valor = float(input("Digite o valor a sacar: "))
                conta.sacar(valor)

        elif opcao == 3:
            if autenticar(conta):
                valor = float(input("Digite o valor a aplicar para poupança: "))
                conta.aplicar(conta, valor)

        elif opcao == 4:
            if autenticar(conta):
                valor = float(input("Digite o valor a resgatar da poupança: "))
                conta.resgatar(valor)

        elif opcao == 5:
            conta.extrato()

        elif opcao == 6:
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


# Executar o programa
menu()
