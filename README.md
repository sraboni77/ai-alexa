
Alexa Voice Assistant using Python + Ollama (TinyLLaMA)

 A smart offline voice assistant built with Python that listens to your voice, answers questions using TinyLLaMA via Ollama, tells weather info, plays YouTube videos, and tells jokes — all in a beautiful GUI!




 Features

Voice command input

 YouTube video playback via pywhatkit

 Weather info via OpenWeatherMap API

 Jokes via pyjokes

Wikipedia info summary

Offline QA via predefined answers

AI answers using Ollama + TinyLLaMA (offline)

 GUI interface using CustomTkinter





 Setup Instructions

 1. Clone or Download

git clone https://github.com/yourname/alexa-voice-assistant.git
cd alexa-voice-assistant

 2. Install Python Libraries

pip install -r requirements.txt

 3. Required Libraries

 requirements.txt 

pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes requests customtkinter

 4. Install & Run Ollama with TinyLLaMA

1. Install Ollama


2. Pull TinyLLaMA model:



ollama pull tinyllama

3. Test the model:



ollama run tinyllama


---

 Weather API Setup

1. Visit: https://openweathermap.org/api


2. Create an account and get your API Key


3. Replace the following line in your code:



weather_api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

With:

weather_api_key = 'your_real_api_key_here'




How to Run

Terminal Mode (no GUI):

python main.py

 GUI Mode:

python app.py




 Sample Voice Commands

Try saying:

Alexa what time is it?

Alexa play shape of you

Alexa tell me about Python

Alexa what is the capital of Bangladesh

Alexa joke

Alexa weather in Dhaka

Alexa chat with me





 File Structure

 alexa-voice-assistant
├── app.py               # GUI frontend
├── main.py              # Core voice logic
├── README.md            # This file
└── requirements.txt     # All dependencies
