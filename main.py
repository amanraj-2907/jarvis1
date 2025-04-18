
from cmath import phase
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

recognizer  = sr.Recognizer()
engine= pyttsx3.init()
newsapi="87439301460f433caff335d005f3ed3e"

def speak(text):
    engine.say( text)
    engine.runAndWait()

def processComand(c):
    if(c.lower()=="open google"):
        webbrowser.open("http://google.com")
    elif(c.lower()=="open youtube"):
        webbrowser.open("http://youtube.com")
    elif(c.lower()=="open facebook"):
        webbrowser.open("http://facebook.com")
    elif(c.lower()=="open linkedin"):
        webbrowser.open("http://linkedin.com")
    elif(c.lower()=="news"):
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if (r.status_code==200):
            data = r.json()

            articles = data.get('articles',[])

            for article in articles :
                speak(article['title'])    
    else:
        pass
if __name__ == "__main__":
    speak("intializing jarvis...")

while True:
    # obtain audio from the microphone
    r = sr.Recognizer()
    


    print ("recognizer")
    # recognize speech using Sphinx
    try:
       with sr.Microphone() as source:
          print("listening...")
          audio = r.listen(source, timeout =2, phrase_time_limit=1)
       word = r.recognize_google(audio)
       if (word.lower() == "jarvis"):
           speak("ya")

           with sr.Microphone() as source:
                print("jarvis active")
                audio = r.listen(source)
                command= r.recognize_google(audio)


                processComand(command)
    
    
    except Exception as e:
        print(" error; {0}".format(e))
 
