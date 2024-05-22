# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st 
# import os 
# import google.generativeai as genai 

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model=genai.GenerativeModel("gemini-pro")
# def get_gemini_response(question):
#     response=model.generate_content(question)
#     return response.text 

# st.set_page_config(page_title='PDF Q&A')
# logo = "logo.jpeg"
# st.image(logo, width=200)
# st.header("Phoenix Lab's AI ASSISTANT: NADIA AI® ")
# input=st.text_input("Input: ",key="input")
# submit=st.button("GO")

# if submit:
#     response=get_gemini_response(input)
#     st.subheader("THE RESPONSE IS")
#     st.write(response)
from dotenv import load_dotenv
import streamlit as st 
import os 
import google.generativeai as genai 
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

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

    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()

    with sf.SoundFile('temp_audio.wav', mode='w', samplerate=samplerate, channels=channels) as file:
        file.write(audio_data)

    with sr.AudioFile('temp_audio.wav') as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

# Set Streamlit page configuration
st.set_page_config(page_title='PDF Q&A')
logo = "logo.jpeg"
st.image(logo, width=200)
st.header("Phoenix Lab's AI ASSISTANT: NADIA AI® ")

# User input options
input_option = st.radio("Choose input method:", ('Text', 'Voice'))

if input_option == 'Text':
    input_text = st.text_input("Input: ", key="input")
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
