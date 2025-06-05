# Gemini AI Chatbot

This is my first AI chatbot project! 🚀  
It uses the Gemini API to generate responses and is built with FastAPI and a simple HTML/JS frontend.  
I'm learning about agentic AI and how to build AI-powered applications.

## Features

- Chat with Gemini AI in real time
- Modern, responsive web UI
- Powered by FastAPI backend
- Uses Google Gemini API for responses

## Setup

1. **Clone the repository**  
   ```sh
   git clone [<your-repo-url>](https://github.com/daniyalquest/agent-1.git)
   cd agent-1
   ```

2. **Set up your API key**  
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

3. **Run the app**  
   ```sh
   uvicorn main:app --reload
   ```
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Project Structure

```
agent-1/
│
├── main.py              # FastAPI backend
├── src/
│   └── ai_agent.py      # Gemini API integration
├── static/
│   └── index.html       # Frontend UI
├── requirements.txt
└── .env                 # Your API key (not committed)
```

## Learning Goals

- Understand how to connect a web UI to an AI backend
- Learn to use FastAPI and Google Gemini API
- Explore agentic AI concepts

---

*Made with ❤️ while learning agentic AI!*
