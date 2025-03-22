import React, { useState } from 'react'
import Loading from './Loading'

function MeditationInput() {
  const [situation, setSituation] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log('Submitted situation:', situation)
    
    // Show loading screen
    setIsLoading(true)
    
    try {
      const response = await fetch('http://localhost:5000/api/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: situation
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('API Response:', data);
      
      // Here you would handle the response data
      // For example, redirect to a results page or display the meditation
      
    } catch (error) {
      console.error('Error:', error);
      // Here you would handle any errors
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <div className="input-container">
      {isLoading && <Loading />}
      <form onSubmit={handleSubmit}>
        <textarea
          value={situation}
          onChange={(e) => setSituation(e.target.value)}
          placeholder="Describe your situation..."
          rows="4"
          className="meditation-input"
          disabled={isLoading}
        />
        <button 
          type="submit" 
          className="submit-button"
          disabled={isLoading}
        >
          Create Meditation
        </button>
      </form>
    </div>
  )
}

export default MeditationInput
