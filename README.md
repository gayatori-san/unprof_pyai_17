## CLI AI Assistant using LLM API

## 📌 Overview

This project is a simple Command Line Interface (CLI) AI Assistant built using either the **OpenAI API** or the **Google Gemini API**.

The assistant accepts a user's prompt from the terminal, sends it to an LLM (Large Language Model), and displays the generated response. It also includes basic error handling for invalid API keys, network issues, and other common API errors.

This project introduces the fundamentals of interacting with Large Language Models through APIs and serves as the first step toward building intelligent AI-powered applications.

---

# 🚀 Features

* Accepts user prompts through the terminal
* Sends requests to an LLM API
* Displays AI-generated responses
* Handles common API errors gracefully
* Uses environment variables for secure API key storage
* Easy to extend into a chatbot or RAG application

---

# 🛠️ Technologies Used

* Python 3.x
* OpenAI API **or** Google Gemini API
* python-dotenv
* requests (if required)
* openai / google-generativeai SDK

---

# 📂 Project Structure

```
Day17-LLM-API/
│
├── assistant.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/gayatori-san/unprof_pyai_17.git

cd unprof
```

---

## 2. Create a Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Setup

## Option 1 — OpenAI API

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Option 2 — Gemini API

Create a `.env` file.

```env
GEMINI_API_KEY=your_api_key_here
```

Never share or upload your API keys to GitHub.

---

# ▶️ Running the Project

```bash
python assistant.py
```

Example:

```
Enter your prompt:

What is Machine Learning?

AI Response:

Machine Learning is a branch of Artificial Intelligence that enables computers to learn from data without being explicitly programmed...
```

---

# 🧠 Concepts Learned

* Large Language Models (LLMs)
* API Integration
* Prompt Engineering Basics
* Tokens and Token Usage
* Request-Response Workflow
* Environment Variables
* Exception Handling

---

# ⚠️ Error Handling

The application gracefully handles situations such as:

* Invalid API key
* Internet connection issues
* API rate limits
* Empty user input
* Unexpected server errors

---

# 📖 Understanding the Workflow

```
User Input
      │
      ▼
CLI Application
      │
      ▼
LLM API (OpenAI / Gemini)
      │
      ▼
AI Generates Response
      │
      ▼
Response Displayed in Terminal
```

---

# 📸 Sample Output

```
=============================
      CLI AI Assistant
=============================

You: Explain Artificial Intelligence.

AI:

Artificial Intelligence (AI) is a field of computer science focused on creating systems capable of performing tasks that typically require human intelligence, such as reasoning, learning, problem-solving, and language understanding.
```

---
# 📚 Learning Outcomes

By completing this project, you will understand:

* How LLM APIs work
* How prompts are sent to AI models
* How responses are generated and parsed
* Secure API key management
* Building the foundation for chatbots and RAG applications

---
