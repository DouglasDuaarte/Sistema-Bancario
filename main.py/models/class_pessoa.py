from models.utils import info_conta



class Pessoa:
    def __init__(self, nome, sobrenome, cpf, idade):
        
        self._nome = nome
        self._sobrenome = sobrenome
        self.__cpf = cpf
        self._idade = idade
        self._contas_bancarias = []
        
    #getter de nome

    @property  
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome.capitalize()

    #getter de sobrenome     

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome.capitalize()


    #getter de cpf

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        

    @property
    def contas_bancarias(self):
        return self._contas_bancarias

    def adicionar_conta(self, conta):
        self._contas_bancarias.append(conta) 


    #metodos de informações   

    def info_pessoa(self):
        print(f"\nNome: {self._nome} {self._sobrenome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self._idade} Anos")



    def info_contas(self):
        info_conta(self._contas_bancarias) #utils import
    

    #criando meus objetos apartir de inputs @classmethod

    @classmethod
    def tecla_input(cls):
        nome = input("Digite o Nome: ").capitalize()
        sobrenome = input("Digite o Sobrenome: ").capitalize()
        cpf = int(input("Digite o CPF: "))
        idade = int(input("Digite a Idade: "))
        return cls(nome, sobrenome, cpf, idade)


