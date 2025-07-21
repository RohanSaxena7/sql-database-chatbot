# 💻 LangChain SQL Database ChatBot

A powerful, interactive chatbot built with **LangChain**, **Groq's LLM**, and **Streamlit**. Query your own database—either the bundled SQLite demo (`student.db`) or any MySQL instance—using plain English. Powered by generative AI, the assistant converts your question into SQL, runs it, and replies conversationally, complete with real-time agent reasoning.

**App Link**: _[Deploy on Streamlit Cloud]_

## 🚀 Features

- 🔗 **Connects to Your Database:**
    - Use the included `student.db` SQLite or connect instantly to any MySQL database with your credentials.
- 🧠 **Natural Language Queries:**
    - Ask any question in plain English—get meaningful, data-backed answers.
- 🤖 **LLM-Powered Agent:**
    - Integrates Groq’s Gemma2-9b LLM with LangChain agents for zero-shot SQL generation.
- 🧩 **Real-Time Thoughts \& Explanations:**
    - See exactly how the AI thinks via `StreamlitCallbackHandler`.
- 🔐 **No Hardcoded Secrets:**
    - Secure Groq API and database credentials via sidebar input or Streamlit secrets.
- 🗂️ **Session-Based Chat Memory:**
    - Keeps your chat history for the session; clear anytime.

## 📦 Requirements

Before running or deploying, make sure you have:

- **Python 3.10.x** (recommended: 3.10.17 for Streamlit compatibility)
- **pip** (Python package manager)
- **Groq API Key** ([Sign up here](https://console.groq.com))
- (Optional for MySQL): MySQL server credentials (host, user, password, database name)


## 🏗️ How It Works

1. **User launches the app** via Streamlit (locally or in the cloud).
2. **Choose your database:**
    - Use the built-in `student.db` sample, or
    - Connect to your own MySQL database by entering details in the sidebar.
3. **Enter your Groq API key** in the sidebar.
4. **Ask questions** in the chat—e.g., "List all students in the Computer Science major".
5. **Behind the scenes:**
    - The LLM interprets your question, generates valid SQL, and safely queries your chosen database.
    - Results are replied back conversationally—with agent "thoughts" visible in real time for full transparency.

## 📝 Usage Instructions

1. **Clone this repository:**

```sh
git clone https://github.com/yourusername/langchain-sql-chatbot.git
cd langchain-sql-chatbot
```

2. **Install requirements:**

```sh
pip install -r requirements.txt
```

3. **Add API secrets (for local use):**
    - _Preferred_: Use the sidebar to input the Groq API key at runtime.
    - _For LangChain LangSmith tracking (optional)_: Add your LangSmith keys in Streamlit Cloud “Secrets”.
4. **(Optional)** Ensure `student.db` is present in the project folder.
_To use your own database, just select the option and enter credentials on the web app sidebar._
5. **Run the application:**

```sh
streamlit run app.py
```

6. **On the Web App:**
    - Select your database mode (SQLite demo or MySQL).
    - Enter your credentials and API key.
    - Start chatting!

## ⚙️ Configuration

- **requirements.txt**

```
streamlit>=1.29.0
langchain>=0.1.0
langchain-community>=0.0.21
langchain-groq>=0.0.4
sqlalchemy>=2.0.0
mysql-connector-python>=8.0.32
```

- **Secrets (Streamlit Cloud)**:
Add these in your app's “Secrets” if deploying with LangSmith tracking:

```
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=SQL_CHATBOT
```

- **Python version:** 3.10.17 (recommended, see Streamlit/PyPI support notes).


## 🧩 LangSmith Tracing (Optional)

- Built-in support for LangSmith run tracking—just set your LangSmith secrets.
- Project traces will appear under `SQL_CHATBOT` in your LangSmith dashboard.


## 🖥 Sample User Flow

1. **Open app:** “Choose database” — pick SQLite demo for a quick start.
2. **Sidebar:** Paste your Groq API key.
3. **Chat:**
    - Ask: _“Show me 3 students who secured the top 3 marks.”_
    - Watch the agent’s reasoning unfold.
    - Get results in chat form.
4. **Switch to MySQL:** Connect instantly to your custom database for real-world application.
   

## ❓ FAQ

**Is my data secure?**

- Yes! Credentials are never logged or hardcoded. All queries are parameterized for safety.

**Can I use my own database?**

- Absolutely—just choose “MySQL” and enter info in the sidebar.

**What if my database is huge?**

- For very large datasets, results are paginated and summarized when possible.


## 📚 Resources

- [Groq API Sign Up](https://console.groq.com)
- [LangChain Documentation](https://python.langchain.com/docs/)
- [Streamlit Documentation](https://docs.streamlit.io)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

