from hashlib import sha256

class ContaBancaria:
    def __init__(self, id:int, nome:str = '', saldo:float = 0, chave:str = ''):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave == '':
            print('Digite a senha para criar a conta.')
            chave = self.pede_senha()
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else:
            chave = str(input("Digete a senha para validar"))
            self.valida_senha(chave)
        

    def pede_senha(self):
        from pwinput import pwinput
        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha    

    def valida_senha(self, valor):
        valor = sha256(valor.encode("utf-8")).hexdigest()
        if self.__hash == valor:
            print(f"Senha valiadada.")
            return True
        else:
            print("As senhas não conferem. Acesso bloqueado")
            return False

    def __str__(self):
        return f'Estado atual da conta: {self.__dict__}'

    def sacar(self, valor, chave:str = ''):
        if chave == '':
            chave = (self.pede_senha())
            chave = sha256(chave.encode('utf-8')).hexdigest()
        if self.__hash == chave:
            valor = abs(valor)
            if valor > self.__saldo:
                print(f'Saque NEGADO de R${valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE')
            else:
                self.__saldo -= valor
                print(f'Saque AUTORIZADO, valor atual na conta: R${self.__saldo:,.2f}')
        else:
            print('acesso negado a conta!')

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo+=valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self._id}')