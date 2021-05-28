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

## email feature
def sendmail(to, content):
    msg = MIMEMultipart()
    msg.attach(MIMEText("Hello, my name is December", 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.ehlo()
    server.starttls()
    server.login("userr@gmail.com","Password")
    server.sendmail("user@gmail.com", to, content)
    server.quit()

##In this we are giving the power to take screenshots or screencapture when we told it to do it
def screenshot():
    screencapture = pyautogui.screenshot()
    screencapture.save("D:\Documentos\Proyectos\AI - Inteligencia Artificial\Proyectos\sc.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    print(usage)
   # cpu_temp = psutil.sensors_temperatures(fahrenheit=False)()
   # speak("CPU temp is at "+ cpu_temp)
   # print(cpu_temp)
   # fans = psutil.sensors_fans()
   # speak("Fans are at "+ fans)
   # print(fans)
   # speak("CPU temp is at " + str(psutil.sensors_temperatures()))
   # speak("Fans are at " + psutil.sensors_fans)
    
    battery = psutil.sensors_battery()
    speak("Battery is at ") 
    speak(battery.percent)
    print(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query: #ver como hacer un comando global
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            ## Here December will tell us what she is looking at
            ## and the results, aun necesita mejoras..      
        elif "send email" in query:
            try: ## Will ask us what the mail should contain
                speak("Sir, what should I say?")
                content = takeCommand()
                to = "user@gmail.com"
                sendmail(to, content)
                #speak(content)
                speak("Sir the email was successfully sent to the recipient.")
            except Exception as e:
                    speak(e)
                    speak("Sir im unable to send the email") 
        elif "search in chrome" in query:
            speak("Sir, what should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query: ##log off, the same as type win logon + L
            os.system("shutdown -l")
        elif "shutdown" in query: ##shutdown in 1 min, can be less if we choose zero = 0, than 1
            os.system("shutdown /s /t 1")
        elif "restart" in query: ##restart the computer
            os.system("shutdown /r /t 1")
        elif "play music" in query: ##Play music inside a folder
            songs_dir = "D:\Música"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0])) ## This one is under development because can be used for path traversal
        elif "Remember that" in query: #Recordar cosas
            speak("What should I remember?")
            data = takeCommand()
            speak("Sir, you told me to remember" + data)
            Remember = open("data.txt", "w")
            Remember.write(data)
            Remember.close()
        elif "What we have for on point" in query: #The AI assistant will tell us what he/she saved
            Remember = open("data.txt", "r")
            speak("Sir, you told me to remember that"+Remember.read())
        elif "screenshot" in query: #The AI wil tell us that he/she took the screenshot
            screenshot()
            speak("Sir, I took the screenshot")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()


