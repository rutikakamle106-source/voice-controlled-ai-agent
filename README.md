# Voice-Controlled AI Agent

## 📌 Objective
This project builds a local AI agent that takes voice input, detects user intent, executes tasks, and displays results in a UI.

## 🚀 Features
- Audio input via microphone and file upload
- Speech-to-text conversion
- Intent classification
- Task execution
- Clean UI display

## 🛠️ Technologies Used
- Python
- SpeechRecognition
- PyAudio
- OpenAI / Local LLM (if used)
- Tkinter / Streamlit (UI)

## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py

Voice Ai Agent Git Hub Project
🎤 Voice-Controlled Local AI Agent
📌 Overview

This project is a Voice-Controlled Local AI Agent that:

Accepts audio input (file upload)
Converts speech to text using Whisper
Classifies user intent using a local LLM (Ollama)
Executes actions (file creation, code writing, summarization, chat)
Displays results in a Streamlit UI
🧱 Project Structure
voice_ai_agent/
│
├── app.py
├── stt.py
├── intent.py
├── tools.py
├── requirements.txt
├── README.md
├── output/
⚙️ Installation
# Clone repo
git clone <your-repo-link>
cd voice_ai_agent


# Install dependencies
pip install -r requirements.txt
▶️ Run the App
streamlit run app.py
🧠 Requirements
Python 3.9+
Ollama installed and running

Start Ollama:

ollama run mistral
📦 requirements.txt
streamlit
transformers
torch
librosa
soundfile
requests