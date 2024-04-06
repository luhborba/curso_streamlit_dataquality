from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Funcionarios(Base):
    """
    Classe de Funcionários utilizando a ORM SQLAlchemy.

    Args:
        id (int): ID do Funcionário.
        nome (str): Nome do Funcionário.
        idade (int): Idade do Funcionário.
        datanascimento (datetime): Data de Nascimento do Funcionário.
        email (str): Email do Funcionário.
        cargo (str): Cargo do Funcionário.
        departamento (str): Departamento do Funcionário.
    """
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    datanascimento = Column(DateTime)
    email = Column(String)
    cargo = Column(String)
    departamento = Column(String)


def criar_sessao():
    """Função de Conexão com o Banco de Dados."""
    engine = create_engine("sqlite:///funcionarios.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
