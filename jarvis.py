import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()



def speak(audio):
    if not engine.isBusy():
        engine.say(audio)
        engine.runAndWait()
    else:
        print("Engine is busy, cannot speak at the moment")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir")

    speak("Jarvis at your service sir, please tell me how may I help you.")
    print("Jarvis at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        query=query.lower()
        if query.endswith("jarvis"):
          print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"
    if query.endswith("jarvis"):
      return query
    else:
        return ""

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm JARVIS and I'm a desktop voice assistant.")
            print("I'm JARVIS and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "tell me something" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("tell me something","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            speak("opening youtube")
            wb.open("youtube.com") 

        elif "open google" in query:
            speak("opening google")
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            speak("opening stackoverflow")
            wb.open("stackoverflow.com")
        
        elif query.startswith("open"):
            wb.open(query[5:-7]+".com")

        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "start chrome" in query:
            try:
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)
            except Exception as e:
                speak("File location not found")
                print("File location not found")
            

        elif "search on chrome" in query:
            try:
                # speak("What should I search?")
                # print("What should I search?")
                # chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                # search = takecommand()
                # wb.get(chromePath).open_new_tab(search)
                # print(search)
                speak("What should I search?")
                print("What should I search?")
                search_query = takecommand()
                wb.open_new_tab(search_query)
                print(search_query)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        
        elif "just remember" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")


        elif "offline" in query:
            quit()


