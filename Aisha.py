import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os 
import webbrowser
import random
from emails import sendEmail,sendMail

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    printAndSpeak("Hello , how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:
        print("sorry can you Say that again ......")
        return "None"
    return command

    while True:
        speak("ok speak your friend name")
        try:
            name=takeCommand().lower()
            print(name)
            if name in  dict[name]:
                print("can you speak your message.")
                speak("can you speak your message.")
                content = takeCommand().lower()
                print("do yo want to send a message")
                speak("do yo want to send a message")
                confirm = takeCommand().lower()
                if 'yes' in confirm:
                    try:
                        to = dict[name]
                        sendEmail(to, content)
                        print("Email has been sent!")
                        speak("Email has been sent!")
                        break
                    except Exception as e:
                        print("message sending failed")
                        speak("message sending failed")
                        continue
                elif 'no' in confirm:
                    print("message sending process cancel..")
                    speak("message sending process cancel")
                    break
        except Exception as e:
            speak("can you say again your friend name")

def printAndSpeak(s):
    print(s)
    speak(s)

if __name__ == "__main__":
    wishMe()
    i=0
    while True:
        command = takeCommand().lower()
        if 'wikipedia' in command:
            printAndSpeak("Searching  wikipedia...")
            command = command.replace("wikipedia","")
            result = wikipedia.summary(command, sentences=2)
            printAndSpeak("according to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in command:
            printAndSpeak("youtube is opening")
            webbrowser.get('windows-default').open("https://youtube.com")

        elif 'open facebook' in command:
            printAndSpeak("facebook is opening")
            webbrowser.get('windows-default').open("https://facebook.com")

        elif 'open whatsapp' in command:
            printAndSpeak("whatsapp opening")
            webbrowser.get('windows-default').open('https://web.whatsapp.com')
        
        elif 'open google' in command:
            print("google is opening.")
            webbrowser.get('windows-default').open("https://google.com")

        elif '.com' in command:
           try:
               word=command.split()
               website=word[-1]
               chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
               printAndSpeak(website+" is opening")
               webbrowser.get(chrome).open('http://www.' + website)
               continue
           except Exception as e:
               print(e)
               word = command.split()
               website = word[-1]
               printAndSpeak(website+" is opening")
               webbrowser.get('windows-default').open('http://www.' + website)
               continue
        elif 'internet' in command or 'google' in command:
                text = command
                temp = ['please','search','on internet','internet','on','google']
                WordFormCommand = text.split()
                try:
                    finalwords = (words for words in WordFormCommand if words not in temp)
                    final = ' '.join(finalwords)
                    chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
                    printAndSpeak(final + " is searching on google")
                    webbrowser.get(chrome).open('http://www.google.com/?#q='+final)
                except Exception as e:
                    print(e)

        elif 'hello' in command or 'hi' in command:
            printAndSpeak("hello how are you")

        elif 'who are you' in command or 'your name' in command:
            printAndSpeak("i am AIsha . Artificial Intelligence assistant.")

        elif 'how are you' in command:
            printAndSpeak("I am fine and you ?")

        elif 'i am also fine' in command or 'i am very well' in command :
            printAndSpeak("good")

        elif 'thanks' in command or 'thank you' in command:
            printAndSpeak("you are welcome.")

        elif 'play music' in command or 'start music' in command:
            music_dir = 'E:\\hindi songs'
            songs = random.choice(os.listdir(music_dir))
            printAndSpeak(songs)
            os.startfile(os.path.join(music_dir, songs))

        elif 'time' in command:
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")
            printAndSpeak(f"the time is {currentTime}")

        elif 'calculator' in command:
            os.startfile("C:\\Windows\\System32\\calc.exe")

        elif 'what can you do' in command or 'help' in command:
            printAndSpeak("I can do small things that you give such as \n  "
                          "1 Every application will be open  \n using command \"open\" and \" your apllication name\" like \"open google\" or  \"open youtube\" \n"
                          "2.I can search your query on wikipedia and will be give best result \n using command \"wikipedia\" and \"then your query.\"  \n")

        elif 'email' in command:
            sendMail()

        elif 'shutdown my computer' in command or 'shutdown my pc' in command or 'shutdown my laptop' in command or 'please shut down' in command:
            speak("do you want shutdown your computer system")
            confirm = takeCommand().lower()
            if 'yes' in confirm:
                printAndSpeak("The computer is shutting down.")
                os.system("C:/Windows/System32/shutdown.exe")
                break
            elif 'no' in confirm:
                printAndSpeak("Confirmation has been canceled")
                continue
            else:
                printAndSpeak("please confirm your task")

        elif 'sleep my computer' in command or 'sleep my pc' in command or 'sleep my laptop' in command or 'please sleep' in command:
            speak("do you sleep your computer system")
            confirm = takeCommand().lower()
            if 'yes' in confirm:
                printAndSpeak("The computer is sleeping down.")
                try:
                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                except Exception as e:
                    print(e)

            elif 'no' in confirm:
                printAndSpeak("Confirmation has been canceled")
                continue
            elif '' in command:
                printAndSpeak("please confirm your task")


        elif 'goodbye' in command:
            bye = "ok bye, see you later"
            printAndSpeak("bye")
            exit()

        elif '' in command:
            if(i==5):
                printAndSpeak("please ask me, I am listening")

        i+=1
        if(i==10):
            break

