// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [generatedText, setGeneratedText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGenerate = async () => {
    setLoading(true);
    setError(null);
    setGeneratedText('');

    try {
      const response = await axios.post('http://localhost:8000/generate', {
        prompt: prompt,
        max_length: 100
      });

      setGeneratedText(response.data.generated_text);
    } catch (err) {
      setError('Error generating text. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Text Generation LLM</h1>
      </header>
      <main>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt here..."
          rows={4}
          cols={50}
        />
        <br />
        <button onClick={handleGenerate} disabled={loading || !prompt}>
          {loading ? 'Generating...' : 'Generate Text'}
        </button>
        {error && <p className="error">{error}</p>}
        {generatedText && (
          <div className="output">
            <h2>Generated Text:</h2>
            <p> {generatedText} </p>
            
          </div>
        )}
      </main>
    </div>
  );
}

export default App;