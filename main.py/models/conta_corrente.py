from models.class_contaBancaria import Conta_Bancaria

class Conta_Corrente(Conta_Bancaria): #herdando todas as funções da classe mae conta_bancaria
    def __init__(self, titular, banco, nrConta, saldo, senha, taxas_mensais):
        super().__init__(titular, banco, nrConta, saldo, senha)
        self._taxas_mensais = taxas_mensais

    def novo_mes(self):
        self._saldo -= self._taxas_mensais
        print(f"Taxa mensal de R${self._taxas_mensais:.2f} descontada. Saldo atual: R${self._saldo:.2f}")


    

    def __str__(self):
        return (f"Conta Corrente\n"
                f"Banco: {self._banco.nome}\n"
                f"Nº Conta: {self._nrConta}\n"
                f"Titular: {self._titular.nome}\n"
                f"Saldo: R${self._saldo:.2f}\n"
                f"Taxa mensal: R${self._taxas_mensais:.2f}")

    @property
    def taxas_mensais(self):
        return self._taxas_mensais

    @taxas_mensais.setter
    def taxas_mensais(self, valor):
        self._taxas_mensais = valor