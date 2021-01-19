import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
#from googlesearch.googlesearch import GoogleSearch

listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'friday' in command:
                command=command.replace('friday','')
                print(command)
    except:
        pass
    return command

def run_friday():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is: '+time)

    elif 'who the heck is' in command:
        person=command.replace('who the heck is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'hello' in command:
        talk('Yes boss,how can i Help You?')
    else:
        talk('Please say the command again,sir.')

while True:
    run_friday()
