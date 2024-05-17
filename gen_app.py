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
from gtts import gTTS
import base64

# Load environment variables
load_dotenv()

# Configure the Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Function to generate response from the Generative AI model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text 

# Function to convert text to speech and save to audio file
def text_to_speech(text, filename='audio.mp3'):
    tts = gTTS(text)
    audio_file_path = filename
    tts.save(audio_file_path)
    return audio_file_path

# Function to generate download link for binary file
def get_binary_file_downloader_html(bin_file, file_label='File', button_label='Download', file_extension='mp3'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    base64_encoded_file = base64.b64encode(data).decode()
    href = f'<a href="data:audio/{file_extension};base64,{base64_encoded_file}" download="{bin_file}">{button_label}</a>'
    return href

# Set Streamlit page configuration
st.set_page_config(page_title='PDF Q&A')

# Display logo and header
logo = "logo.jpeg"
st.image(logo, width=200)
st.header("Phoenix Lab's AI ASSISTANT: NADIA AI® ")

# Text input for user query
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("GO")

if submit_button:
    response = get_gemini_response(input_text)
    st.subheader("THE RESPONSE IS")
    st.write(response)
    
    # Convert response text to speech and save to audio file
    audio_file_path = text_to_speech(response)
    
    # Provide a download link for the audio file
    st.markdown(get_binary_file_downloader_html(audio_file_path, 'Download Audio', 'Audio File'), unsafe_allow_html=True)
