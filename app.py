# app.py
import  streamlit as st
from stt import transcribe
from intent import classify_intent
from tools import *

st.title("🎤 Voice AI Agent")

# Input options
option = st.radio("Choose input method:", ["Upload Audio"])

audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

if audio_file:
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    st.success("Audio uploaded!")

    # Step 1: STT
    text = transcribe("temp.wav")
    st.subheader("📝 Transcribed Text")
    st.write(text)

    # Step 2: Intent
    intent_data = classify_intent(text)
    st.subheader("🧠 Detected Intent")
    st.write(intent_data)

    # Step 3: Execution
    intent = intent_data["intent"]
    details = intent_data.get("details", "")

    if intent == "create_file":
        result = create_file("new_file.txt")

    elif intent == "write_code":
        result = write_code("code.py", details)

    elif intent == "summarize":
        result = summarize_text(details)

    else:
        result = chat_response(text)

    st.subheader("⚙️ Action Taken")
    st.write(result)

    st.subheader("✅ Final Output")
    st.write(result)