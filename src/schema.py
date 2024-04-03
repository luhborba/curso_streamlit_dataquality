"""Arquivo de Schema de Funcionarios."""
from pydantic import BaseModel, EmailStr, PositiveInt
from datetime import datetime

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