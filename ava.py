import datetime #it take current date and time
import pyttsx3  #it convert speech into text
import speech_recognition as sr  #it take microphone input from user and return string output
import wikipedia    # use for searching about anything through wikipedia
import webbrowser   # use for web search
import os    
import subprocess   
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    speak("I am Ava, Tell me how can I help you")

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        #print(e)   
        speak("Sorry, Surbhi I can't understand. Can you please say it again.") 

        return "None"
     
    return query
    

    

if __name__== "__main__":
    #speak("surbhi is sweet")
    wishMe()
    while True:    #use when we want Ava listen one query only when we want she listen unlimited time.then use True
        query = takeCommand().lower()  #All the commands said by user will be stored here in 'query' and will be converted to lower case for easily recognition of command

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  #read upto two sentences from wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)
          
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak("Here you go to Github\n")
            webbrowser.open("github.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or 'play song' in query:
            speak("Here you go to Song\n")
            webbrowser.open("music.youtube.com")
    
        elif 'open visual Studio code' in query:
            speak("Hey coder, I am opening visual code for you give me a minute")
            codePath = "C:\\Users\\SURBHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("Hope you are also fine")

        elif 'who are you' in query:
            speak("I am Ava, Surbhi has created me")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Surbhi, the time is {strTime}")
        
        elif 'exit' in query:
            speak("Thanks Surbhi, Have a good day")
            exit()