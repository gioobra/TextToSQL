import streamlit as st
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text, inspect as sql_inspect
import graphviz
import re
import ast

# A importação correta
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Carrega as variáveis de ambiente
load_dotenv()

# --- FUNÇÃO: Para desenhar o esquema do banco de dados ---
def display_logical_schema(db_uri):
    """
    Cria e exibe um diagrama lógico do banco de dados usando Graphviz.
    """
    try:
        engine = create_engine(db_uri)
        inspector = sql_inspect(engine)
        
        dot = graphviz.Digraph(
            'database_schema', 
            comment='Esquema do Banco de Dados',
            graph_attr={'rankdir': 'LR', 'splines': 'ortho'}
        )
        dot.attr('node', shape='record', style='rounded', fontname='Arial')
        dot.attr('edge', arrowsize='0.7')

        table_names = inspector.get_table_names()

        for table_name in table_names:
            columns_str = f"{{ {table_name} |"
            columns = inspector.get_columns(table_name)
            for column in columns:
                columns_str += f" {column['name']} ({column['type']}) \\l"
            columns_str += "}}"
            dot.node(table_name, columns_str)

            fks = inspector.get_foreign_keys(table_name)
            for fk in fks:
                dot.edge(table_name, fk['referred_table'])

        st.graphviz_chart(dot)
        
    except Exception as e:
        st.error(f"Não foi possível gerar o diagrama do esquema: {e}")

# --- Configurações Iniciais da Página ---
st.set_page_config(
    page_title="Talk to SQL",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Talk To SQL: Converse com seus Bancos de Dados")
st.caption("Insira as credenciais, conecte-se, escolha um banco de dados e faça sua pergunta!")

# --- Inicialização do Session State ---
if 'db_list' not in st.session_state:
    st.session_state.db_list = []
if 'sql_generation_chain' not in st.session_state:
    st.session_state.sql_generation_chain = None
if 'db_connection' not in st.session_state:
    st.session_state.db_connection = None
if 'db_uri' not in st.session_state:
    st.session_state.db_uri = ""
if 'sql_query' not in st.session_state:
    st.session_state.sql_query = ""
if 'sql_result' not in st.session_state:
    st.session_state.sql_result = ""

# --- Barra Lateral para Configuração da Conexão ---
with st.sidebar:
    st.header("⚙️ Configuração da Conexão")
    db_type = st.selectbox(
        "1. Escolha o tipo de Banco de Dados:",
        ("PostgreSQL", "MySQL"),
        key="db_type_selector"
    )
    
    db_host = st.text_input("Host do Banco de Dados", value="localhost")
    db_user = st.text_input("Usuário")
    db_password = st.text_input("Senha", type="password")
    
    if st.button("Conectar ao Servidor"):
        with st.spinner("Conectando e buscando bancos de dados..."):
            try:
                st.session_state.db_list = []
                st.session_state.sql_generation_chain = None
                
                if db_type == "PostgreSQL":
                    temp_uri = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/postgres"
                    query = "SELECT datname FROM pg_database WHERE datistemplate = false;"
                else: # MySQL
                    temp_uri = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}"
                    query = "SHOW DATABASES;"

                engine = create_engine(temp_uri)
                with engine.connect() as connection:
                    result = connection.execute(text(query))
                    st.session_state.db_list = [row[0] for row in result if row[0] not in ['information_schema', 'performance_schema', 'mysql', 'sys', 'postgres', 'template0', 'template1']]
                
                st.success("Conectado! Escolha um banco de dados abaixo.")
            
            except Exception as e:
                st.error(f"Falha na conexão: {e}")
                st.session_state.db_list = []

    if st.session_state.db_list:
        selected_db = st.selectbox(
            "2. Escolha o Banco de Dados para conversar:",
            st.session_state.db_list,
            index=None,
            placeholder="Selecione um banco de dados..."
        )
        
        if selected_db:
            if db_type == "PostgreSQL":
                st.session_state.db_uri = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{selected_db}"
            else: # MySQL
                st.session_state.db_uri = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{selected_db}"
            
            try:
                prompt_template_text = f"""Dada a seguinte pergunta, crie uma consulta SQL para {db_type} que a responda. Retorne APENAS a consulta SQL e nada mais.

**Instruções Críticas:**
1. Retorne APENAS o comando SQL.
2. Não inclua texto explicativo como "Aqui está a consulta:".
3. Não envolva a consulta em blocos de código markdown como ```sql.

Com base no esquema de tabela abaixo, escreva uma consulta SQL que responda à pergunta do usuário.

Esquema:
{{table_info}}

Pergunta: {{input}}
Sua consulta SQL:"""
                
                # CORREÇÃO APLICADA AQUI e modelo atualizado
                llm = GoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0) 
                
                prompt = PromptTemplate(
                    input_variables=["input", "table_info"],
                    template=prompt_template_text,
                )

                db_connection = SQLDatabase.from_uri(st.session_state.db_uri)
                
                st.session_state.sql_generation_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
                st.session_state.db_connection = db_connection
                
                st.success(f"Pronto para conversar com o banco '{selected_db}'!")
            except Exception as e:
                st.error(f"Não foi possível preparar o assistente para este DB: {e}")
                st.session_state.sql_generation_chain = None
                st.session_state.db_connection = None

# --- Interface Principal (dividida em duas colunas) ---
col1, col2 = st.columns(2)

with col1:
    st.header("🔍 Consultar")
    if st.session_state.sql_generation_chain:
        question = st.text_area("Faça sua pergunta sobre o banco de dados:", height=100)
        
        if st.button("Perguntar", type="primary"):
            st.session_state.sql_query = ""
            st.session_state.sql_result = ""
            
            with st.spinner("1. Gerando SQL... 🧠"):
                try:
                    table_info = st.session_state.db_connection.get_table_info()
                    raw_sql_response = st.session_state.sql_generation_chain.run(input=question, table_info=table_info)
                    
                    clean_sql = re.sub(r"```sql|```", "", raw_sql_response).strip()
                    st.session_state.sql_query = clean_sql
                    
                    with st.spinner("2. Executando consulta... ⚙️"):
                        raw_result_str = st.session_state.db_connection.run(clean_sql)
                        
                        try:
                            result_list = ast.literal_eval(raw_result_str)
                            
                            if isinstance(result_list, list) and len(result_list) > 0:
                                formatted_result = "\n".join([f"- {item[0]}" for item in result_list])
                            elif isinstance(result_list, list) and len(result_list) == 0:
                                formatted_result = "A consulta não retornou resultados."
                            else:
                                formatted_result = str(result_list)
                        except (ValueError, SyntaxError):
                            formatted_result = raw_result_str

                        st.session_state.sql_result = formatted_result

                except Exception as e:
                    st.error(f"Ocorreu um erro: {e}")
                    st.session_state.sql_query = "Erro na geração ou execução."
                    st.session_state.sql_result = ""
        
        if st.session_state.sql_query:
            with st.expander("Ver Consulta SQL Gerada", expanded=True):
                st.code(st.session_state.sql_query, language="sql")
        
        if st.session_state.sql_result:
            st.subheader("Resposta")
            st.markdown(st.session_state.sql_result)

    else:
        st.info("👈 Por favor, conecte-se a um banco de dados na barra lateral para começar.")

with col2:
    st.header("🏛️ Esquema do Banco de Dados")
    if st.session_state.db_uri:
        display_logical_schema(st.session_state.db_uri)
    else:
        st.info("Conecte-se a um banco de dados para ver o esquema.")
