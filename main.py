import pyttsx3
import speech_recognition as sc
import datetime
import wikipedia
import webbrowser
import smtplib

mails = [
    {
        "username": "fahad1",
        "email": "ff3008413@gmail.com"

    },
    {
        "username": "fahad2",
        "email": "ff084130@gmail.com"

    },
]

engine = pyttsx3.init()
engine.setProperty('voice', 'english_rp+f4')


def speak(speech):
    print(speech)
    engine.say(speech)
    engine.runAndWait()


password = ''

with open('./password.txt', 'r') as file:
    password = file.readline()


email = 'faizanfarooq00011@gmail.com'


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good Morning!")
    elif hour >= 12 and hour < 18:
        speak("good Afternoon!")
    else:
        speak("good evening!")
    speak("hello I am rachel sir how can I help you")


def takecommand():
    r = sc.Recognizer()
    with sc.Microphone() as source:
        print("index", source.device_index)
        print("I am listening")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source=source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that agin")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to, content)


if __name__ == "__main__":
    wishme()
    while True:
        command = takecommand().lower()
        if 'wikipedia' in command:
            speak('searching Wikipedia... ')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, 2)
            print(results)
            speak(results)
        elif 'close all' in command:
            break
        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
        elif 'open google' in command:
            webbrowser.open("google.com")
        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif 'sendemail' in command:
            speak("tell me receivers name")
            name = takecommand()
            for mail in mails:
                if mail['username'] == name:
                    to = mail['email']

                    speak("what do you want to send")
                    content = takecommand()
                    sendemail(to, content=content)
