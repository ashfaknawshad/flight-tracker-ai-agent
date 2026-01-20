# 🎯 Example Queries & Use Cases

## Basic Time & Info
```
"What time is it?"
"What's the current date and time?"
```

## Flight Tracking

### Track Specific Flights
```
"Track flight AA123"
"Is flight UA456 on time?"
"Show me status of Delta flight DL789"
"Where is American Airlines flight AA100?"
```

**Common Flight Codes:**
- AA = American Airlines
- UA = United Airlines  
- DL = Delta Air Lines
- WN = Southwest Airlines
- B6 = JetBlue Airways

### Real Flight Numbers to Try:
```
"Track flight AA1234" (American Airlines)
"Check status of UA2345" (United Airlines)
"Is DL1001 delayed?" (Delta)
```

## Airport Information

### Major US Airports
```
"Tell me about JFK airport"
"What's the status of LAX?"
"Give me info on Chicago O'Hare"
"Show details for Atlanta airport"
```

**Airport Codes:**
- JFK = New York JFK
- LAX = Los Angeles
- ORD = Chicago O'Hare
- ATL = Atlanta
- DFW = Dallas/Fort Worth
- SFO = San Francisco
- MIA = Miami
- LGA = New York LaGuardia
- BOS = Boston
- SEA = Seattle

### International Airports
```
"Info on London Heathrow" (LHR)
"Tell me about Tokyo Narita" (NRT)
"What about Dubai airport?" (DXB)
```

## Route Searches

### Domestic Routes
```
"Show flights from LAX to JFK"
"Find flights between San Francisco and New York"
"What flights go from Chicago to Miami?"
"List all flights from Seattle to Boston"
```

### Popular Routes
```
"Flights from New York to Los Angeles"
"Show me LAX to ORD flights"
"JFK to SFO route information"
```

## Natural Language Queries

The AI is smart and understands natural language:

```
"I need to fly from Los Angeles to New York, show me options"
"What's happening at O'Hare airport today?"
"Is my flight AA123 going to be late?"
"Can you check if there are any delays at JFK?"
"I'm at LAX, when does the next flight to Chicago leave?"
```

## Complex Multi-Step Queries

```
"Track flight AA123 and tell me about the departure airport"
"What time is it and is flight UA456 on time?"
"Show me LAX airport info and flights to JFK"
```

## Creative Queries

```
"I'm traveling to New York tomorrow, what airport should I fly into?"
"What's the difference between JFK and LGA?"
"Help me find the fastest route from San Francisco to Miami"
"Which airport has more flights, LAX or ORD?"
```

## Demo Mode (Without API Key)

If you don't have AviationStack API key, the agent will use demo data:

```
✅ Works: "Track flight AA123" → Returns demo data
✅ Works: "LAX airport info" → Returns demo data
✅ Works: "Flights from JFK to LAX" → Returns demo data
```

## Tips for Best Results

1. **Use IATA Codes** when possible (AA123, JFK, LAX)
2. **Be specific** with flight numbers (include airline code + number)
3. **Ask naturally** - the AI understands context
4. **Combine queries** - ask multiple things in one message

## Example Conversation Flow

```
You: "What time is it?"
Agent: "It's 3:45 PM, January 20, 2026"

You: "Track flight AA123"
Agent: "Flight AA123 Status:
        ✈️ Status: ON TIME
        📍 Route: Los Angeles (LAX) → New York (JFK)
        🛫 Departure: 2:30 PM
        🛬 Arrival: 10:45 PM
        🚪 Gate: A12"

You: "Tell me about JFK airport"
Agent: "Airport Information:
        🏢 Name: John F. Kennedy International Airport
        📍 Location: New York, United States
        🗺️ IATA Code: JFK
        ⏰ Timezone: America/New_York"

You: "Show me flights from LAX to JFK"
Agent: "Flights from LAX to JFK:
        
        1. AA123 - Departs: 2:30 PM - Status: On Time
        2. UA456 - Departs: 4:15 PM - Status: On Time
        3. DL789 - Departs: 6:00 PM - Status: Delayed
        ..."
```

## Try These Now! 🚀

Copy and paste these into your agent:

1. `Track flight AA123`
2. `What's the status of JFK airport?`
3. `Show me flights from LAX to ORD`
4. `Tell me about Chicago O'Hare`
5. `What time is it and is flight UA456 on time?`

Have fun exploring! ✈️
