# relationalDB_LLM

# Relational Database Query System with Natural Language Interface

## Problem Statement

The challenge is to develop a system that empowers a computer to comprehend and respond to user queries about relational databases using natural language. This involves extracting the database structure through SQL queries, generating and executing SQL queries based on user input, and presenting the results in a coherent and understandable format.

## Proposed Solution

### Schema Retrieval

- Utilize SQL queries to retrieve the database schema.
- Extract information such as available tables, keys, relations, and the total number of records using automated methods.

### Input Preparation

- Combine the user query and the retrieved schema information into a prompt.
- Ensure the prompt is structured for effective communication with the Large Language Model (LLM).

### LLM Interaction

- Present the prepared prompt to the LLM (e.g., ChatGPT).
- Allow the LLM to generate an SQL query based on the user query and provided schema information.

### SQL Query Execution

- Execute the generated SQL query on the relational database.

### Result Retrieval

- Obtain the output of the SQL query from the database.

### NLG Interaction

- Send the SQL query result to the LLM for natural language generation (NLG).
- Convert the structured database output into a coherent natural language response.

### Output Presentation

- Display the natural language response generated by the LLM to the user on the screen.

## Getting Started

To get started with the Relational Database Query System, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Configure the database connection details in the `config.json` file.
4. Run the main application script.

## Usage

1. Input a natural language query about the relational database.
2. The system will interact with the LLM to generate an SQL query.
3. Execute the SQL query on the database and retrieve the results.
4. Convert the structured database output into a coherent natural language response using NLG.
5. Display the response to the user.

## Repository Information

This repository is organized to facilitate a seamless understanding and implementation of the Relational Database Query System. Here's a breakdown of the key components:

- **`main` Folder:** Contains the core logic of the system in the `main.py` file. This is where the primary functionality and processing occur.

- **`.env` File:** Before running the application, make sure to add your GPT API key and the local SQL DBMS password to the `.env` file. This ensures secure and authorized access to the required services.

- **`app.py` File:** In this file, a Streamlit UI will be implemented, providing a user-friendly interface for interacting with the system.

- **`db.py` File:** This file is dedicated to handling SQL operations, ensuring efficient and organized management of database interactions.

- **`Pipfile`:** Lists the necessary dependencies for the project. Run `pip install pipenv` and then `pipenv install` to set up the virtual environment with the required packages.

Feel free to explore and contribute to the project, enhancing its functionality and usability. If you encounter any issues or have suggestions, please open an issue or submit a pull request. Your contributions are highly valued!

**Note:** Make sure to adhere to the security measures by appropriately configuring the `.env` file before running the application.

## Contributions

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.
