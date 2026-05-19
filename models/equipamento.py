# Equipamento: representar equipamentos cadastrados.

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Equipamento(ABC):
    id: int
    nome: str
    disponivel: bool

    @abstractmethod
    def calcular_multa(self, dias_atraso):
        pass


@dataclass
class Camera(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 8)


@dataclass
class CaixaSom(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 4)
