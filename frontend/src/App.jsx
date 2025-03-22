import './App.css'
import React from 'react'
import MeditationInput from './components/MeditationInput'

function App() {
  return (
    <div className="app-container">
      <div className="logo-container">
        <div className="logo">LUMA</div>
      </div>
      <div className="content-container">
        <MeditationInput />
      </div>
      <div className="wave-bg"></div>
    </div>
  )
}

export default App
