# 🏗️ Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         USER                                 │
│                    (Web Browser)                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   FRONTEND                                   │
│              React + TypeScript + Vite                       │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  App.tsx (Chat Interface)                            │  │
│  │  - Message display                                   │  │
│  │  - Input handling                                    │  │
│  │  - HTTP requests to backend                          │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  App.css (Styling)                                   │  │
│  │  - Glassmorphism design                              │  │
│  │  - Dark theme                                        │  │
│  │  - Animations                                        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  Port: 5173                                                 │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ POST /chat
                         │ {message: "Track flight AA123"}
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND                                   │
│                  Flask + Python                              │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  main.py                                             │  │
│  │                                                       │  │
│  │  1. Receive user message                            │  │
│  │  2. Forward to DeepSeek AI                          │  │
│  │  3. Process tool calls                              │  │
│  │  4. Return response                                 │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  Port: 5000                                                 │
└────────────┬───────────────────────┬────────────────────────┘
             │                       │
             │ API Request           │ Tool Execution
             ▼                       ▼
┌─────────────────────┐   ┌─────────────────────────────────┐
│   DEEPSEEK AI       │   │   TOOL FUNCTIONS                │
│                     │   │                                 │
│ - Function calling  │   │  ┌───────────────────────────┐ │
│ - Natural language  │   │  │ get_current_time()        │ │
│ - Context aware     │   │  │ → Returns date/time       │ │
│                     │   │  └───────────────────────────┘ │
│ Model: deepseek-chat│   │  ┌───────────────────────────┐ │
└─────────────────────┘   │  │ track_flight(number)      │ │
                          │  │ → Calls AviationStack API │ │
                          │  └───────────────────────────┘ │
                          │  ┌───────────────────────────┐ │
                          │  │ get_airport_info(code)    │ │
                          │  │ → Calls AviationStack API │ │
                          │  └───────────────────────────┘ │
                          │  ┌───────────────────────────┐ │
                          │  │ search_flights_by_route() │ │
                          │  │ → Calls AviationStack API │ │
                          │  └───────────────────────────┘ │
                          └────────────┬────────────────────┘
                                       │
                                       │ HTTP Request
                                       ▼
                          ┌─────────────────────────────────┐
                          │   AVIATIONSTACK API             │
                          │                                 │
                          │  - Real-time flight data        │
                          │  - Airport information          │
                          │  - Route searches               │
                          │                                 │
                          │  Free tier: 100 req/month      │
                          └─────────────────────────────────┘
```

## Request Flow Example

### Example: "Track flight AA123"

```
1. USER TYPES
   └─> "Track flight AA123"

2. FRONTEND (App.tsx)
   └─> POST http://localhost:5000/chat
       Body: {message: "Track flight AA123"}

3. BACKEND (main.py)
   └─> Receives request
   └─> Calls DeepSeek AI with message + tool definitions

4. DEEPSEEK AI
   └─> Analyzes: "User wants flight tracking"
   └─> Decides: "Use track_flight tool"
   └─> Returns: tool_call {
         name: "track_flight",
         arguments: {flight_number: "AA123"}
       }

5. BACKEND (main.py)
   └─> Executes: track_flight("AA123")
   └─> Function makes HTTP request to AviationStack

6. AVIATIONSTACK API
   └─> Returns flight data:
       {
         flight_status: "active",
         departure: {...},
         arrival: {...}
       }

7. BACKEND (main.py)
   └─> Formats result
   └─> Sends back to DeepSeek AI with tool result

8. DEEPSEEK AI
   └─> Generates natural language response:
       "Flight AA123 is currently on time. 
        It departed from LAX at 2:30 PM..."

9. BACKEND (main.py)
   └─> Returns JSON response to frontend

10. FRONTEND (App.tsx)
    └─> Displays message in chat interface
    └─> Shows with green border + animation
```

## Data Flow Diagram

```
┌──────┐      ┌─────────┐      ┌─────────┐      ┌──────────┐      ┌────────┐
│ User │ ───> │ React   │ ───> │ Flask   │ ───> │ DeepSeek │ ───> │ Tools  │
│      │ ←─── │ Frontend│ ←─── │ Backend │ ←─── │    AI    │ ←─── │ (APIs) │
└──────┘      └─────────┘      └─────────┘      └──────────┘      └────────┘
  Chat         HTTP             JSON              Function          External
  Input        Request          Processing        Calling           Data
```

## Technology Stack

### Frontend Layer
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool & dev server
- **CSS3** - Modern styling with animations

### Backend Layer
- **Python 3.8+** - Programming language
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin requests
- **OpenAI SDK** - DeepSeek API client
- **Requests** - HTTP library for external APIs

### AI Layer
- **DeepSeek Chat** - LLM with function calling
- **Function Calling** - Tool use capability

### Data Layer
- **AviationStack API** - Flight & airport data
- **REST API** - Communication protocol

## Security Considerations

```
┌─────────────────────────────────────────────┐
│ Environment Variables (.env)                │
│                                             │
│  ✓ API keys stored securely                │
│  ✓ Not committed to git                    │
│  ✓ Loaded at runtime only                  │
│                                             │
│  DEEPSEEK_API_KEY=xxxxx                    │
│  AVIATIONSTACK_API_KEY=xxxxx               │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ CORS Configuration                          │
│                                             │
│  ✓ Allows frontend-backend communication   │
│  ✓ Restricts unauthorized access           │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ Request Validation                          │
│                                             │
│  ✓ Type checking with TypeScript           │
│  ✓ Error handling in Python                │
│  ✓ Timeout on API requests (10s)           │
└─────────────────────────────────────────────┘
```

## Deployment Options

### Development (Current)
```
Frontend: localhost:5173
Backend:  localhost:5000
```

### Production Options

1. **Separate Hosting**
   - Frontend: Vercel/Netlify
   - Backend: Heroku/Railway/Render

2. **Monolithic**
   - Flask serves React build
   - Single deployment

3. **Containerized**
   - Docker Compose
   - Frontend + Backend containers

## Performance Characteristics

| Component | Latency | Notes |
|-----------|---------|-------|
| Frontend Render | <100ms | React instant updates |
| HTTP Request | 10-50ms | Local network |
| DeepSeek AI | 1-3s | Depends on response length |
| AviationStack API | 100-500ms | External API call |
| **Total Response** | **1.5-4s** | Typical query |

## Scalability

### Current Limits
- **DeepSeek**: Rate limits per account
- **AviationStack Free**: 100 requests/month
- **Flask Dev**: Single-threaded

### Scale Up Options
- Upgrade AviationStack tier
- Use production WSGI server (Gunicorn)
- Add caching (Redis)
- Load balancing for multiple instances

---

**This architecture provides:**
- ✅ Clear separation of concerns
- ✅ Easy to extend with new tools
- ✅ Maintainable codebase
- ✅ Scalable foundation
