# 🤖 AutoStream AI Agent

## 📌 Overview

AutoStream AI Agent is a conversational AI system designed to assist users with pricing, plans, and policy-related queries. It also detects high-intent users and captures leads interactively.

This project demonstrates a **Retrieval-Augmented Generation (RAG)** approach combined with **agent-based workflow automation**.

---

## 🚀 Features

* 💬 Conversational chatbot interface
* 📊 RAG-based knowledge retrieval from JSON
* 🎯 Intent detection (greeting, pricing, high-intent)
* 🧠 Lead capture workflow (name, email, platform)
* ⚙️ Tool execution (simulated lead storage)

---

## 🗂️ Project Structure

```
inflx-agent-project/
│
├── README.md
├── agent.py
├── rag.py
├── intent.py
├── tools.py
├── main.py
├── requirements.txt
├── .env
├── data/
│   └── knowledge.json
```

---

## ⚙️ How to Run the Project Locally

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/inflx-agent-project.git
cd inflx-agent-project
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Agent

```bash
python main.py
```

---

## 🧪 Sample Test Cases

### Greeting

```
Hi
```

### Pricing Query

```
What is the price of Pro plan?
```

### Policy Query

```
What is your refund policy?
```

### High-Intent Query

```
I want to buy the Pro plan
```

---

## 🎯 Expected Output Flow

```
Agent: What's your name?
User: Swarnim
Agent: Please enter your email:
User: swarnim@gmail.com
Agent: Which platform do you create content on?
User: YouTube

📌 Captured Lead Data: {'name': 'swarnim', 'email': 'swarnim@gmail.com', 'platform': 'youtube'}
✅ Lead captured successfully!
🎉 Our team will contact you soon.
```

---

## 🧠 Architecture Explanation

This project follows a lightweight agent-based architecture with a Retrieval-Augmented Generation (RAG) pipeline.

### Why this approach?

Instead of using heavy frameworks like LangGraph or AutoGen, a simple custom agent is implemented to keep the system easy to understand, debug, and extend.

### Components:

1. **Agent (agent.py)**

   * Handles user interaction
   * Detects intent (greeting, query, high-intent)
   * Routes requests accordingly

2. **RAG Pipeline (rag.py)**

   * Loads knowledge from a JSON file
   * Converts it into searchable text
   * Retrieves relevant answers using keyword matching

3. **Intent Detection**

   * Rule-based keyword detection
   * Identifies high-intent users (buy/subscribe)

4. **Tool Execution (tools.py)**

   * Simulates lead capture
   * Stores user details (name, email, platform)

### State Management

The agent maintains state using:

* `lead_mode` → tracks lead capture stage
* `user_data` → stores collected user inputs

This allows multi-step conversational flow.

---

## 📱 WhatsApp Deployment (Concept)

To integrate this agent with WhatsApp, webhooks can be used along with services like Twilio or Meta WhatsApp Cloud API.

### Workflow:

1. User sends message on WhatsApp
2. Message is forwarded to a backend server (Flask/FastAPI) via webhook
3. Backend passes message to the agent (`handle_input`)
4. Agent processes input and generates response
5. Response is sent back to user via WhatsApp API

### Technologies:

* Flask / FastAPI
* Webhooks
* WhatsApp Cloud API / Twilio

This enables real-time chatbot interaction on WhatsApp.

---

## 🛠️ Tech Stack

* Python 🐍
* JSON (Knowledge Base)
* VS Code
* Basic NLP (Keyword Matching)

---

## 📊 Future Improvements

* Add vector embeddings (FAISS/OpenAI)
* Store leads in a database
* Improve intent detection using ML
* Deploy as a web application

---

## 👨‍💻 Author

Swarnim 

---

## 🎉 Conclusion

This project demonstrates:

* Conversational AI
* RAG-based retrieval
* Agent-driven workflow
* Lead capture automation

It simulates a real-world AI assistant for business use cases.
