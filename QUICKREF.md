# ✈️ Flight Tracker AI Agent - Quick Reference

## 🎯 What This Does
An AI agent that tracks flights, monitors airports, and provides real-time aviation data using natural language.

## 🔑 API Keys Needed
1. **DeepSeek** (Required): https://platform.deepseek.com/
2. **AviationStack** (Optional): https://aviationstack.com/signup/free
   - Free tier: 100 requests/month
   - Without it: Demo data is used

## 🚀 Quick Start Commands

```bash
# Backend (Terminal 1)
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python main.py

# Frontend (Terminal 2)
cd frontend
npm install
npm run dev
```

## 📱 Try These Commands

| Query | What It Does |
|-------|-------------|
| `Track flight AA123` | Get real-time flight status |
| `Tell me about JFK airport` | Airport information |
| `Flights from LAX to JFK` | Search route |
| `What time is it?` | Current date/time |

## 🏢 Major Airport Codes

| Code | Airport |
|------|---------|
| JFK | New York JFK |
| LAX | Los Angeles |
| ORD | Chicago O'Hare |
| ATL | Atlanta |
| DFW | Dallas/Fort Worth |
| SFO | San Francisco |

## 🛫 Common Airline Codes

| Code | Airline |
|------|---------|
| AA | American Airlines |
| UA | United Airlines |
| DL | Delta Air Lines |
| WN | Southwest Airlines |
| B6 | JetBlue Airways |

## 🔧 Available Tools

The AI agent has access to:
- `get_current_time()` - Returns current date/time
- `track_flight(flight_number)` - Track specific flight
- `get_airport_info(airport_code)` - Airport details
- `search_flights_by_route(dep, arr)` - Route search

## 🎨 UI Features

- **Dark theme** with gradient background
- **Glassmorphism** effects
- **Smooth animations** for messages
- **Responsive design** (mobile-friendly)
- **Real-time updates** as agent processes

## 📁 File Structure

```
ai-agent-with-tools/
├── backend/
│   ├── main.py          # API + Tools
│   ├── requirements.txt # Dependencies
│   └── .env             # Your API keys
├── frontend/
│   └── src/
│       ├── App.tsx      # Main component
│       └── App.css      # Styling
└── README.md            # Full documentation
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Backend won't start | Check Python 3.8+, install requirements |
| Frontend won't start | Check Node 16+, run `npm install` |
| CORS errors | Ensure backend runs on port 5000 |
| No flight data | Check AVIATIONSTACK_API_KEY or use demo mode |

## 📚 Full Docs

- [README.md](README.md) - Complete documentation
- [SETUP.md](SETUP.md) - Detailed setup guide
- [EXAMPLES.md](EXAMPLES.md) - Query examples

## 🎓 How It Works

```
User Message → Frontend → Backend → DeepSeek AI
                                         ↓
                            (AI decides if tools needed)
                                         ↓
                            Execute Python Functions
                                         ↓
                            (Get flight/airport data)
                                         ↓
    Display ← Frontend ← Backend ← AI Response
```

## 💡 Extend It

Add new tools in [main.py](backend/main.py):

```python
def your_tool(param):
    # Your code
    return result

tools_map["your_tool"] = your_tool
# Add to tools_schema too!
```

---

**Made with ❤️ | Happy Flying! ✈️**
