# import streamlit as st
# import os
# from google import generativeai as genai
# import sounddevice as sd
# import soundfile as sf
# import speech_recognition as sr
# from dotenv import load_dotenv
# import pyaudio

# # Load environment variables
# load_dotenv()

# # Configure the Generative AI model
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-pro")

# # Function to generate response from the Generative AI model
# def get_gemini_response(question):
#     response = model.generate_content(question)
#     return response.text 

# # Function to recognize speech from audio
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     duration = 3  # Duration for recording in seconds
#     samplerate = 44100  # Sample rate
#     channels = 1  # Number of audio channels

#     audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='float32')
#     sd.wait()

#     temp_audio_path = 'temp_audio.wav'
#     with sf.SoundFile(temp_audio_path, mode='w', samplerate=samplerate, channels=channels) as file:
#         file.write(audio_data)

#     with sr.AudioFile(temp_audio_path) as source:
#         audio_data = recognizer.record(source)
    
#     try:
#         text = recognizer.recognize_google(audio_data)
#         return text
#     except sr.UnknownValueError:
#         return "Sorry, I could not understand the audio."
#     except sr.RequestError as e:
#         return f"Could not request results from Google Speech Recognition service; {e}"

# # Set Streamlit page configuration
# st.set_page_config(page_title="Phoenix Lab's AI ASSISTANT: NADIA AI®", page_icon="🧠", layout='wide')

# # Display header and logo
# st.title("Phoenix Lab's AI ASSISTANT: NADIA AI®")
# logo_path = 'logo.jpeg'
# if os.path.exists(logo_path):
#     st.image(logo_path, width=200)
# else:
#     st.warning("Logo image not found!")

# # User input options
# input_option = st.radio("Choose input method:", ('Text', 'Voice'))

# if input_option == 'Text':
#     input_text = st.text_input("Input: ")
#     submit_button = st.button("GO")
#     if submit_button:
#         response = get_gemini_response(input_text)
#         st.subheader("THE RESPONSE IS")
#         st.write(response)
        
# elif input_option == 'Voice':
#     st.info("Please click the button below and speak clearly into your microphone.")
#     record_button = st.button("Start Recording")
#     if record_button:
#         st.info("Recording... Speak now.")
#         text_query = recognize_speech()
#         st.write("Recognized Text: ", text_query)
#         response = get_gemini_response(text_query)
#         st.subheader("THE RESPONSE IS")
#         st.write(response)

# # Health Check Endpoint
# @st.cache
# def health_check():
#     return "OK"

# if st.button("Check Health"):
#     status = health_check()
#     st.write("Health Check:", status)
import streamlit as st
import os
from google import generativeai as genai
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Function to generate response from the Generative AI model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text 

# Function to recognize speech from audio
def recognize_speech():
    recognizer = sr.Recognizer()
    duration = 3  # Duration for recording in seconds
    samplerate = 44100  # Sample rate
    channels = 1  # Number of audio channels

    # Record audio using sounddevice
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='float32')
    sd.wait()

    temp_audio_path = 'temp_audio.wav'
    # Write recorded audio to a temporary file
    with sf.SoundFile(temp_audio_path, mode='w', samplerate=samplerate, channels=channels) as file:
        file.write(audio_data)

    # Recognize speech using speech_recognition
    with sr.AudioFile(temp_audio_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

# Set Streamlit page configuration
st.set_page_config(page_title="Phoenix Lab's AI ASSISTANT: NADIA AI®", page_icon="🧠", layout='wide')

# Display header and logo
st.title("Phoenix Lab's AI ASSISTANT: NADIA AI®")
logo_path = 'logo.jpeg'
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

# Health Check Endpoint
@st.cache
def health_check():
    return "OK"

if st.button("Check Health"):
    status = health_check()
    st.write("Health Check:", status)

