import React from 'react'
import './Loading.css'

function Loading() {
  return (
    <div className="loading-overlay">
      <div className="loading-container">
        <div className="loading-ball ball-1"></div>
        <div className="loading-ball ball-2"></div>
        <div className="loading-ball ball-3"></div>
      </div>
    </div>
  )
}

export default Loading
