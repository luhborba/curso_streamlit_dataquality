import pandas as pd
import streamlit as st

from src.schema import ContratoFuncionarios


def validar(csv):
    """
    Validar o csv.

    Args:
        csv (str): Caminho do arquivo csv.
    """
    try:
        df = pd.read_csv(csv)
        erros = []

        for idx, row in df.iterrows():
            try:
                ContratoFuncionarios(**row.to_dict())
            except Exception as e:
                erros.append(f"Error na Linha:{idx+2} de {e}")

        if erros:
            st.error("Erros encontrados no Arquivo Enviado:")
            for erro in erros:
                st.error(erro)
        else:
            st.success("Arquivo Valido!")
            return True

    except Exception as e:
        st.error(f"Error ao ler o arquivo: {e}")


def main():
    """Função principal."""
    st.set_page_config(page_title="Validador de CSV", layout="wide")
    st.title("Validador de CSV")

    csv = st.file_uploader("Escolha um arquivo CSV para validar", type=["csv"])

    botao = st.button("Validar")

    if botao:
        validar(csv)


if __name__ == "__main__":
    main()
