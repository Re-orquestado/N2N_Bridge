```markdown
# N2N Bridge Middleware

**N2N Bridge** is an intelligent middleware that converts video game telemetry into **MusicXML 3.1** scores using AI (Groq). The system acts as a bridge between game state and musical notation, generating **structural scaffolds** that serve as a starting point for human composers.

---

## 🎯 Features

- **Semantic translation**: Converts game variables (tension, environment, combat) into musical parameters (harmony, rhythm, dynamics, instrumentation).
- **MusicXML 3.1**: Generates valid, well-formed code compatible with MuseScore 4 and other notation software.
- **REST API**: Exposes endpoints to receive telemetry and return scores.
- **Structural scaffolding**: Creates functional mockups with 4 real voices, logical harmonic progressions, and respect for instrumental ranges.
- **Deterministic and educational**: Designed for the human composer to complete and refine the work.

---

## 🚀 Technologies

- **Python 3.10+**
- **FastAPI** – Web framework for the REST API
- **Groq SDK** – Connection with the Llama 3.3 70B model
- **Pydantic** – Telemetry data validation
- **Uvicorn** – ASGI server

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/N2N_Bridge_Final.git
cd N2N_Bridge_Final
```

2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create a .env file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

---

🖥️ Usage

Run the server

```bash
python main.py
```

The server will be available at http://localhost:8000.

Available endpoints

POST /generate

Receives telemetry and generates a MusicXML file.

Example request:

```json
{
  "player_health": 45.0,
  "enemy_proximity": 78.0,
  "environment": "dark_cave",
  "narrative_tension_level": 8,
  "is_in_combat": true,
  "musical_request": {
    "emotions": ["tenso", "oscuro", "urgente"]
  }
}
```

Response:

```json
{
  "status": "success",
  "filename": "output_1702345678.musicxml",
  "musicxml": "<?xml version=\"1.0\" ... </score-partwise>"
}
```

GET /health

Verifies that the service is running.

---

📁 Project Structure

```
N2N_Bridge_Final/
├── main.py              # FastAPI server
├── bridge.py            # Core logic (Groq connection)
├── models.py            # Pydantic models for telemetry
├── config.py            # Configuration and environment variables
├── requirements.txt     # Dependencies
├── telemetry_example.json # Example telemetry for testing
└── README.md            # This file
```

---

🎼 How it works internally

1. The user sends telemetry to the /generate endpoint.
2. The system builds a prompt with specific instructions for the LLM (role, constraints, theoretical rules, parameter mapping).
3. Groq processes the prompt and generates clean MusicXML 3.1 code, with no extra text.
4. The file is saved with a unique timestamp on the server.
5. The score can be opened in MuseScore for review and editing.

---

🧪 Quick tests

With curl

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d @telemetry_example.json
```

With Python (requests)

```python
import requests
import json

telemetry = {
    "player_health": 45.0,
    "enemy_proximity": 78.0,
    "environment": "dark_cave",
    "narrative_tension_level": 8,
    "is_in_combat": True,
    "musical_request": {
        "emotions": ["tenso", "oscuro"]
    }
}

response = requests.post("http://localhost:8000/generate", json=telemetry)
print(response.json())
```

---

🔧 Customization

Modify the system prompt

Edit bridge.py in the build_system_prompt() method. You can adjust:

· Harmony and counterpoint rules.
· Instrumental ranges.
· Emotion-to-harmonic-progression mapping.
· Rhythmic density parameters.

Change the Groq model

In bridge.py, modify:

```python
self.model = "llama-3.3-70b-versatile"  # Change to another available model
```

Adjust generation parameters

In generate_musicxml(), modify:

```python
temperature=0.7,      # Creativity (0-1)
max_tokens=4096,      # Length limit
top_p=0.95            # Nucleus sampling
```

---

📚 Main dependencies

Package Version Purpose
fastapi 0.115.6 Web framework
uvicorn 0.34.0 ASGI server
groq 0.10.0 Groq API SDK
python-dotenv 1.0.1 Environment variable loading
pydantic 2.9.2 Data validation

---

🤝 Contributing

Contributions are welcome. Please open an issue or pull request to suggest improvements.

---

📄 License

MIT License – see the LICENSE file for details.

---

👤 Author

Sergio Andrés Gutiérrez León

· GitHub: @sergioandresgutierrezleon-lab

---

🙏 Acknowledgements

· Groq for providing the Llama 3.3 70B model.
· MuseScore for their excellent music notation software.
· The open-source community for the tools that make this project possible.

---

Note: This system is designed to generate structural scaffolds, not finished works. The intention is to accelerate the composer's workflow, not to replace their artistic judgment.

```
