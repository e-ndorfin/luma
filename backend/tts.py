import os
from google.cloud import texttospeech

"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""

def generate_audio(input_text: str) -> None:
    '''Takes in string / SSML code and saves audio in same folder as .mp3'''
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'


    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(ssml=input_text)

    # Build the voice request, select the language code ("en-US") 

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )   

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=0.7,
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


if __name__ == "__main__": 
    ssml = """
    <speak>
        <p>
        Welcome. <break time="5000ms"/>
        Find a comfortable position, wherever you are. <break time="3000ms"/>
        Let this be a moment to pause and breathe. <break time="5000ms"/>
        </p>

        <p>
        Close your eyes gently, if it feels right. <break time="3000ms"/>
        Soften your jaw, your forehead, and let your shoulders relax. <break time="5000ms"/>
        Take a slow, deep breath in… <break time="3000ms"/>
        And exhale, letting go of any tension. <break time="5000ms"/>
        </p>

        <p>
        It’s okay to feel disappointed right now. <break time="3000ms"/>
        Maybe a grade didn’t go your way, and that’s heavy. <break time="5000ms"/>
        But remember, one moment doesn’t define you. <break time="3000ms"/>
        You are more than this. <break time="5000ms"/>
        </p>

        <p>
        Feel your breath, steady and calm. <break time="3000ms"/>
        Inhale… and exhale. <break time="3000ms"/>
        Let each breath remind you: you are resilient. <break time="5000ms"/>
        You are capable. <break time="3000ms"/>
        You will take one step at a time. <break time="5000ms"/>
        </p>

        <p>
        Notice any tightness in your chest or stomach. <break time="3000ms"/>
        It’s okay to feel it. <break time="2000ms"/>
        Breathe into that space… <break time="3000ms"/>
        And as you exhale, imagine releasing a little of that weight. <break time="5000ms"/>
        </p>

        <p>
        You’re allowed to rest. <break time="3000ms"/>
        You’re allowed to feel what you feel. <break time="3000ms"/>
        And you’re allowed to let it go, just for now. <break time="5000ms"/>
        </p>

        <p>
        Repeat these words softly, if they resonate: <break time="3000ms"/>
        <prosody rate="slow">“I am enough.”</prosody> <break time="3000ms"/>
        <prosody rate="slow">“I am learning.”</prosody> <break time="3000ms"/>
        <prosody rate="slow">“I will try again.”</prosody> <break time="5000ms"/>
        </p>

        <p>
        As we close, bring your awareness back to the room. <break time="3000ms"/>
        Wiggle your fingers and toes, gently. <break time="3000ms"/>
        When you’re ready, open your eyes. <break time="5000ms"/>
        </p>

        <p>
        Carry this calm with you. <break time="3000ms"/>
        One breath at a time. <break time="5000ms"/>
        </p>
    </speak>
    """
    generate_audio(ssml)