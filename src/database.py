from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
    engine = create_engine('sqlite:///funcionarios.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()