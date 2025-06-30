from models.class_contaBancaria import Conta_Bancaria

class Conta_Poupanca(Conta_Bancaria):
    def __init__(self, titular, banco, nrConta, saldo, senha, rendimento):
        super().__init__(titular, banco, nrConta, saldo, senha)
        self._rendimento = rendimento
        self._saques_mensais = 3


    def saque(self, valor, senha):
        if self._saques_mensais > 0:
            resultado = super().saque(valor, senha)
            if resultado is None or resultado:  #Se saque foi realizado
                self._saques_mensais -= 1
                print(f"Saques restantes no mês: {self._saques_mensais}")
        else:
            print("Limite de saques mensais atingido.")

    def novo_mes(self):
        self._saldo += self._saldo * self._rendimento
        self._saques_mensais = 3
        print("Novo mês: rendimento aplicado e saques mensais resetados.")


    def __str__(self):
        return (f"Conta Poupança\n"
                f"Banco: {self._banco.nome}\n"
                f"Nº Conta: {self._nrConta}\n"
                f"Titular: {self._titular.nome}\n"
                f"Saldo: R${self._saldo:.2f}\n"
                f"Rendimento mensal: {self._rendimento*100:.2f}%\n"
                f"Saques restantes no mês: {self._saques_mensais}")
    

    @property
    def rendimento(self):
        return self._rendimento
    
    @rendimento.setter
    def rendimento(self, valor_rendido):
        self._rendimento = valor_rendido

