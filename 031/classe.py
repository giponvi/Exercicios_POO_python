class Retangulo:

    def __init__(self, h = 1, largura = 1):
        self._altura = None
        self._base = None
        self._area = None

        self.altura = h
        self.base = largura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("Valor informado possui TIPO indesejado")
        elif valor < 1:
            raise ValueError("Valor de base zero ou negativa")
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("Valor informado possui TIPO indesejado")
        elif valor < 1:
            raise ValueError("Valor de altura zero ou negativa")
        else:
            self._altura = valor

    @property
    def area(self):
        return self.base * self.altura

    @area.setter
    def area(self):
        raise PermissionError("Área é um atributo somente leitura e não pode ser alterado diretamente")

    @area.setter
    def area(self):
        raise PermissionError("Área não pode ser configurada por este meio")

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura ={self.altura}\nárea = {self.area}'

    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError("As medidas devem ser informadas em um tupla")
        if len(valores) != 2:
            raise ValueError("Informa uma tupla com 2 valores")
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError("A base deve ser um número")
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError("A altura deve ser um número")