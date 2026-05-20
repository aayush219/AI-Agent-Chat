# AI Agent Chat

A **conversational AI chatbot built with Python using LangChain and Google Gemini**. It features real-time web search integration via the **Tavily API** and isolates communication contexts using custom **conversation threads** backed by a persistent local database.

---

## 🚀 Features

* **LangChain Integration:** Orchestrates LLMs, custom tools, and context components seamlessly.
* **Google Gemini LLM:** Powering natural language understanding and text generation.
* **Real-time Web Search:** Utilises the [Tavily Search API](https://tavily.com) to pull accurate, live information directly from the web.
* **Thread-based Memory Isolation:** Tracks independent chat histories uniquely via Thread IDs to eliminate data bleed between sessions.
* **Persistent SQLite Backend:** Chat logs and contextual memory tokens are securely saved locally inside `chatbot_memory.db`.

---

## 📁 Repository Structure

```text
├── .vscode/               # Editor workspace configurations
├── .gitignore             # Git exclusion rules 
├── chatbot_memory.db      # SQLite database storing threaded histories
├── google_gemini.py       # Configuration and setup for the Gemini model
├── main.py                # Main chatbot application entry point
└── requirement.txt        # Python package dependencies
```

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com
cd AI-Agent-Chat
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root project directory and populate it with your private keys:

```env
# Google Gemini API configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Tavily Web Search API configuration
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## 💻 Usage

Run the primary script to initiate a new session with your AI agent:

```bash
python main.py
```

### Interacting with Threads
The database will automatically map and separate messages based on unique thread flags. When building chat scripts or hitting endpoints, remember to pass a distinct `thread_id` keyword argument inside your LangChain config parameters:

```python
config = {"configurable": {"thread_id": "user_session_123"}}
# pass config alongside user query inputs to your agent executor
```

---

## 🧰 Tech Stack

* **Language:** Python
* **Framework:** LangChain
* **LLM Provider:** Google Gemini
* **Search Engine Tool:** Tavily Search API
* **Database Backend:** SQLite 

---

## 📄 License

This project is open-source. Check the repository files for specific licensing details.
