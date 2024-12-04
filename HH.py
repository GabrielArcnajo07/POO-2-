import random

class ContaCorrente:
    def __init__(self, titular, senha):
        self.titular = titular
        self.numero = random.randint(100, 999)
        self.__senha = senha
        self.__saldo = 0.0

    def verificar_senha(self, senha):
        return self.__senha == senha

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito efetuado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor, senha):
        if not self.verificar_senha(senha):
            print("Senha incorreta.")
            return False
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque efetuado com sucesso!")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def aplicar(self, valor, conta_poupanca, senha):
        if self.sacar(valor, senha):
            conta_poupanca.depositar(valor)


class ContaPoupanca(ContaCorrente):
    def __init__(self, titular, senha):
        super().__init__(titular, senha)
        self.__saldo_poupanca = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo_poupanca += valor
            print("Valor aplicado na poupança com sucesso!")
        else:
            print("Valor inválido.")

    def resgatar(self, valor, conta_corrente, senha):
        if not self.verificar_senha(senha):
            print("Senha incorreta.")
            return
        if valor <= self.__saldo_poupanca:
            self.__saldo_poupanca -= valor
            conta_corrente.depositar(valor)
            print("Resgate efetuado com sucesso!")
        else:
            print("Saldo insuficiente na poupança.")

    def get_saldo_poupanca(self):
        return self.__saldo_poupanca

    def extrato(self):
        print("+------------------------------------------+")
        print(f"Titular: {self.titular}")
        print(f"Número da conta: {self.numero}")
        print(f"Saldo da Conta Corrente: R$ {self.get_saldo():.2f}")
        print(f"Saldo da Conta Poupança: R$ {self.get_saldo_poupanca():.2f}")
        print("+------------------------------------------+")


# Sistema de Operações
def main():
    print("Bem-vindo ao Banco Celestial!")
    nome = input("Digite seu nome completo: ")
    while True:
        senha = input("Digite uma senha numérica de 4 dígitos: ")
        if senha.isdigit() and len(senha) == 4:
            break
        print("Senha inválida. Tente novamente.")

    conta_corrente = ContaCorrente(nome, senha)
    conta_poupanca = ContaPoupanca(nome, senha)

    print("\nRealize seu primeiro depósito de no mínimo R$ 10,00!")
    while True:
        try:
            deposito_inicial = float(input("Valor do depósito: R$ "))
            if deposito_inicial >= 10:
                conta_corrente.depositar(deposito_inicial)
                print("Conta criada com sucesso!")
                print(f"Número da conta: {conta_corrente.numero}")
                break
            else:
                print("O valor mínimo é R$ 10,00.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

    while True:
        print("\nEscolha uma operação:")
        print("1. Extrato")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Aplicar")
        print("5. Resgatar")
        print("6. Sair")
        opcao = input("Digite o número da operação: ")

        if opcao == "1":
            conta_poupanca.extrato()
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor para depositar: R$ "))
                conta_corrente.depositar(valor)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "3":
            try:
                valor = float(input("Digite o valor para sacar: R$ "))
                senha = input("Digite sua senha: ")
                conta_corrente.sacar(valor, senha)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "4":
            try:
                valor = float(input("Digite o valor para aplicar: R$ "))
                senha = input("Digite sua senha: ")
                conta_corrente.aplicar(valor, conta_poupanca, senha)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "5":
            try:
                valor = float(input("Digite o valor para resgatar: R$ "))
                senha = input("Digite sua senha: ")
                conta_poupanca.resgatar(valor, conta_corrente, senha)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "6":
            print("Obrigado por usar o Banco Celestial! Até logo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
