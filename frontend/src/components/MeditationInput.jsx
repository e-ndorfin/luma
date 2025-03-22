import React, { useState, useEffect } from 'react'
import Loading from './Loading'
import MeditationOutput from './MeditationOutput'

function MeditationInput() {
  const [situation, setSituation] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [showOutput, setShowOutput] = useState(false)

  // Use useEffect to monitor state changes
  useEffect(() => {
    console.log('State updated - isLoading:', isLoading, 'showOutput:', showOutput)
  }, [isLoading, showOutput])

  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log('Form submitted with situation:', situation)
    
    // Show loading screen
    setIsLoading(true)
    
    console.log('Loading screen activated')
    
    // Create a clearly named timeout reference
    const timeoutId = setTimeout(() => {
      console.log('Timeout fired after 3 seconds')
      
      // First hide the loading screen
      setIsLoading(false)
      
      // Then show the output screen
      setTimeout(() => {
        setShowOutput(true)
        console.log('Output screen should now be visible')
      }, 50) // Small delay to ensure state updates properly
    }, 3000)
    
    // Log that the timeout has been set
    console.log('Timeout set with ID:', timeoutId)
    
    // Commented out API call for future implementation
    /*
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
    }
    */
  }

  // Log every render
  console.log('Rendering component with states:', { isLoading, showOutput })
  
  // Simplified conditional rendering
  return (
    <div className="input-container">
      {isLoading && <Loading />}
      {showOutput && <MeditationOutput />}
      {!isLoading && !showOutput && (
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
      )}
    </div>
  )
}

export default MeditationInput
