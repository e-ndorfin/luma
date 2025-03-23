import os
import cohere
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from typing import Tuple, Dict, Any
from tts import generate_audio
from prompts import full_prompt
from audio_mixer import mix_audio_with_soundtrack

load_dotenv()

class SSMLResponse(BaseModel):
    ssml_content: str

class MeditationAgent:
    def __init__(self):
        self.co = cohere.ClientV2(api_key=os.getenv('COHERE_API_KEY'))
        
    def _build_prompt(self, user_input: str) -> str:
        return f"""
        {full_prompt}
        
        USER CONTEXT:
        {user_input}
        
        OUTPUT FORMAT:
        - Valid SSML wrapped in <speak> tags
        - DO NOT ADD <voice> TAGS IN ANY CIRCUMSTANCE
        - No markdown or additional formatting
        - Only include the SSML script
        """
        
    def _process_response(self, generated_text: str) -> Tuple[str, str]:
        # Extract SSML content
        if "<speak>" in generated_text:
            ssml_content = generated_text.split("<speak>")[1].strip()
            if "</speak>" in ssml_content:
                ssml_content = ssml_content.split("</speak>")[0].strip()
            ssml_content = f"<speak>{ssml_content}</speak>"
        else:
            # If no tags, wrap the entire content
            ssml_content = f"<speak>{generated_text}</speak>"
            
        # Validate with Pydantic
        try:
            SSMLResponse(ssml_content=ssml_content)
            return ssml_content, ""
        except ValidationError as e:
            return "", f"Invalid SSML format: {str(e)}"


    def generate_meditation(self, user_input: str) -> Tuple[Dict[str, Any], int]:
        if not user_input:
            return {"error": "Prompt is required"}, 400
            
        try:
            prompt = self._build_prompt(user_input)
            
            # Get Cohere response

            response = self.co.chat(
                model="command-a-03-2025",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],  # Add relevant chat history if needed
                temperature=0.2,
            )
            print(response.message.content[0].text)
            
            generated_text = response.message.content[0].text
            ssml_content, error = self._process_response(generated_text)
            
            if error:
                return {"error": error}, 400
                
            # Generate audio from SSML
            generate_audio(ssml_content)
            
            # Mix with background music
            mix_audio_with_soundtrack()
            
            return {
                "ssml": ssml_content,
                "response": generated_text,
                "audio_file": "final_output.mp3"
            }, 200
            
        except Exception as e:
            print (str(e))
            return {"error": str(e)}, 500
