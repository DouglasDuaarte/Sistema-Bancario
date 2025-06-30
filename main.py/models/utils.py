
def info_conta(self):
    if not self._contas_bancarias:
        print("Nenhuma conta cadastrada!")

    else:
        print("\n--Contas Bancarias--\n")
        for conta in self._contas_bancarias:
            print(conta)