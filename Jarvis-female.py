from tkinter import *
import pyttsx3  # pip install pyttex3
import datetime
import speech_recognition as sr  # pip install sp.r
import wikipedia  # pip install
import smtplib
import webbrowser as wb
import psutil# pip install
import pyjokes  # pip install
import os
os.system('clear')
import pyautogui  # pip install
import random
import wolframalpha  # pip install
import json
import requests
from urllib.request import urlopen
import time
import ctypes






root = Tk()
root.title('jarvis!')
root.geometry("400x600")

root.mainloop()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wolframalpha_app_id = 'EGPE43-G93TU78LXR'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # for 12 hour
    speak("The current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back adity!")
    time_()
    date_()

    # Greeting

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Scarlett at your service. Please tell me how can I help you today?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say That agian Please....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # for this fuction to work you must enable to  security

    server.login('username@gmail.com', 'password')
    server.sendmail('username@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/KAPIL/Desktop/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)


def joke():
    speak(pyjokes.get_joke())


if __name__ == '__main__':

    wishme()

    while True:
        query = TakeCommand().lower()

        # all command will be stored in lower case in query
        # for easy recognition

        if 'time' in query:  # tell us time when asked
            time_()

        elif 'date' in query:  # tell us date when asked
            date_()

        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = TakeCommand()
                # provide reciver email address

                speak("who is the Reciever?")
                reciever = input("Enter Reciever,s Email :")
                to = reciever
                sendEmail(to, content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak("Unable to send Email.")


        elif 'search in chrome' in query:
            speak('what should I search?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            # chromepath is loacation of chrome,s installation on Computer

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')  # only open websites with '.com


        elif 'search youtube' in query:
            speak('What should I search?')
            search_trem = TakeCommand().lower()
            speak("Here We go to youtube!")
            wb.open('https://www.youtube.com/results?search_query=' + search_trem)

        elif 'search google' in query:
            speak('what should I search?')
            search_trem = TakeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q=' + search_trem)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going Offline sir!')
            quit()

        elif 'word' in query:
            speak('Opening MS Word....')
            ms_word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk'
            os.startfile(ms_word)

        elif 'power point' in query:
            speak('Opening MS Power point....')
            ms_ppt = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007.lnk'
            os.startfile(ms_ppt)

        elif 'excel' in query:
            speak('Opening MS excel....')
            ms_excel = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk'
            os.startfile(ms_excel)

        elif 'html code editor ' in query:
            speak('Opening brackets....')
            br_brackets = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brackets.lnk'
            os.startfile(br_brackets)



        elif 'write a note' in query:
            speak("What should I write, Sir!")
            notes = TakeCommand()
            file = open('notes.txt', 'w')
            speak("Sir should I include Date and Time ?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak('Done Taking Notes, SIR!')
            else:
                file.write(notes)

        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play video music' in query:
            songs_dir = 'E:\musi'
            music = os.listdir(songs_dir)
            speak('what should I play?')
            speak('select a number...')
            ans = TakeCommand().lower()
            while 'number' not in ans and ans != 'random' and ans != 'you choose':
                speak('I could not understand you. Please Try Agian.')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number', ''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(0, 19)
            os.startfile(os.path.join(songs_dir, music[no]))

        elif 'play song' in query:
            music_dir = 'E:\\1.MAIN\\jfg'
            song = os.listdir(music_dir)       
            speak('what should I play?')
            speak('select a number...')
            ans = TakeCommand().lower()
            while 'number' not in ans and ans != 'random' and ans != 'you choose':
                speak('I could not understand you. Please Try Agian.')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number', ''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(0, 97)
            os.startfile(os.path.join(music_dir, song[no]))


        elif 'remember that' in query:
            speak("what should I remember?")
            memory = TakeCommand()
            speak("you asked me to remember that" + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak('you asked me to remember that' + remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen(
                    "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d38ec9e7211342f5a2fe5ae614e511d5")
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top headline from the Entertainment Industry')
                print('=================Top Headline===============')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate" + location)
            wb.open_new_tab("https://www.google.com/maps/place/" + location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is : ' + answer)
            speak('The Answer is ' + answer)

        elif 'what is' in query or 'who is' in query:
            # use the same API key that we genrated earlier i.e. wolfa
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")
        elif 'stop listening' in query:
            speak('For How many Second you want me to stop listening to your commands?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
       

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "332011865ca1f96ecc927c54c164c6a7"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to Adity.")

        elif "who are you" in query:
            speak("I am your virtual assistant created by adity")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister adity ")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by adity.")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me Scarlett")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


