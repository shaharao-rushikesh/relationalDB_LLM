
import streamlit as st
# from langchain import SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
# import langchain.utilities.SQLDatabase
# from langchain import SQLDatabaseChain
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


# Setting up the api key
import environ

env = environ.Env()
environ.Env.read_env()

API_KEY = env('apikey')

# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{env('dbpass')}@localhost:5432/Ecom",
)

# setup llm
llm = ChatOpenAI(temperature=0, openai_api_key=API_KEY, model_name='gpt-3.5-turbo')

# Create query instruction
QUERY = """
Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

{question}
"""

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)


# def run_app():
#     st.title("Interactive SQL Query Assistant")

#     st.sidebar.info("Type your SQL-related questions in the input box.")

#     user_input = st.text_area("Enter your SQL-related question here:")
    
#     if st.button("Submit"):
#         try:
#             question = QUERY.format(question=user_input)
#             result = db_chain.run(question)
#             st.markdown(f"**SQL Query:** {result['SQLQuery']}")
#             st.markdown(f"**SQL Result:** {result['SQLResult']}")
#             st.markdown(f"**Answer:** {result['Answer']}")
#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")


# if __name__ == '__main__':
#     run_app()


def run_app():
    st.title("Interactive SQL Query Assistant")

    st.sidebar.info("Type your SQL-related questions in the input box.")

    user_input = st.text_area("Enter your SQL-related question here:")
    
    if st.button("Submit"):
        try:
            question = QUERY.format(question=user_input)
            result = db_chain.run(question)

            # Assuming result is a list of tuples
            for row in result:
                st.markdown((db_chain.run(question)))

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    run_app()