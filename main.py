import pandas as pd
import streamlit as st
from datetime import datetime

from src.schema import ContratoFuncionarios
from src.database import criar_sessao, Funcionarios


def validar_e_inserir_no_banco(csv, session):
    """
    Função de Validar o arquivo em formato csv e inserir dados no Banco de Dados.

    Args:
        csv (str): Caminho do arquivo csv.
        session (Session): Sessão do SQLAlchemy.
    """
    try:
        df = pd.read_csv(csv)
        erros = []
        dados_validos = []

        for idx, row in df.iterrows():
            try:
                ContratoFuncionarios(**row.to_dict())
                row['datanascimento'] = datetime.strptime(row['datanascimento'], '%Y-%m-%d')
                dados_validos.append(Funcionarios(**row.to_dict()))
            except Exception as e:
                erros.append(f"Error na Linha:{idx+2} de {e}")

        if erros:
            st.error("Erros encontrados no Arquivo Enviado:")
            for erro in erros:
                st.error(erro)
        else:
            session.add_all(dados_validos)
            session.commit()
            st.success("Arquivo Valido e Dados Inseridos no Banco de Dados!")
            return True

    except Exception as e:
        st.error(f"Error ao ler o arquivo: {e}")


def main():
    """Função principal."""
    st.set_page_config(page_title="Validador de CSV", layout="wide")
    st.title("Validador de CSV")
    session = criar_sessao()

    csv = st.file_uploader("Escolha um arquivo CSV para validar", type=["csv"])

    botao = st.button("Validar")

    if botao:
        validar_e_inserir_no_banco(csv, session)


if __name__ == "__main__":
    main()
