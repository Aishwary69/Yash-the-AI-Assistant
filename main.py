import speech_recognition as sr;
import webbrowser
import pyttsx3
import musicLibrary
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

recognizer = sr.Recognizer()
ttsx= pyttsx3.init()


def speak(text):
    engine=ttsx
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(command)
    return response.text


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link)
    else:
        output = aiprocess(c)
        speak(output) 



if __name__ == "__main__":
    speak("Intializing Yash")
    #Listing for the word Aishtri 
    # obtain audio from the microphone

    r=sr.Recognizer()


   
    
    try:
        with sr.Microphone() as source:
            print("say something")
            # to talk after the uper statment gets print tabhi it will listen and recognise 
            audio = r.listen(source, timeout=2,phrase_time_limit=1)
            print("recognizing ")
        command = r.recognize_google(audio)
        if (command.lower()=="hello yash"):
            speak("yes sir")

            # listen to the commands
            with sr.Microphone() as source:
                print("Yash Active....")
                audio = r.listen(source)
                command=r.recognize_google(audio)
                processCommand(command)
        print(command)
    except Exception as e:
        print("Error :".format(e))
