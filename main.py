import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import requests
import subprocess


weather_api_key = '9fb129e93e9a8b2009238cd45dba8ad0'


listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    print("Alexa:", text)
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('🎙️ Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
    except Exception as e:
        print("Error:", e)
    return command


def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"The temperature in {city.title()} is {temp}°C with {desc}."
        else:
            return f"Sorry, I couldn't get weather info for {city}."
    except:
        return "Sorry, weather service failed."


qa_data = {
    "what is your name": "My name is Alexa.",
    "who are you": "I am your offline AI assistant.",
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who is the prime minister of bangladesh": "The Prime Minister of Bangladesh is Sheikh Hasina.",
    "what is the capital of bangladesh": "The capital of Bangladesh is Dhaka.",
    "how are you": "I am fine, thank you!",
    "exit chat": "exit"
}

def ask_offline_bot(user_input):
    user_input = user_input.lower()
    for question in qa_data:
        if question in user_input:
            return qa_data[question]
    return None


def ask_ollama(question):
    try:

        result = subprocess.run(
            ["ollama", "run", "tinyllama"],
            input=question.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        output = result.stdout.decode('utf-8').strip()
        if output:
            return output
        else:
            return "Sorry, I did not get a response from AI model."
    except Exception as e:
        return f"Ollama error: {e}"


def run_alexa():
    command = take_command()
    if command:
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'play' in command:
            song = command.replace('play', '').strip()
            talk('Playing ' + song)
            pywhatkit.playonyt(song)

        elif 'tell me about' in command:
            topic = command.replace('tell me about', '').strip()
            try:
                info = wikipedia.summary(topic, sentences=2)
                talk(info)
            except:
                talk("Sorry, I couldn't find anything about " + topic)

        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'date' in command:
            talk('Sorry vaiya, I am in another relation.')

        elif 'weather' in command or 'আজকের weather' in command or 'আবহাওয়া' in command:
            city = ''
            words = command.split()

            if 'in' in words:
                idx = words.index('in')
                city = ' '.join(words[idx + 1:])
            elif 'for' in words:
                idx = words.index('for')
                city = ' '.join(words[idx + 1:])
            else:
                temp = command.replace('today', '').replace('weather', '').replace('আজকের', '').replace('আজকে', '').replace('আবহাওয়া', '').strip()
                city = temp if temp else 'dhaka'

            report = get_weather(city)
            talk(report)

        elif 'chat with me' in command:
            start_chat_mode()

        elif 'what is' in command or 'who is' in command:
            response = ask_offline_bot(command)
            if response:
                talk(response)
            else:

                ai_response = ask_ollama(command)
                talk(ai_response)

        else:

            ai_response = ask_ollama(command)
            if ai_response and "error" not in ai_response.lower():
                talk(ai_response)
            else:
                talk("I didn't understand. Let me search it for you.")
                pywhatkit.search(command)
    else:
        print("Alexa: Please say that again.")


def start_chat_mode():
    talk("Sure! Chat mode is on. Ask me anything. Say 'exit chat' to stop.")
    while True:
        question = take_command()
        if question:
            if "exit chat" in question:
                talk("Okay, exiting chat mode.")
                break
            response = ask_offline_bot(question)
            if not response:
                response = ask_ollama(question)
            talk(response)
        else:
            talk("I didn't catch that. Please repeat.")

# ===  Continuous Loop ===
while True:
    run_alexa()
