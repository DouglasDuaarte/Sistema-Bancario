#  classe banco 
from models.class_pessoa import Pessoa
from models.utils import info_conta

class Banco:

    def __init__(self, nome, cnpj, nrBanco):
        self._nome = nome
        self._cnpj = cnpj
        self._nrBanco = nrBanco
        
        self._contas_bancarias = [] 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome


    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj

    
    @property
    def nrBanco(self):
        return self._nrBanco
    
    @nrBanco.setter
    def nrBanco(self, nrBanco):
        self._nrBanco = nrBanco

    

    def info_banco(self):
        print(f"\nNome do Banco: {self._nome}")
        print(f"CPNJ: {self._cnpj}")
        print(f"Numero do Banco: {self._nrBanco}")


    def info_contas(self):
        info_conta(self._contas_bancarias)


    
    def criar_conta(self, conta):
        if conta not in self._contas_bancarias:
            self._contas_bancarias.append(conta)
            print("Conta criada com sucesso!")
        else:
            print("Conta já cadastrada neste banco.")


    def fechar_conta(self, conta):
        if conta in self._contas_bancarias:
            self._contas_bancarias.remove(conta)
            print("Conta removida com sucesso!")
        else:
            print("Conta não encontrada neste banco.")


    @classmethod
    def banco_input(cls):
        nome = str(input("Nome do Banco: "))
        cnpj = str(input("CNPJ do Banco: "))
        nrBanco = int(input("Numero do Banco: "))
        return cls(nome, cnpj, nrBanco)


    