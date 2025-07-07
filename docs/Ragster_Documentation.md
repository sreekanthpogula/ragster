# Ragster Documentation
 
**Ragster** is an AI-powered legal assistant designed to streamline access to legal information. Built using Retriever-Augmented Generation (RAG), Ragster leverages modern AI and NLP techniques to provide concise, relevant answers to legal queries, aiming to make legal knowledge more accessible to everyone.
 
---
 
## Table of Contents
 
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
 
---
 
## Overview
 
Ragster provides a free, open-source platform that simplifies legal research by retrieving and presenting legal information in an easy-to-understand manner. Currently focused on Indian laws, Ragster enables users to get concise responses to complex legal queries using a combination of machine learning, natural language processing, and vector embeddings.
 
The long-term goal is to expand Ragster to cover international laws and make it a global legal AI assistant.
 
## Features
 
- **AI-Powered Legal Assistance**: Provides quick, accurate responses to legal questions.
- **Retriever-Augmented Generation (RAG)**: Uses RAG to gather relevant legal information from a vast legal corpus.
- **Open Source**: Completely free and open for contributions from the community.
- **Multi-Platform Access**: Responsive design suitable for mobile and web platforms.
- **Extendable Architecture**: Can be expanded to other legal systems in the future.
 
## Technologies Used
 
- **Python**: Core programming language for backend development.
- **LangChain**: For building conversational AI pipelines and managing RAG workflows.
- **ChromaDB**: Vector database (using `db_legal_database`) to manage legal document embeddings and facilitate information retrieval.
- **Django**: Web framework for structuring backend API.
- **Streamlit**: Interface for running the application prototype.
- **HTML/CSS**: Frontend for styling and responsive UI design.
 
## Installation
 
	Follow these steps to set up and run Ragster locally.
 
	1. **Clone the Repository**:
	   ```bash
	   git clone https://github.com/sreekanthpogula/ragster.git
	   cd ragster
	   ```
	2. **Create a Virtual Environment**:
 
		```bash
			python -m venv env
			source env/bin/activate   # For Linux/macOS
			env\Scripts\activate      # For Windows
		```
	3. **Install Requirements**:
 
		```bash
		pip install -r requirements.txt
		```
	4. **Set up ChromaDB**: Ensure ```chroma_db_legal_database``` is properly configured for managing the embeddings and retrieval.
 
	5. **Run the Streamlit App**:
		```bash
		streamlit run app.py
		```
	6. **Access Ragster**: Open the URL provided by Streamlit in your terminal to view the application.
 
## Usage
 
- **Ask Legal Questions**: Users can type in legal questions related to Indian law, and Ragster will retrieve relevant responses.
- **Review Relevant Context**: Ragster provides contextual information to ensure accuracy.
- **Contribute Feedback**: Users are encouraged to provide feedback, which helps improve the AI model’s accuracy and relevance.
 
## Project Structure
 
- `app.py`: Contains the Streamlit code that runs the main interface for Ragster.
- `Ragster_main.py`: Core RAG retrieval code handling the interaction with ChromaDB and LangChain.
- `chroma_db_legal_database/`: Directory for ChromaDB database managing the legal document embeddings.
- `requirements.txt`: List of Python dependencies.
 
## Future Enhancements
 
- **International Law Support**: Extend support to other legal systems.
- **Enhanced Conversational Capabilities**: Improve the AI’s conversational abilities for more dynamic interactions.
- **User Account Management**: Allow users to create accounts and save query history.
- **Advanced Analytics**: Integrate analytics to monitor popular queries and trends.
 
## Contributing
We welcome contributions to Ragster! If you have ideas for improvements or new features, please follow these steps:
 [Contributing Guide](../CONTRIBUTING.md)
 
## License

This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for more information.

## Contact
For any inquiries or feedback, please reach out at sreekanthpogula2001@gmail.com
