🧠 Talk To SQL: Converse com seus Bancos de Dados em Linguagem NaturalUma aplicação web interativa construída com Streamlit e LangChain que traduz perguntas em português para consultas SQL, permitindo que você converse diretamente com seus bancos de dados PostgreSQL e MySQL.(Dica: Grave um GIF rápido ou tire um screenshot da sua aplicação em funcionamento e substitua o link acima)🚀 Visão GeralEste projeto tem como objetivo democratizar o acesso a dados, eliminando a necessidade de conhecimento técnico em SQL para realizar consultas. Utilizando o poder dos Grandes Modelos de Linguagem (LLMs) através da API do Google Gemini e do framework LangChain, esta ferramenta atua como um tradutor inteligente:Você pergunta: "Quantos alunos estão matriculados em Ciência da Computação?"A IA traduz: Gera o comando SELECT COUNT(id_aluno) FROM matriculas WHERE id_curso = 1;A aplicação executa: Envia a consulta para o banco de dados conectado.Você recebe a resposta: O resultado da consulta é exibido de forma clara e legível.✨ Principais FuncionalidadesSuporte a Múltiplos Bancos de Dados: Conecte-se facilmente a servidores PostgreSQL e MySQL.Conexão Interativa: Interface segura que permite ao usuário inserir suas credenciais (host, usuário, senha) e escolher o banco de dados alvo de uma lista populada dinamicamente.Visualização da Consulta SQL: Veja exatamente qual comando SQL foi gerado pela IA para cada pergunta, promovendo transparência e aprendizado.Diagrama Lógico do Esquema: Visualize a estrutura do seu banco de dados com um diagrama de Entidade-Relacionamento gerado automaticamente, facilitando a compreensão das tabelas e suas relações.Interface Amigável: Interface limpa e intuitiva construída com Streamlit.🛠️ Tecnologias UtilizadasFrontend: StreamlitBackend & Orquestração de IA: Python, LangChainModelo de Linguagem (LLM): Google Gemini Pro via APIBancos de Dados: PostgreSQL, MySQLVisualização de Esquema: Graphviz⚙️ Como Executar o Projeto LocalmenteSiga estes passos para configurar e rodar a aplicação na sua máquina.1. Pré-requisitosPython 3.9+GitAcesso a um servidor PostgreSQL e/ou MySQL.2. Clonar o Repositóriogit clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
3. Configurar o Ambiente VirtualÉ altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente
# No Linux ou macOS:
source .venv/bin/activate
# No Windows:
.\.venv\Scripts\activate
4. Instalar as DependênciasCrie um ficheiro requirements.txt com o conteúdo abaixo e depois execute o comando de instalação.requirements.txt:streamlit
langchain
langchain-community
langchain-experimental
langchain-google-genai
sqlalchemy
psycopg2-binary
mysql-connector-python
python-dotenv
graphviz
Comando de instalação:pip install -r requirements.txt
5. Configurar a Chave de APICrie um ficheiro chamado .env na raiz do projeto.Adicione sua chave da API do Google Gemini a este ficheiro:GOOGLE_API_KEY="SUA_API_KEY_AQUI"
Você pode obter uma chave gratuita no Google AI Studio.6. Executar a AplicaçãoCom o ambiente virtual ativado, inicie o servidor do Streamlit:streamlit run app.py
Seu navegador abrirá automaticamente com a aplicação em execução!👨‍💻 Como UsarAbra a aplicação no seu navegador.Na barra lateral esquerda, escolha o tipo de banco de dados (PostgreSQL ou MySQL).Preencha as credenciais do seu servidor (Host, Usuário e Senha).Clique em "Conectar ao Servidor".Se a conexão for bem-sucedida, um novo menu suspenso aparecerá. Escolha o banco de dados com o qual deseja conversar.Na coluna da direita, um diagrama do esquema do banco de dados será exibido.Na coluna da esquerda, digite sua pergunta em português na área de texto e clique em "Perguntar".Abaixo, a consulta SQL gerada e a resposta do banco de dados serão exibidas.📄 LicençaEste projeto está sob a licença MIT. Veja o ficheiro LICENSE para mais detalhes.Feito com ❤️ para facilitar a vida de quem trabalha com dados.
