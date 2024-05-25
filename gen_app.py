import os
import logging
from google import generativeai as genai
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from dotenv import load_dotenv
import streamlit as st

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()
logging.info("Loaded environment variables.")

# Configure the Generative AI model
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    logging.info("Configured Generative AI model.")
except Exception as e:
    logging.error(f"Error configuring Generative AI model: {e}")

# Function to generate response from the Generative AI model
def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text 
    except Exception as e:
        st.error(f"Error generating response: {e}")
        logging.error(f"Error generating response: {e}")
        return "Error generating response"

# Function to recognize speech from audio
def recognize_speech():
    recognizer = sr.Recognizer()
    duration = 3  # Duration for recording in seconds
    samplerate = 44100  # Sample rate
    channels = 1  # Number of audio channels

    try:
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='float32')
        sd.wait()

        temp_audio_path = 'temp_audio.wav'  # Relative path for temp audio file
        with sf.SoundFile(temp_audio_path, mode='w', samplerate=samplerate, channels=channels) as file:
            file.write(audio_data)

        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        st.error(f"Error recording audio: {e}")
        logging.error(f"Error recording audio: {e}")
        return "Error recording audio"

# Set Streamlit page configuration
st.set_page_config(page_title="Phoenix Lab's AI ASSISTANT: NADIA AI®", page_icon="🧠")

# Display header and logo
st.title("Phoenix Lab's AI ASSISTANT: NADIA AI®")
logo_path = 'logo.jpeg'  # Relative path for logo image
if os.path.exists(logo_path):
    st.image(logo_path, width=200)
else:
    st.warning("Logo image not found!")

# User input options
input_option = st.radio("Choose input method:", ('Text', 'Voice'))

if input_option == 'Text':
    input_text = st.text_input("Input: ")
    submit_button = st.button("GO")
    if submit_button:
        response = get_gemini_response(input_text)
        st.subheader("THE RESPONSE IS")
        st.write(response)
        
elif input_option == 'Voice':
    st.info("Please click the button below and speak clearly into your microphone.")
    record_button = st.button("Start Recording")
    if record_button:
        st.info("Recording... Speak now.")
        text_query = recognize_speech()
        st.write("Recognized Text: ", text_query)
        response = get_gemini_response(text_query)
        st.subheader("THE RESPONSE IS")
        st.write(response)
