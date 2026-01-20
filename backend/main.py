import os
import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Retrieve the keys from environment variables
api_key = os.getenv("DEEPSEEK_API_KEY")
aviation_api_key = os.getenv("AVIATIONSTACK_API_KEY")

if not api_key:
    raise ValueError("No DEEPSEEK_API_KEY found. Check your backend/.env file!")

if not aviation_api_key:
    print("⚠️  Warning: No AVIATIONSTACK_API_KEY found. Flight tracking features will use demo data.")
    print("Get a free API key at: https://aviationstack.com/signup/free")

client = OpenAI(
    api_key=api_key, 
    base_url="https://api.deepseek.com"
)

# --- TOOL DEFINITIONS ---
def get_current_time():
    """Get the current time"""
    return datetime.now().strftime("%I:%M %p, %B %d, %Y")

def track_flight(flight_number):
    """Track a specific flight by flight number (e.g., AA123, UA456)"""
    if not aviation_api_key:
        return f"Demo: Flight {flight_number} - Status: On Time, Departure: 2:30 PM, Arrival: 5:45 PM, Gate: A12"
    
    try:
        url = "http://api.aviationstack.com/v1/flights"
        params = {
            'access_key': aviation_api_key,
            'flight_iata': flight_number
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if not data.get('data'):
            return f"Flight {flight_number} not found. Please check the flight number."
        
        flight = data['data'][0]
        flight_info = flight.get('flight', {})
        departure = flight.get('departure', {})
        arrival = flight.get('arrival', {})
        
        status = flight.get('flight_status', 'Unknown')
        dep_airport = departure.get('airport', 'Unknown')
        arr_airport = arrival.get('airport', 'Unknown')
        dep_time = departure.get('scheduled', 'Unknown')
        arr_time = arrival.get('scheduled', 'Unknown')
        
        return f"""Flight {flight_number} Status:
✈️ Status: {status.upper()}
📍 Route: {dep_airport} → {arr_airport}
🛫 Departure: {dep_time}
🛬 Arrival: {arr_time}
🚪 Gate: {departure.get('gate', 'TBA')}"""
    except Exception as e:
        return f"Error tracking flight: {str(e)}"

def get_airport_info(airport_code):
    """Get information about an airport using IATA code (e.g., JFK, LAX, ORD)"""
    if not aviation_api_key:
        return f"Demo: {airport_code} Airport - Status: Operational, Avg Delay: 15 min, Weather: Clear"
    
    try:
        url = "http://api.aviationstack.com/v1/airports"
        params = {
            'access_key': aviation_api_key,
            'search': airport_code
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if not data.get('data'):
            return f"Airport {airport_code} not found."
        
        airport = data['data'][0]
        return f"""Airport Information:
🏢 Name: {airport.get('airport_name', 'Unknown')}
📍 Location: {airport.get('city_iata_code', 'Unknown')}, {airport.get('country_name', 'Unknown')}
🗺️ IATA Code: {airport.get('iata_code', 'Unknown')}
⏰ Timezone: {airport.get('timezone', 'Unknown')}"""
    except Exception as e:
        return f"Error fetching airport info: {str(e)}"

def search_flights_by_route(departure_code, arrival_code):
    """Search for flights between two airports using IATA codes (e.g., JFK to LAX)"""
    if not aviation_api_key:
        return f"Demo: Found 5 flights from {departure_code} to {arrival_code}. Next departures: 2:30 PM, 4:15 PM, 6:00 PM"
    
    try:
        url = "http://api.aviationstack.com/v1/flights"
        params = {
            'access_key': aviation_api_key,
            'dep_iata': departure_code,
            'arr_iata': arrival_code
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if not data.get('data'):
            return f"No flights found from {departure_code} to {arrival_code}"
        
        flights = data['data'][:5]  # Get first 5 flights
        result = f"Flights from {departure_code} to {arrival_code}:\n\n"
        
        for idx, flight in enumerate(flights, 1):
            flight_info = flight.get('flight', {})
            departure = flight.get('departure', {})
            result += f"{idx}. {flight_info.get('iata', 'N/A')} - Departs: {departure.get('scheduled', 'N/A')} - Status: {flight.get('flight_status', 'Unknown')}\n"
        
        return result
    except Exception as e:
        return f"Error searching flights: {str(e)}"

# Map names to functions
tools_map = {
    "get_current_time": get_current_time,
    "track_flight": track_flight,
    "get_airport_info": get_airport_info,
    "search_flights_by_route": search_flights_by_route
}

# --- TOOL SCHEMA FOR AI ---
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current date and time",
        }
    },
    {
        "type": "function",
        "function": {
            "name": "track_flight",
            "description": "Track a specific flight in real-time by its flight number (IATA code). Use format like AA123, UA456, DL789.",
            "parameters": {
                "type": "object",
                "properties": {
                    "flight_number": {
                        "type": "string",
                        "description": "The flight number in IATA format (e.g., AA123, UA456)"
                    }
                },
                "required": ["flight_number"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_airport_info",
            "description": "Get detailed information about an airport including location, timezone, and current status using its IATA code (3-letter code like JFK, LAX, ORD)",
            "parameters": {
                "type": "object",
                "properties": {
                    "airport_code": {
                        "type": "string",
                        "description": "The IATA airport code (e.g., JFK, LAX, ORD, ATL)"
                    }
                },
                "required": ["airport_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_flights_by_route",
            "description": "Search for all flights between two airports. Provide departure and arrival airport IATA codes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure_code": {
                        "type": "string",
                        "description": "Departure airport IATA code (e.g., JFK, LAX)"
                    },
                    "arrival_code": {
                        "type": "string",
                        "description": "Arrival airport IATA code (e.g., LAX, ORD)"
                    }
                },
                "required": ["departure_code", "arrival_code"]
            }
        }
    }
]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    # 1. Ask AI if it needs a tool
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_input}],
        tools=tools_schema
    )
    
    message = response.choices[0].message
    tool_calls = message.tool_calls

    # 2. If the AI wants to call a tool
    if tool_calls:
        results = []
        for tool in tool_calls:
            func_name = tool.function.name
            func_args = json.loads(tool.function.arguments)
            
            # Execute the actual Python function
            result = tools_map[func_name](**func_args)
            results.append(result)
        
        # 3. Send the tool result back to AI for final answer
        final_response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": user_input},
                message,
                {"role": "tool", "tool_call_id": tool.id, "content": str(results)}
            ]
        )
        return jsonify({"response": final_response.choices[0].message.content})

    return jsonify({"response": message.content})

if __name__ == '__main__':
    print("=" * 60)
    print("✈️  FLIGHT TRACKER AI AGENT - Backend Server")
    print("=" * 60)
    print(f"✅ DeepSeek API: Connected")
    if aviation_api_key:
        print(f"✅ AviationStack API: Connected (Real-time data)")
    else:
        print(f"⚠️  AviationStack API: Using demo data")
        print(f"   Get free API key: https://aviationstack.com/signup/free")
    print(f"\n🚀 Server running on: http://localhost:5000")
    print(f"📡 Ready to track flights!\n")
    print("=" * 60)
    app.run(port=5000, debug=True)