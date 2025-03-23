import React, { useState, useRef, useEffect } from 'react';
import './MeditationOutput.css';
import kanyeImg from '../assets/imgs/kanye.png';
import runawayAudio from '../../../backend/final_output.mp3';

function MeditationOutput() {
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef(new Audio(runawayAudio));
  
  // Set up audio event listeners
  useEffect(() => {
    // When audio ends, update the isPlaying state
    const handleAudioEnd = () => {
      setIsPlaying(false);
      console.log('Audio playback ended');
    };
    
    audioRef.current.addEventListener('ended', handleAudioEnd);
    
    // Cleanup event listeners on component unmount
    return () => {
      audioRef.current.removeEventListener('ended', handleAudioEnd);
      audioRef.current.pause();
    };
  }, []);
  
  // Control audio playback based on isPlaying state
  useEffect(() => {
    if (isPlaying) {
      console.log('Starting audio playback');
      audioRef.current.play()
        .catch(error => {
          console.error('Error playing audio:', error);
          setIsPlaying(false);
        });
    } else {
      console.log('Pausing audio playback');
      audioRef.current.pause();
    }
  }, [isPlaying]);
  
  const togglePlayback = () => {
    setIsPlaying(!isPlaying);
  };
  
  const rewindAudio = () => {
    // Reset audio to beginning
    audioRef.current.currentTime = 0;
    console.log('Audio rewound to beginning');
  };

  return (
    <div className="meditation-output">
      
      <div className="vinyl-container">
        <img 
          src={kanyeImg} 
          alt="Meditation Cover" 
          className={`vinyl-image ${isPlaying ? 'rotating' : ''}`} 
        />
      </div>
      
      <div className="controls-container">
        {/* Center space filler */}
        <div className="control-spacer"></div>
        
        {/* Main play/pause button */}
        <button 
          className="playback-button" 
          onClick={togglePlayback}
          aria-label={isPlaying ? "Pause" : "Play"}
        >
          {isPlaying ? (
            <svg viewBox="0 0 24 24" width="32" height="32">
              <rect x="6" y="4" width="4" height="16" fill="white" />
              <rect x="14" y="4" width="4" height="16" fill="white" />
            </svg>
          ) : (
            <svg viewBox="0 0 24 24" width="32" height="32">
              <polygon points="5,3 19,12 5,21" fill="white" />
            </svg>
          )}
        </button>
        
        {/* Rewind button */}
        <button 
          className="rewind-button" 
          onClick={rewindAudio}
          aria-label="Rewind to beginning"
        >
          <svg viewBox="0 0 24 24" width="24" height="24">
            <path d="M12,12 L20,6 L20,18 L12,12 M4,12 L12,6 L12,18 L4,12" fill="white" />
          </svg>
        </button>
      </div>
    </div>
  );
}

export default MeditationOutput;
