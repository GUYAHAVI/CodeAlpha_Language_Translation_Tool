# 🌍 HelCrafters Language Translator

A simple yet powerful language translation web app that allows users to translate text between multiple languages using the Lecto AI Translation API.

Built with:
- 🌐 **HTML**, **CSS**, **JavaScript**, **Bootstrap** (Frontend)
- 🐍 **Python (Flask)** (Backend)
- 🌎 **Lecto AI** (Translation API)

---

## 🚀 Features

- ✅ Translate text between languages  
- ✅ Language selector (From / To)  
- ✅ Dynamic response display  
- ✅ CORS-enabled Flask backend  
- ✅ Error handling and fallback messages  
- ✅ Sleek, branded HelCrafters UI  

---

## 📸 Preview

![HelCrafters Translator Screenshot](screenshot.png)  
<sup>_Update this screenshot with an actual preview of your app._</sup>

---

## 🧱 Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Frontend     | HTML, CSS, Bootstrap, JavaScript |
| Backend      | Python, Flask                  |
| API          | [Lecto.ai Translation API](https://www.lecto.ai/) |
| Deployment   | Flask Dev Server (Localhost)  |

---

## 🛠️ Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/helcrafters-translator.git
cd helcrafters-translator
2. Set up your Python environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Create a .env file
In your project root, create a .env file and add your Lecto API key:

env
Copy
Edit
LECTO_API_KEY=your_lecto_api_key_here
4. Start the Flask backend
bash
Copy
Edit
python app.py
Flask will start on: http://127.0.0.1:5001

5. Open the frontend
Open index.html in your browser or serve it using Live Server / any static server.

📡 API Info
This app uses the Lecto.ai /translate/text endpoint with POST requests.

Required fields in the payload:

json
Copy
Edit
{
  "texts": ["Hello World"],
  "from": "en",
  "to": ["fr", "sw"]
}
🔐 Environment Variables

Variable	Description
LECTO_API_KEY	Your Lecto API Key
📁 Project Structure
bash
Copy
Edit
helcrafters-translator/
├── app.py               # Flask backend
├── .env                 # API key (not included in repo)
├── index.html           # Frontend UI
├── static/              # CSS/JS/Images
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
📄 License
This project is open for educational or personal use. For commercial deployment, ensure proper API licensing with Lecto.ai.

✨ Author
Built by Havi Elvis — HelCrafters Technologies

