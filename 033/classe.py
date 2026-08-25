from abc import ABC, abstractmethod
from datetime import datetime


class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = nascimento
        self._idade = None

    @property
    def idade(self) -> int:
        ano_atual = datetime.now().year
        return ano_atual - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError(f"Não pode alterar a idade para {valor} por este meio, altere o ano de nascimento")

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.cursos_oficiais = ["ADM", "RH", "ADS"]

        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, valor):
        if valor in self.cursos_oficiais:
            self._curso = valor
            return self._curso
        else:
            raise ValueError("Curso indisponivel na lista de cursos")

    def add_curso(self, curso:str):
        if curso not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso)
        else:
            return("Curso já existente em na lista de Cursos oficiais")