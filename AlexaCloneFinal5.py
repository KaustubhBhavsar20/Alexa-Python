#Kaustubh Bhavsar
print("Python Mini Project- Cloning Alexa By Kaustubh Bhavsar")
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pygoogle
import webbrowser
listener=sr.Recognizer()
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command
    
def run_alexa():


    command=take_command()
    print(command)
    
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'time'  in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' +time)
       
    elif 'who is ' in command:
         person=command.replace('who is', '')
         info=wikipedia.summary(person,2)
         print(info)
         talk(info)
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())\
                                  
    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")                              
   
    elif 'open youtube' in command:
       
        talk("Here you go to youtube\n")
        webbrowser.open("youtube.com")
    
    elif 'open instagram' in command:
       
        talk("Here you go to instagram\n")
        webbrowser.open("insatgram.com")
    
    else:
        talk('Sorry I didnt got you...please repeat the command')
talk("Hi, I am your Alexa, What can I do for you?")
while True:
    run_alexa()
