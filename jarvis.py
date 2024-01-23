import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import datetime

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12: 
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeComand():
    #it takes microphone input from the user and returns string outpult

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try: 
            print('Recognizing...')
            query = r.recognize_google(audio, Language='en-rs')
            print(f"User said: {query}\n")


        except Exception as e: 
            # print(e)

            print("Say that again please...")
            return "None"
        return query    
 
if __name__ == "__main__":
    wishMe()
    takeComand()
