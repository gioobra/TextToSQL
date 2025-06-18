
# 🧠 Talk To SQL: Converse com seus Bancos de Dados em Linguagem Natural

Uma aplicação web interativa construída com Streamlit e LangChain que traduz perguntas em português para consultas SQL, permitindo que você converse diretamente com seus bancos de dados PostgreSQL e MySQL.

## 🚀 Visão Geral

Este projeto tem como objetivo democratizar o acesso a dados, eliminando a necessidade de conhecimento técnico em SQL para realizar consultas. Utilizando o poder dos Grandes Modelos de Linguagem (LLMs) através da API do Google Gemini e do framework LangChain, esta ferramenta atua como um tradutor inteligente:

1. **Você pergunta:** "Quantos alunos estão matriculados em Ciência da Computação?"
2. **A IA traduz:** Gera o comando ``SELECT COUNT(id_aluno) FROM matriculas WHERE id_curso = 1;``
3. **A aplicação executa:** Envia a consulta para o banco de dados conectado.
4. **Você recebe a resposta:** O resultado da consulta é exibido de forma clara e legível.

## ✨ Principais Funcionalidades

- Suporte a Múltiplos Bancos de Dados: Conecte-se facilmente a servidores PostgreSQL e MySQL.
- Conexão Interativa: Interface segura que permite ao usuário inserir suas credenciais (host, usuário, senha) e escolher o banco de dados alvo de uma lista populada dinamicamente.
- Visualização da Consulta SQL: Veja exatamente qual comando SQL foi gerado pela IA para cada pergunta, promovendo transparência e aprendizado.
- Diagrama Lógico do Esquema: Visualize a estrutura do seu banco de dados com um diagrama de Entidade-Relacionamento gerado automaticamente, facilitando a compreensão das tabelas e suas relações.
- Interface Amigável: Interface limpa e intuitiva construída com Streamlit.
  
## 🛠️ Tecnologias Utilizadas

- Frontend: Streamlit
- Backend & Orquestração de IA: Python, LangChainModelo de Linguagem (LLM): Google Gemini Pro via API
- Bancos de Dados: PostgreSQL, MySQL
- Visualização de Esquema: Graphviz

## ⚙️ Como Executar o Projeto Localmente

Siga estes passos para configurar e rodar a aplicação na sua máquina.

1. Pré-requisitos
   - Python 3.9+
   - GitAcesso a um servidor PostgreSQL e/ou MySQL.
2. Clonar o Repositório
   ``git clone https://github.com/gioobra/TextToSQL``
   ``cd TextToSQL``
3. Configurar o Ambiente Virtual
    -É altamente recomendado usar um ambiente virtual para isolar as dependências do  projeto.

    ```#shell
    # Criar o ambiente virtual
    python -m venv .venv

    # Ativar o ambiente
    # No Linux ou macOS:
    source .venv/bin/activate
    # No Windows:
    .\.venv\Scripts\activate
    ```

4. Instalar as Dependências
    Crie um arquivo ```requirements.txt``` com o conteúdo abaixo e depois execute o comando de instalação.

    ```#shell
    streamlit
    langchain
    langchain-community
    langchain-experimental
    langchain-google-genai
    sqlalchemy
    psycopg2-binary
    mysql-connector-python
    python-dotenv
    graphviz
    ```

    Comando de instalação:
    ```pip install -r requirements.txt```

5. Configurar a Chave de API
   1. Crie um arquivo chamado ```.env``` na raiz do projeto.
   2. Adicione sua chave da API do Google Gemini dentro dele:
      ``GOOGLE_API_KEY="SUA_API_KEY_AQUI"``
    Você pode obter uma chave gratuita no Google AI Studio.
6. Executar a Aplicação
   Com o ambiente virtual ativado, inicie o servidor do Streamlit:
   ``streamlit run main.py``
    Seu navegador abrirá automaticamente com a aplicação em execução!

## 👨‍💻 Como Usar

1. Abra a aplicação no seu navegador.
2. Na barra lateral esquerda, escolha o tipo de banco de dados (PostgreSQL ou MySQL).
3. Preencha as credenciais do seu servidor (Host, Usuário e Senha).
4. Clique em "Conectar ao Servidor".
5. Se a conexão for bem-sucedida, um novo menu suspenso aparecerá. Escolha o banco de dados com o qual deseja conversar.
6. Na coluna da direita, um diagrama do esquema do banco de dados será exibido.
7. Na coluna da esquerda, digite sua pergunta em português na área de texto e clique em "Perguntar".
8. Abaixo, a consulta SQL gerada e a resposta do banco de dados serão exibidas.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

*Feito com ❤️ para facilitar a vida de quem trabalha com dados.*
