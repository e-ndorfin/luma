from pydub import AudioSegment
from pydub.utils import mediainfo

def mix_audio_with_soundtrack(
    speech_path: str = "output.mp3",
    soundtrack_path: str = "soundtrack.mp3",
    output_path: str = "final_output.mp3",
    music_volume_dB: float = -20.0
) -> None:
    """Mix speech audio with background music at reduced volume"""
    
    # Load audio files
    speech = AudioSegment.from_file(speech_path, format="mp3")
    soundtrack = AudioSegment.from_file(soundtrack_path, format="mp3")
    
    # Calculate durations
    speech_duration = len(speech)
    
    # Reduce music volume
    soundtrack = soundtrack + music_volume_dB
    
    # Cut soundtrack to match speech duration
    trimmed_soundtrack = soundtrack[:speech_duration]
    
    # Mix the audio
    mixed = speech.overlay(trimmed_soundtrack)
    
    # Export final output
    mixed.export(output_path, format="mp3", bitrate="192k", tags=mediainfo(speech_path).get('TAG', {}))

if __name__ == "__main__":
    mix_audio_with_soundtrack()