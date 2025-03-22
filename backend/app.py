from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
import cohere
from datetime import datetime

load_dotenv()  # Load environment variables
app = Flask(__name__)
CORS(app)  # Enable CORS for development

co = cohere.Client(os.getenv('COHERE_API_KEY'))  # Initialize Cohere client

# Example API endpoint
@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Flask backend!'})

@app.route('/api/generate', methods=['POST'])
def generate_text():
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
            
        # Get Cohere response
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=4096,
            temperature=0.9
        )
        
        generated_text = response.generations[0].text
        
        # Store in responses.txt
        with open('responses.txt', 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\nPrompt: {prompt}\nResponse: {generated_text}\n\n")
        
        return jsonify({"response": generated_text})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Production setup for React static files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join('frontend/dist', path)):
        return send_from_directory('frontend/dist', path)
    else:
        return send_from_directory('frontend/dist', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
