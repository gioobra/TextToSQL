
# 🧠 Talk To SQL: Talk to Your Databases in Natural Language

An interactive web app built with Streamlit and LangChain that translates Portuguese questions into SQL queries, letting you talk directly to PostgreSQL and MySQL databases.

## 🚀 Overview

This project democratizes data access by removing the need for SQL expertise. Using large language models (LLMs) through the Google Gemini API and the LangChain framework, the tool acts as an intelligent translator:

1. **You ask:** "Quantos alunos estão matriculados em Ciencia da Computacao?"
2. **The AI translates:** Generates `SELECT COUNT(id_aluno) FROM matriculas WHERE id_curso = 1;`
3. **The app executes:** Sends the query to the connected database.
4. **You get the answer:** The result is displayed clearly.

## ✨ Key Features

- Multi-database support: Easily connect to PostgreSQL and MySQL servers.
- Interactive connection: Secure UI to enter credentials (host, user, password) and pick a target database from a dynamically populated list.
- SQL query visibility: See the exact SQL command generated for each question to ensure transparency and learning.
- Logical schema diagram: View your database structure with an auto-generated ER diagram to understand tables and relationships.
- Friendly UI: Clean, intuitive interface built with Streamlit.

## 🛠️ Tech Stack

- Frontend: Streamlit
- Backend and AI orchestration: Python, LangChain
- Language model (LLM): Google Gemini Pro via API
- Databases: PostgreSQL, MySQL
- Schema visualization: Graphviz

## ⚙️ Run the Project Locally

Follow these steps to set up and run the app on your machine.

1. Prerequisites
   - Python 3.9+
   - Git
   - Access to a PostgreSQL and/or MySQL server
2. Clone the repository
   - `git clone https://github.com/gioobra/TextToSQL`
   - `cd TextToSQL`
3. Set up a virtual environment (recommended to isolate dependencies)

   ```shell
   python -m venv .venv

   # Activate the environment
   # On Linux or macOS:
   source .venv/bin/activate
   # On Windows:
   .\.venv\Scripts\activate
   ```

4. Install dependencies
   Create a `requirements.txt` file with the content below and then run the install command.

   ```shell
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

   Installation command:

   ```shell
   pip install -r requirements.txt
   ```

5. Configure the API key
   1. Create a file named `.env` at the project root.
   2. Add your Google Gemini API key inside it:
      `GOOGLE_API_KEY="YOUR_API_KEY_HERE"`
   You can obtain a free key from Google AI Studio.
6. Run the app
   With the virtual environment active, start Streamlit:
   `streamlit run main.py`
   Your browser will open automatically with the app running.

## 👨‍💻 How to Use

1. Open the app in your browser.
2. In the left sidebar, choose the database type (PostgreSQL or MySQL).
3. Enter your server credentials (host, user, and password).
4. Click "Connect to Server."
5. If the connection succeeds, a new dropdown appears. Select the database you want to chat with.
6. On the right column, a database schema diagram is displayed.
7. On the left column, type your question in Portuguese in the text area and click "Ask."
8. Below, you will see the generated SQL query and the database response.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

*Made with ❤️ to make data work easier for everyone.*
