"""Arquivo de Schema de Funcionarios."""

from datetime import datetime

from pydantic import BaseModel, EmailStr, PositiveInt


class ContratoFuncionarios(BaseModel):
    """
    Classe responsável pelo contrato de dados do Funcionário.

    Args:
        id (PositiveInt): ID do Funcionário.
        nome (str): Nome do Funcionário.
        idade (PositiveInt): Idade do Funcionário.
        datanascimento (datetime): Data de Nascimento do Funcionário.
        email (EmailStr): Email do Funcionário.
        cargo (str): Cargo do Funcionário.
        departamento (str): Departamento do Funcionário.
    """

    id: PositiveInt
    nome: str
    idade: PositiveInt
    datanascimento: datetime
    email: EmailStr
    cargo: str
    departamento: str
