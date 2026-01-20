import { useState } from 'react';
import './App.css';

// Learning Theory: Interfaces define the "shape" of our data
interface Message {
  role: 'user' | 'assistant';
  content: string;
}

interface ChatResponse {
  response: string;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const sendMessage = async (): Promise<void> => {
    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };
    const updatedMessages = [...messages, userMessage];
    
    setMessages(updatedMessages);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });
      
      const data: ChatResponse = await response.json();
      
      const assistantMessage: Message = { role: 'assistant', content: data.response };
      setMessages([...updatedMessages, assistantMessage]);
    } catch (error) {
      console.error("Error connecting to backend:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <header>
        <h1>✈️ Flight Tracker AI Agent</h1>
        <p>Real-time flight tracking, airport status & aviation intelligence</p>
      </header>
      
      <div className="message-list">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.role}`}>
            <strong>{msg.role === 'user' ? '👤 You' : '🤖 Agent'}:</strong>
            <p>{msg.content}</p>
          </div>
        ))}
        {isLoading && <div className="loading">✈️ Agent is tracking flights...</div>}
      </div>

      <div className="input-area">
        <input 
          value={input} 
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => setInput(e.target.value)}
          onKeyDown={(e: React.KeyboardEvent) => e.key === 'Enter' && sendMessage()}
          placeholder="Ask about flights, airports, or routes..."
        />
        <button onClick={sendMessage} disabled={isLoading}>
          {isLoading ? '✈️' : 'Send'}
        </button>
      </div>
    </div>
  );
}

export default App;