# ⚖️ **Ragster: AI-Powered Legal Assistant**
![Ragster Logo](assets/Ragster_logo.png)

[![GitHub Stars](https://img.shields.io/github/stars/sreekanthpogula/ragster?style=social)](https://github.com/sreekanthpogula/ragster)
[![GitHub Forks](https://img.shields.io/github/forks/sreekanthpogula/ragster?style=social)](https://github.com/sreekanthpogula/ragster/forks)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/license/apache-2-0)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Open%20Source-5e9cff?logo=langchain&logoColor=white)](https://python.langchain.com/docs/introduction/)
[![Crew AI](https://img.shields.io/badge/Crew%20AI-Multi--Agent%20Workflows-00bdaa?style=flat-square)](https://www.crewai.com/)
![GitHub Issues](https://img.shields.io/github/issues/sreekanthpogula/ragster)

### *Bridging the Gap Between People and Legal Access*  🌍

🌐 **Website:** [Ragster](https://Ragster.com/)

**Ragster** is a free, open-source, people-centric initiative 💡 designed to make legal guidance accessible to everyone. Using **AI-powered Retriever-Augmented Generation (RAG)**, **Ragster** delivers quick, accurate legal support tailored to your needs, whether you're seeking information as a layperson or a professional.

> 🛡️ **Mission:** “Justice should be accessible to everyone. Ragster ensures that no one is left behind when it comes to legal knowledge.”

This project is developed by [Sreekanth Pogula](https://github.com/sreekanthpogula) 💼

---

## 📚 **Legal Coverage**

Ragster currently supports the following laws, with plans to expand internationally:

- 🏛️ **The Indian Constitution**
- 📜 **The Bharatiya Nyaya Sanhita, 2023**
- 🚨 **The Bharatiya Nagarik Suraksha Sanhita, 2023**
- 🧾 **The Bharatiya Sakshya Adhiniyam, 2023**
- 📦 **The Consumer Protection Act, 2019**
- 🧭 **The Motor Vehicles Act, 1988**
- 💻 **Information Technology Act, 2000**
- 👧 **The Protection of Children from Sexual Offences Act (POCSO), 2012**
- **The Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013**

**Ragster** aims to cover legal systems from different countries in the near future.

## 💻 **Developer Quick Start Guide**

## Ragster Initial Architecture Overview
```
ragster/
├── config/                  # Configuration directory
│   ├── __init__.py
│   ├── model_config.yaml    # Model-specific configurations
│   ├── prompt_templates.yaml # Prompt templates
│   └── logging_config.yaml  # Logging settings
│
├── assets/                   # Requirements directory
│   ├── Ragster_logo.png      # Logo asset
│   ├── favicon.ico          # Favicon for web app
|
|--database/                # Database directory
│   ├──chroma.sqlite3       # ChromaDB database file
│
├── src/                     # Source code
│   ├── llm/                # LLM clients
│   │   ├── base.py         # Base LLM client
│   │   ├── claude_client.py # Anthropic Claude client
│   │   ├── gpt_client.py   # OpenAI GPT client
│   │   └── utils.py        # Shared utilities
│   │
│   ├── prompt_engineering/ # Prompt engineering tools
│   │   ├── templates.py    # Template management
│   │   ├── few_shot.py    # Few-shot prompt utilities
│   │   └── chain.py       # Prompt chaining logic
│   │
│   ├── utils/             # Utility functions
│   │   ├── rate_limiter.py # API rate limiting
│   │   ├── token_counter.py # Token counting
│   │   ├── cache.py       # Response caching
│   │   └── logger.py      # Logging utilities
│   │
│   └── handlers/          # Error handling
│       └── error_handler.py
│
├── data/                   # Data directory
│   ├── cache/             # Cache storage
│   ├── prompts/           # Prompt storage
│   ├── outputs/           # Output storage
│   └── embeddings/        # Embedding storage
│
├── examples/              # Example implementations
│   ├── basic_completion.py
│   ├── chat_session.py
│   └── chain_prompts.py
│
├── docs/                  # Documentation
│   ├── architecture.md     # Architecture overview
│   ├── usage.md            # Usage guide
│   ├── api.md              # API documentation
│   └── contributing.md      # Contribution guidelines
│
├── notebooks/              # Jupyter notebooks
│   ├── data_preprocessing.ipynb
│   ├── llm_integration.ipynb
│   ├── prompt_testing.ipynb
│   ├── response_analysis.ipynb
│   └── model_experimentation.ipynb
│
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_llm.py         # LLM client tests
│   ├── test_prompt_engineering.py # Prompt engineering tests
│   ├── test_utils.py       # Utility function tests
│   └── test_handlers.py    # Error handler tests
│
├── app.py                 # Main application entry point
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .python-version         # Python version specification
├── .env.example           # Example Environment variables
├── .gitignore             # Git ignore file
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .dockerignore          # Docker ignore file
├── .flake8                # Flake8 configuration for linting
├── .pylintrc              # Pylint configuration for code quality
├── .streamlit/            # Streamlit configuration directory
│   ├── config.toml         # Streamlit configuration file
│   └── secrets.toml         # Streamlit secrets file
├── .vscode/               # Visual Studio Code settings
│   ├── settings.json        # VS Code settings
│   ├── launch.json          # Debugging configuration
│   └── tasks.json           # Task runner configuration
├── .github/               # GitHub workflows and issue templates
│   ├── workflows/           # GitHub Actions workflows
│   │   ├── ci.yml            # Continuous Integration workflow
│   │   └── deploy.yml        # Deployment workflow
│   └── ISSUE_TEMPLATE/       # Issue templates
│       ├── bug_report.md     # Bug report template
│       └── feature_request.md # Feature request template
│
├── setup.py               # Setup script for packaging
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Change log for version history
├── Dockerfile             # Dockerfile for containerization    
└── LICENSE                # License file
```

## 🚀 **Getting Started with Ragster**

Ready to get started? Follow these simple steps to set up **Ragster** on your machine:

1. **Clone the Repository** 🌀
    ```bash
    git clone https://github.com/Ragster/Ragster.git
    ```

2. **Install uv** 📂

    First, let’s install uv and set up our Python project and environment
    
    MacOS/Linux:
      ``` bash 
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```

    Windows:

      ``` bash 
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```
    Make sure to restart your terminal afterwards to ensure that the uv command gets picked up.

3. **Install Dependencies** 📦
    ```bash
    uv sync
    ```

4. **Set Your OpenAI API Key** 🔑

   Open `.env` and add your OpenAI API key:
      ```bash
      OPENAI_API_KEY=your-api-key-here
      ```

5. **Run the Application** 🚀
    ```bash
    uv run streamlit run app.py
    ```

6. **Access the App** 🌐  
    Open your browser and visit:  
    ```bash
    http://127.0.0.1:8501
    ```

---

## 🔧 **Tools & Technologies**

| 💡 **Technology**  | 🔍 **Description**                            |
|--------------------|-----------------------------------------------|
| **LangChain**       | Framework for building language models       |
| **ChromaDB**        | Vector database for RAG implementation       |
| **OpenAI API**      | Powering natural language understanding      |

---

## 🌟 **Future Roadmap**

Exciting developments are planned for **Ragster**! Here’s what’s coming next:

1.  **🤝 Smarter Together: Introducing Our Multi-Agentic Framework 🤖**
    * Imagine a team of specialized AI agents working seamlessly in the background to provide you with the most comprehensive and efficient legal insights. Our new multi-agent framework makes this a reality, boosting platform performance like never before!

2.  **🌎 Law Without Borders: Expanding Our Global Reach 🇨🇦 + More!**
    * Ragster is going global! We're significantly expanding our legal knowledge base to include jurisdictions like Canada and beyond. Soon, you'll have access to a truly worldwide legal resource at your fingertips.

3.  **🗣️ Your Voice is the Key: Introducing Voice Interaction 🎙️**
    * Navigate and access legal information effortlessly with our new voice command feature. Simply speak your queries and let Ragster do the rest – making legal research more intuitive and accessible.

4.  **🌍 Bridging Language Barriers: Multi-Lingual Legal Assistance 🌐**
    * We're committed to serving a global audience. Ragster will soon offer legal assistance in multiple languages, breaking down communication barriers and making our platform truly inclusive.

5.  **🎯 Precision & Personalization: Advanced Search & Tailored Assistance 🔍**
    * Say goodbye to endless scrolling! Our enhanced search engine will pinpoint the exact legal information you need with lightning speed. Plus, enjoy personalized suggestions and assistance crafted just for you.

6.  **✍️ Draft with Confidence: Introducing Legal Document Generation 📄**
    * Need a contract or agreement? Our upcoming legal document generation feature will empower you to create essential legal documents using customizable templates and intuitive user input.

7.  **🗓️ Stay Organized, Stay Ahead: Introducing Case Management 📁**
    * Effortlessly manage your legal matters with our new case management feature. Track crucial deadlines, appointments, and important events all in one centralized location, keeping you in control.

---

## 🤝 **Contribute**

We are always looking for contributors! Whether you want to help with development, report issues, or request features, we welcome you to fork the repo and submit a pull request. Every contribution helps to make **Ragster** better for everyone! see [CONTRIBUTING.md](../CONTRIBUTING.md) for more details.

---

**Ragster** is more than just an AI tool—it's a movement to democratize access to legal knowledge for everyone. Together, let’s make justice truly accessible! ✨

## 📜 **License**

This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for more information.
