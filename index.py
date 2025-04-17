import os
import requests
import json

# Load API key from environMyment variable
api_key = os.getenv('API_KEY')  # Make sure to set this in your environment

headers = {
    'X-API-Key': api_key,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

# Get user input and split into a list
texts_input = input("Enter the texts to translate (comma separated): ")
texts = [text.strip() for text in texts_input.split(",") if text.strip()]

# Define target languages (Portuguese-Brazilian and German)
target_languages = ["pt-BR", "de"]

# Prepare the request payload
payload = {
    "texts": texts,
    "to": target_languages,
    "from": "en"  # Source language (English)
}

try:
    # Make the API request
    response = requests.post(
        'https://api.lecto.ai/v1/translate/text',
        headers=headers,
        data=json.dumps(payload)  # Convert dict to JSON string
    )
    # Check if the request was successful
    if response.status_code == 200:
        translations = response.json()
        print("\nTranslation Results:")
        for i, text in enumerate(texts):
            print(f"\nOriginal ({payload['from']}): {text}")
            for lang in target_languages:
                translated_text = translations['translations'][i][lang]
                print(f"Translated ({lang}): {translated_text}")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())  # Print error details

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except KeyError:
    print("Unexpected response format from API.")
    print(response.json())  # Print error details
    
except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
except KeyError:
        print("Unexpected response format from API.")
        print(response.json())  # Print error details
        
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except KeyError:
    print("Unexpected response format from API.")