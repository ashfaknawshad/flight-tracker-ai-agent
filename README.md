# ✈️ Flight Tracker AI Agent

An intelligent AI agent that provides real-time flight tracking, airport information, and aviation intelligence powered by DeepSeek AI and AviationStack API.

[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/ashfaknawshad/flight-tracker-ai-agent)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/ashfaknawshad/flight-tracker-ai-agent/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/ashfaknawshad/flight-tracker-ai-agent)

## 🚀 Features

- **Real-time Flight Tracking** - Track any flight by flight number (e.g., AA123, UA456)
- **Airport Information** - Get detailed airport info, status, and timezone
- **Route Search** - Find all flights between two airports
- **Smart AI Agent** - AI automatically decides when to use tools to answer your questions
- **Modern UI** - Beautiful glassmorphism design with dark mode

## 🛠️ Tech Stack

**Backend:**
- Python + Flask
- DeepSeek AI (LLM with function calling)
- AviationStack API (flight data)

**Frontend:**
- React + TypeScript
- Vite
- Modern CSS with animations

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashfaknawshad/flight-tracker-ai-agent.git
cd flight-tracker-ai-agent
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your API keys
# DEEPSEEK_API_KEY=your_key_here (Required)
# AVIATIONSTACK_API_KEY=your_key_here (Optional - uses demo data if not provided)
```

**Get API Keys:**
- **DeepSeek API**: https://platform.deepseek.com/ (Required)
- **AviationStack API**: https://aviationstack.com/signup/free (Optional - FREE 100 requests/month)

### 3. Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install
```

## 🚀 Running the Application

### Terminal 1 - Backend
```bash
cd backend
python main.py
```
Backend will run on `http://localhost:5000`

### Terminal 2 - Frontend
```bash
cd frontend
npm run dev
```
Frontend will run on `http://localhost:5173`

## 💬 Example Queries

Try asking the AI agent:

- "Track flight AA123"
- "What's the status of JFK airport?"
- "Show me flights from LAX to JFK"
- "Is flight UA456 on time?"
- "Tell me about Chicago O'Hare airport"
- "What time is it?"

The AI will automatically determine which tools to use!

## 📦 Project Structure

```
ai-agent-with-tools/
├── backend/
│   ├── main.py              # Flask API + tool definitions
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # Environment variables (create this)
│   └── .env.example         # Template for .env
├── frontend/
│   ├── src/
│   │   ├── App.tsx          # React main component
│   │   ├── App.css          # Styling
│   │   └── main.tsx         # Entry point
│   ├── package.json         # Node dependencies
│   └── vite.config.ts       # Vite configuration
└── README.md
```

## 🔑 How It Works

1. **User sends a message** through the React frontend
2. **Backend forwards to DeepSeek AI** with tool definitions
3. **AI analyzes the query** and decides if tools are needed
4. **If tools needed:**
   - AI calls the appropriate function (track_flight, get_airport_info, etc.)
   - Backend executes the Python function
   - Results sent back to AI for final response
5. **Response displayed** in the chat interface

## 🎨 Customization

### Add More Tools

Edit [backend/main.py](backend/main.py):

```python
def your_new_tool(param):
    """Tool description"""
    # Your code here
    return result

# Add to tools_map
tools_map = {
    "your_new_tool": your_new_tool,
    # ... existing tools
}

# Add to tools_schema
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "your_new_tool",
            "description": "Description for AI",
            "parameters": {
                "type": "object",
                "properties": {
                    "param": {"type": "string"}
                },
                "required": ["param"]
            }
        }
    }
]
```

### Modify UI Theme

Edit [frontend/src/App.css](frontend/src/App.css) - change CSS variables:

```css
:root {
  --bg-dark: #0f0f23;
  --accent-blue: #3b82f6;
  --accent-green: #10b981;
  /* ... modify colors */
}
```

## 🐛 Troubleshooting

**Backend won't start:**
- Check if Python 3.8+ is installed: `python --version`
- Verify DEEPSEEK_API_KEY is set in `.env`
- Install dependencies: `pip install -r requirements.txt`

**Frontend won't start:**
- Check if Node.js 16+ is installed: `node --version`
- Clear cache: `rm -rf node_modules && npm install`

**CORS errors:**
- Ensure backend is running on port 5000
- Check frontend is using `http://localhost:5000/chat`

**AviationStack not working:**
- Free tier has limits (100 requests/month)
- App will use demo data if API key is missing
- Verify API key is correct in `.env`

## 📝 License

MIT License - feel free to use this project for learning or commercial purposes!

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new tools
- Improve UI/UX
- Fix bugs
- Add tests

## 🙏 Credits

- DeepSeek AI for the LLM
- AviationStack for flight data
- React + Vite for frontend framework

---

**Repository:** [github.com/ashfaknawshad/flight-tracker-ai-agent](https://github.com/ashfaknawshad/flight-tracker-ai-agent)

Made with ❤️ by [Ashfak Nawshad](https://github.com/ashfaknawshad)
