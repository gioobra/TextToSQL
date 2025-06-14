import streamlit as st
from dotenv import load_dotenv
import os

from langchain_community.utilities import SQLDatabase
from langchain_google_genai import GoogleGenerativeAI
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()

st.set_page_config(
    page_title="Talk to SQL",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Talk to SQL: Converse com seus Bancos de Dados")
st.caption("Escolha um banco de dados, escreva uma pergunta e eu a transformarei em SQL!")

with st.sidebar:
    st.header("Configurações")
    db_type = st.selectbox(
        "Escolha o tipo de Banco de Dados:",
        ("PostgresSQL", "MySQL")
    )

db = None
try:
    if db_type == "PostgresSQL":
        db_uri = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}".format(
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT"),
            db=os.getenv("PG_DB")
        )
    else:
        db_uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST"),
            port=os.getenv("MYSQL_PORT"),
            db=os.getenv("MYSQL_DB")
        )
    db = SQLDatabase.from_uri(db_uri)
    st.sidebar.success("Banco de Dados {db_type} carregado com sucesso!")

except Exception as e:
    st.sidebar.error(f"Erro ao carregar o banco de dados: {e}")
    st.stop()

llm = GoogleGenerativeAI(model="gemini-pro", temperature=0)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

question = st.text_input("Sua pergunta:", placeholder="Ex: Quantos alunos existem no total?")

if st.button("Perguntar", type="primary"):
    if question:
        with st.spinner("Consultando o banco de dados..."):
            try:
                result = db_chain.run(question)
                st.success("Aqui está sua resposta:")
                st.write(result)
            except Exception as e:
                st.error(f"Ocorreu um erro ao consultar o banco de dados: {e}")
    else:
        st.warning("Por favor, insira uma pergunta.")

with st.expander("Ver esquema do Banco de Dados conectado"):
    st.text(db.get_table_info())        


    
