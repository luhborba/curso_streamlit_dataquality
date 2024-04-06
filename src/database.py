from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Funcionarios(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    datanascimento = Column(DateTime)
    email = Column(String)
    cargo = Column(String)
    departamento = Column(String)


def criar_sessao():
    engine = create_engine("sqlite:///funcionarios.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
