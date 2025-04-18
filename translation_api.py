from flask import Flask, request, jsonify
import os
import requests
import json
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
LECTO_API_KEY = os.getenv('LECTO_API_KEY')
LECTO_API_URL = 'https://api.lecto.ai/v1/translate/text'

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Get data from frontend
        data = request.json
        texts = data.get('texts', [])
        target_langs = data.get('target_langs', [])
        source_lang = data.get('source_lang', 'en')  # Default to English
        
        if not texts or not target_langs:
            return jsonify({
                'success': False,
                'error': 'Missing required fields: texts or target_langs'
            }), 400

        # Prepare payload for Lecto API
        payload = {
            "texts": texts,
            "to": target_langs,
            "from": source_lang
        }

        # Make request to Lecto
        response = requests.post(
            LECTO_API_URL,
            headers={
                'X-API-Key': LECTO_API_KEY,
                'Content-Type': 'application/json'
            },
            data=json.dumps(payload)
        )

        # Check response
        if response.status_code == 200:
            translations = response.json()
            return jsonify({
                'success': True,
                'translations': translations['translations'],
                'detected_language': translations.get('detected_language', source_lang)
            })
        else:
            return jsonify({
                'success': False,
                'error': f"Lecto API Error: {response.status_code}",
                'details': response.json()
            }), response.status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)