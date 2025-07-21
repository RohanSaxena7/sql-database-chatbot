##CREATING THE STREAMLIT WEB APP

#importing libraries
import streamlit as st
from pathlib import Path #to get our absolute path
from langchain.agents import create_sql_agent #for constructing a LLM able to generate and execute SQL queries on a database using our instructions.
from langchain.sql_database import SQLDatabase #Provides a wrapper class to connect language models to an SQL database
from langchain.agents.agent_types import AgentType #Enumerates different types of agents available in LangChain
from langchain.callbacks import StreamlitCallbackHandler #Bridges Streamlit apps and LangChain agents, allowing real-time feedback and streaming outputs
from langchain.agents.agent_toolkits import SQLDatabaseToolkit #A toolkit that combines LLMs with SQLDatabase objects
from sqlalchemy import create_engine #Establishes a connection to various SQL databases with a single call
import sqlite3 #provides an interface for interacting with SQLite databases directly
from langchain_groq import ChatGroq
import os

#Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = st.secrets["LANGCHAIN_TRACING_V2"]
os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]

#Setting the page configuration of streamlit
st.set_page_config(page_title= "LangChain: SQL DB ChatBot", page_icon= "💻")
#Setting the page title
st.title("SQL DB ChatBot using LangChain💻")

#global variables
LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

#Creating radio options to allow user to use student.db or use their own databse
radio_opt = ["Use SQLite 3 Database - Student.db", "Connect to your MySQL Database"]
selected_opt = st.sidebar.radio(label= "Choose the database you wish to access", options= radio_opt)

#ito allow the user to connect to their database
if radio_opt.index(selected_opt)==1:
    db_uri = MYSQL
    #ask the user to provide their database link
    mysql_host = st.sidebar.text_input("Provide your MySQL Host")
    #ask them to provide their username
    mysql_user = st.sidebar.text_input("Provide MySQL User")
    #ask for the password
    mysql_password = st.sidebar.text_input("Provide MySQL Password", type= "password")
    #ask the database name
    mysql_db = st.sidebar.text_input("Provide Database name")
#if they choose to use the student.db database
else:
    db_uri = LOCALDB

#api_key  
api_key = st.sidebar.text_input(label="Enter your Groq API Key:", type="password")
    
#if database not provided or chosen
if not db_uri:
    st.info("Please enter the database information and the uri")

#if api key not entered
if not api_key:
    st.info("Please enter your Groq API Key")
    st.stop()
    
##LLM model
llm = ChatGroq(api_key=api_key, model="gemma2-9b-It", streaming = True)

##configure
@st.cache_resource(ttl="2h") #for 2 hours we will keep the database in our streamlit cache, so we dont have to load again
def configure_db(db_uri, mysql_host = None, mysql_user = None, mysql_password = None, mysql_db = None):
    #if we are using localdb
    if db_uri==LOCALDB:
        dbfilepath = (Path(__file__).parent/"student.db").absolute() #getting the abosulate path of the database
        print(dbfilepath) #to see the path
        #connecting the filepath via sqlite3, mode is read only
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri= True)
        return SQLDatabase(create_engine("sqlite:///", creator = creator))
    #if the user wants to give their own database
    elif db_uri == MYSQL:
        #checking if all the information is provided by the user, if not we show an error
        if not (mysql_db and mysql_host and mysql_password and mysql_user):
            st.error("Please provide all the details to connect to your MySQL database!")
            st.stop()
        #if details are there we connect to their server, mysqlconnector will connect to the mysql workbench, this is how we connect
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))
    
if db_uri == MYSQL:
    db = configure_db(db_uri= db_uri, mysql_host= mysql_host, mysql_db= mysql_db, mysql_password= mysql_password, mysql_user= mysql_user)
else:
    db = configure_db(db_uri) #for localdb
    
##toolkit - tools to interact with our database
toolkit = SQLDatabaseToolkit(db = db, llm = llm) #setting the toolkit to use our configured database and our llm model

#creating an agent
agent = create_sql_agent(
    llm= llm,
    toolkit= toolkit,
    verbose= True, #because we want to see the interactions
    agent_type= AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

#creating session state
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content":"Hi, How can I help you?"}]
    
#appending everything in chat_message
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
#user query
user_query = st.chat_input(placeholder="Ask anything from the database")

#append session state and the user message
if user_query:
    st.session_state.messages.append({"role":"user", "content": user_query}) 
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container()) #to show the chain of throughts of our chatbot
        response = agent.run(user_query, callbacks=[streamlit_callback])
        #append the response
        st.session_state.messages.append({"role":"assistant", "content": response})
        st.write(response) #to display this response by assistant
