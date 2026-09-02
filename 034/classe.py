from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str, salario:int|float):
        self.nome = nome
        self.__salario = None
        self.salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if self.__salario is None or novo_salario >= self.__salario:
            self.__salario = novo_salario
        else:
            raise ValueError("Você não pode diminuir o salário do funcionário!")

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        return f"{self.nome} ganha {self.__salario} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus()}"
    



class Gerente(Funcionario):
    bonus = 15
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return (self.salario/100)*self.bonus

class Designer(Funcionario):
    bonus = 8
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return (self.salario/100)*self.bonus

class Desenvolvedor(Funcionario):
    bonus = 10
    def __init__(self, nome, sal):
        super().__init__(nome, sal)

    def calcular_bonus(self):
        return (self.salario/100)*self.bonus
