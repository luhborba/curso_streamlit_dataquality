"""Arquivo de Schema de Funcionarios."""

from datetime import datetime

from pydantic import BaseModel, EmailStr, PositiveInt


class ContratoFuncionarios(BaseModel):
    """
    Classe responsável pelo contrato de dados do Funcionário.
    """

    id: PositiveInt
    nome: str
    idade: PositiveInt
    datanascimento: datetime
    email: EmailStr
    cargo: str
    departamento: str
