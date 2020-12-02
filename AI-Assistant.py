# Este es el asistente AIpy en proceso (iniciado pero falta el ML, AI, etc)
# Este asistente todavia no cuenta con el complemento de la IA o AI
# La mente arquitecta (yo) aun no cuenta con esos conocimientos
#engine.say("Hello world. My name is December.")
#engine.runAndWait()
#ajuste de veloc de hablado
# y cambio del genero de la voz a fem voices[0] señora
# [1] voz femenina mas juvenil
# [2] voz masculina tipo español de castilla

import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 130 #Veloc dentro de lo normal / Normal talk speed
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("This is December, a personal assistant")

def time(): #Now it tell us the current date
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)
#time() #This tells the machine to say it first

def date(): #Tell us the current date in numbers
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)
#date() #same as above but like time is upper, this one is the second one to be said

def wishme():
    speak("Welcome back Sir!")
    time()
    date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak ("Good morning!")
    elif hour >= 12 and hour < 18:
        speak ("Good afternoon!")
    elif hour >= 18 and hour <= 24:
        speak("Good evening!")
    else:
        speak("Good night!")
    speak("December at your service. How can i help you?")
#wishme()
# With this the assistant can hear us and write/shows in terminal
# what we were saying or trying to say... 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Sir...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Kindly say it again....")

        return "None"

    return query
takeCommand()


