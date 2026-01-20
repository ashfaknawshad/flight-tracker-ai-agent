# 🚀 Quick Start Guide

## Step 1: Get API Keys

### DeepSeek API (Required)
1. Go to https://platform.deepseek.com/
2. Sign up/Login
3. Create an API key
4. Copy the key

### AviationStack API (Optional but recommended)
1. Go to https://aviationstack.com/signup/free
2. Sign up for FREE tier (100 requests/month)
3. Get your API key from dashboard
4. Copy the key

**Note:** Without AviationStack key, the app will work with demo/sample data.

---

## Step 2: Setup Backend

```bash
cd backend

# Install Python packages
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env file and paste your keys
# On Windows: notepad .env
# On Mac/Linux: nano .env
```

Your `.env` file should look like:
```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx
AVIATIONSTACK_API_KEY=xxxxxxxxxxxxxx
```

---

## Step 3: Setup Frontend

```bash
cd frontend

# Install Node packages
npm install
```

---

## Step 4: Run the Application

### Terminal 1 - Start Backend
```bash
cd backend
python main.py
```

You should see:
```
============================================================
✈️  FLIGHT TRACKER AI AGENT - Backend Server
============================================================
✅ DeepSeek API: Connected
✅ AviationStack API: Connected (Real-time data)

🚀 Server running on: http://localhost:5000
📡 Ready to track flights!
============================================================
```

### Terminal 2 - Start Frontend
```bash
cd frontend
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

---

## Step 5: Test It!

1. Open browser to `http://localhost:5173/`
2. Try these queries:

**Basic queries:**
- "What time is it?"
- "Track flight AA123"
- "Tell me about JFK airport"

**Advanced queries:**
- "Is flight UA456 on time?"
- "Show me all flights from LAX to JFK"
- "What's the status of Chicago O'Hare?"

---

## 🐛 Common Issues

### "No module named 'flask'"
```bash
cd backend
pip install -r requirements.txt
```

### "Cannot find module" (Frontend)
```bash
cd frontend
rm -rf node_modules
npm install
```

### CORS Error
- Make sure backend is running on port 5000
- Check frontend is pointing to http://localhost:5000

### Backend won't start
- Check Python version: `python --version` (should be 3.8+)
- Verify .env file exists in backend folder
- Check DEEPSEEK_API_KEY is set correctly

---

## 🎉 Success!

If everything works, you'll see:
- Beautiful dark theme UI
- Chat interface with flight emoji
- Ability to track flights in real-time

**Pro tip:** The AI is smart! You can ask questions naturally like:
- "Is my flight to New York on time?" (AI will ask for flight number)
- "What airports are near me?" (AI will help you)

Enjoy your Flight Tracker AI Agent! ✈️
