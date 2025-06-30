from abc import ABC, abstractmethod
from models.class_pessoa import Pessoa
from models.class_banco import Banco

class Conta_Bancaria(ABC):
    def __init__(self, titular: Pessoa, banco: Banco, nrConta: int, saldo: float, senha: str):
        self._titular = titular
        self._banco = banco
        self._nrConta = nrConta
        self._saldo = saldo
        self._senha = senha

#Getters e setters

    @property
    def titular(self):
        return self._titular

    @property
    def banco(self):
        return self._banco

    @property
    def nrConta(self):
        return self._nrConta

    @nrConta.setter
    def nrConta(self, nrConta):
        self._nrConta = nrConta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = str(senha)

#Métodos de saque direto e por terminal

    def saque(self, valor, senha):
        if self.verifica_senha(senha):
            if valor > 0 and valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque concluído de R${valor:.2f} -- R${self._saldo:.2f} saldo após saque.")
            else:
                print("Saldo insuficiente ou valor menor ou igual a 0")
        else:
            print("Senha inválida")

    def saque_terminal(self):
        valor = float(input("Digite o valor desejado: "))
        if self.verifica_senha_terminal():
            if valor > 0 and valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque concluído de R${valor:.2f} -- R${self._saldo:.2f} saldo após saque.")
            else:
                print("Saldo insuficiente ou valor menor ou igual a 0")
        else:
            print("Senha inválida")

#Métodos de depósito direto e por terminal


    def deposito(self, valor):
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado.")

    def deposito_terminal(self):
        valor = float(input("Digite o valor a ser depositado: "))
        return self.deposito(valor)
    
#Métodos de senha
    def verifica_senha(self, senha):
        return senha == self._senha

    def verifica_senha_terminal(self):
        senha = input("Digite a senha da conta: ")
        return self.verifica_senha(senha)


    @abstractmethod
    def novo_mes(self):
        pass