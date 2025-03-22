import React, { useState } from 'react'
import Loading from './Loading'

function MeditationInput() {
  const [situation, setSituation] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('Submitted situation:', situation)
    
    // Show loading screen
    setIsLoading(true)
    
    // Simulate API call with timeout (replace with actual API call)
    setTimeout(() => {
      // After API call completes, you would handle the response
      // For now, we'll just keep the loading screen for demonstration
      // In a real app, you would redirect to results or handle errors
      // setIsLoading(false) // Uncomment to hide loading after the timeout
    }, 3000)
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
