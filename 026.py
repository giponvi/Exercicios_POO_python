from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto, salario):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5


    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        return f'seu salario corresponde a {self.salario/self.sal_min} salarios minimos'



class Horista(Funcionario):
    def __init__(self, nome, sal_bruto, salario, valor_hora, horas_trab):
        super().__init__(nome, sal_bruto, salario)
        self.valor_hora = valor_hora
        self,horas_trab = horas_trab

    def calc_sal(self):
        pass



class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto, salario):
        super().__init__(nome, sal_bruto, salario)

    def calc_sal(self):
        pass