"""Arquivo de teste do schema definido."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from src.schema import ContratoFuncionarios


def test_validar_contrato():
    """Teste para validar o schema."""
    dados_validos = {
        "id": 1,
        "nome": "Gustavo",
        "idade": 18,
        "datanascimento": datetime.now(),
        "email": "gustavo@email.com",
        "cargo": "Desenvolvedor",
        "departamento": "TI",
    }
    funcionario = ContratoFuncionarios(**dados_validos)

    assert funcionario.id == dados_validos["id"]
    assert funcionario.nome == dados_validos["nome"]
    assert funcionario.idade == dados_validos["idade"]
    assert funcionario.datanascimento == dados_validos["datanascimento"]
    assert funcionario.email == dados_validos["email"]
    assert funcionario.cargo == dados_validos["cargo"]
    assert funcionario.departamento == dados_validos["departamento"]


def test_email_invalidos_contrato_funcionario():
    """Testa se o schema de dados é invalido."""
    dados_invalidos = {
        "id": 1,
        "nome": "Luciano Borba",
        "idade": 23,
        "datanascimento": datetime.now(),
        "email": "luhborbafilho",
        "cargo": "Desenvolvedor Python",
        "departamento": "TI",
    }
    with pytest.raises(ValidationError):
        ContratoFuncionarios(**dados_invalidos)


def test__n_negativo_dados_invalidos():
    """Testa se o schema de dados é invalido."""
    dados_invalidos = {
        "id": -1,
        "nome": "Luciano Borba",
        "idade": 23,
        "datanascimento": datetime.now(),
        "email": "luhborbafilho@gmail.com",
        "cargo": "Desenvolvedor Python",
        "departamento": "TI",
    }
    with pytest.raises(ValidationError):
        ContratoFuncionarios(**dados_invalidos)
