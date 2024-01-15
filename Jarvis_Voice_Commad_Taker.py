import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyttsx3
from jarvis_play_game import rockPaperScissor


engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")


engine.setProperty("voices", voice[1].id)
engine.setProperty("rate", 130)
engine.setProperty("volume", 1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good morning, ")

    elif hour >= 12 and hour < 18:
        speak("Good Aftrnoon, ")

    elif hour >= 18 and hour < 24:
        speak("Good evening, ")
    else:
        speak("Good Morning")


def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.energy_threshold = 500

        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-In")
        print(f"Boss siad: {query}\n")
    except Exception as e:
        sen = "Command not match"
        print(sen)
        # speak(sen)
        return ""
    return query


def i_open(a):
    speak("Boss, I opened " + a + ".")


def shutdown_lap():
    try:
        os.system("shutdown /s /t 0")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    while True:  # first loop
        speak(
            "\n\nTo activate jarvis mode, Just say 'Activate Jarvis ' and  to exit from this program Just say 'exit'.\n"
        )
        print(
            "\n\nTo activate jarvis mode, Just say 'Activate Jarvis ' and  to exit from this program Just say 'exit'.\n"
        )

        firstCommand = takeComand().lower()
        if "activate jarvis" in firstCommand:
            speak("Jarvis Activated")
            round = 8
            while True:  # Second loop
                command = takeComand().lower()
                if "hello jarvis" in command or "wake up jarvis" in command:
                    if "hello jarvis" in command:
                        speak("Hello Boss")
                        wishME()
                        speak("How are you ?")
                    elif "wake up jarvis" in command:
                        speak("Yes Boss : Iam here now")
                        speak("How can I assist you Boss !")

                    while True:  # Third loop
                        query = takeComand().lower()
                        if "fine" in query or "iam good" in query:
                            speak("Copy that Boss")

                            speak("How may i help you ?")
                        elif "wake up jarvis" in query or "hello jarvis" in query:
                            if "hello jarvis" in query:
                                speak("yes boss, Do you need any help?")
                            elif "wake up" in query:
                                speak("Yes Boss : Iam here now")
                                wishME()
                                speak("How can I assist you Boss !")

                        elif "according to wikipedia" in query:
                            speak("Give me one second boss.")
                            try:
                                query = query.replace("according to wikipedia", " ?")
                                query = query.replace("jarvis tell me", "")
                                results = wikipedia.summary(query, sentences=2)
                                speak("Boss, According to wikipedia")
                                print(f"{query}\n{results}")
                                speak(results)
                                speak("I think it helpful Boss.")
                            except Exception as e:
                                speak("Could you repeat Boss?")
                        elif "open youtube" in query:
                            webbrowser.open("youtube.com")
                            i_open("youtube")

                        elif "open google" in query:
                            webbrowser.open("google.com")
                            i_open("google")

                        elif "shutdown" in query:
                            c = 0
                            while c < 3:
                                speak("Boss are you sure")
                                query = takeComand().lower()
                                if "yes" in query or "sure" in query:
                                    shutdown_lap()
                                elif "no" in query or "cancel" in query:
                                    speak("Boss i have cancelled shut down task")
                                    break
                                else:
                                    speak("confirm shutdown order")
                                    c += 1

                        elif "open nmk" in query:
                            webbrowser.open("nmk.co.in")
                            i_open("general advertisement website.")

                        elif (
                            "who are you" in query
                            or "about yourself" in query
                            or "what is the jarvis" in query
                        ):
                            if "about yourself" in query:
                                speak("Ok")

                            else:
                                speak("I will tell you my basic information")
                            speak(
                                "MY name is Jarvis, i am a virtual assistent design by mr.Dinesh Shinde. As a personal assistant of his dekstop "
                            )
                            speak("I am a scripted AI and i have limitation of Work.")
                            speak("I can perform many task.")
                            speak("some of these are")
                            speak(
                                "open youtube and play music and search any kind of  information on wikipedia and tell you correct time and many more..."
                            )
                            speak("Do you need any help ? Just say this")
                            print("Yes or NO")

                            while True:  # Fourth loop
                                c = takeComand().lower()
                                if "yes" in c:
                                    speak(
                                        "if you want any kind of information just say, give me information about this according to wikipedia."
                                    )
                                    break
                                elif "no" in c:
                                    speak(
                                        "Ok. Thank you to give your preciaus time. just say hey jarvis or hello jarvis for call me"
                                    )
                                    break

                        elif (
                            "play music" in query
                            or "play silent song" in query
                            or "silent song" in query
                            or "romantic songs" in query
                            or "i want to dance" in query
                            or "change the song" in query
                            or "morning song" in query
                            or "play song" in query
                            or "play music" in query
                            or "listen silent song" in query
                        ):
                            if "dance" in query:
                                speak("I think, You need to close the door")
                                music = "D:\\My_Music\\Romantic"
                                songs = os.listdir(music)
                                d = random.choice(songs)

                            elif "morning song" in query:
                                speak("Ok Boss")
                                music = "D:\\My_Music\Morning Song"
                                songs = os.listdir(music)
                                d = random.choice(songs)

                            elif "silent song" in query:
                                speak("Boss ,Is everything okay  ?")
                                while True:  # Fifth loop
                                    b = takeComand().lower()
                                    if "yes" in b:
                                        speak("copy that")
                                        break
                                    elif "no" in b:
                                        speak(
                                            "Don't wary boss, everything will be fine."
                                        )
                                        speak("I think, you will like this song")
                                        break
                                    else:
                                        speak("Boss ,Is everything okay  ?")
                                music = "D:\\My_Music\\Romantic"
                                songs = os.listdir(music)
                                d = random.choice(songs)

                            else:
                                music = "D:\\My_Music\\Romantic"
                                songs = os.listdir(music)
                                d = random.choice(songs)
                            speak("I am playing this song")
                            print(d)
                            os.startfile(os.path.join(music, d))

                        elif (
                            "jarvis play game" in query
                            or "i want to play game" in query
                            or "play game" in query
                            or "let's play game" in query
                        ):
                            rockPaperScissor()
                            speak(
                                "To play againg game to Voice play game or Voice exit for exit"
                            )
                            if "exit" in query:
                                print("program exited")
                                exit()

                        elif (
                            "jarvis sleep" in query
                            or "sleep jarvis" in query
                            or "i want to sleep" in query
                            or "jarvis mute" in query
                            or "sleep" in query
                        ):
                            if "sleep" in query:
                                speak("ok boss")
                                break
                            speak("Good Night, Sweet Dream Boss")
                            break
                        elif (
                            "what's the time" in query
                            or "what is the time" in query
                            or "tell me time" in query
                            or "right time" in query
                            or "tell me correct time" in query
                        ):
                            strTime = datetime.datetime.now().strftime("%I:%M %p")

                            speak(f"its {strTime} Boss")
                        elif "open code" in query or "open visual studio code" in query:
                            speak("Ok ")

                            fileLocation = "C:\\Users\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                            os.startfile(fileLocation)
                            i_open("visual studio code")

                        elif "java editor" in query or "java ide" in query:
                            speak("Ok ")
                            fileLocation = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2023.1.3\\bin\\idea64.exe"
                            os.startfile(fileLocation)
                            i_open("IntelliJ IDEA Community Edition")

                        elif "python editor" in query or "python ide" in query:
                            speak("Ok ")
                            fileLocation = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm64.exe"
                            os.startfile(fileLocation)
                            i_open("PyCharm IDEA Community Edition")

                        elif "word document" in query:
                            speak("Ok ")
                            fileLocation = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                            os.startfile(fileLocation)
                            i_open("word document")

                        elif "open excel" in query:
                            speak("Ok")
                            fileLocation = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                            os.startfile(fileLocation)
                            i_open("Excel")

                        elif "open power point" in query or "open ppt" in query:
                            speak("Ok")
                            fileLocation = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                            os.startfile(fileLocation)
                            i_open("Power point")

                        elif "open command prompt" in query or "open cmd" in query:
                            speak("Ok")
                            fileLocation = "%windir%\\system32\\cmd.exe"
                            os.startfile(fileLocation)
                            i_open("Command Prompt")

                        elif "open chrome" in query or "browser" in query:
                            speak("Ok")
                            fileLocation = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                            os.startfile(fileLocation)
                            i_open("Google Chrome")
                        elif (
                            "java tutorial" in query
                            or "python tutorial" in query
                            or "software engineering tutorial" in query
                            or "dsa tutorial" in query
                            or "open channele of harry" in query
                            or "open web development" in query
                        ):
                            if "java" in query:
                                speak("Boss  Searching for Best Java tutorial")
                                webbrowser.open(
                                    "https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q"
                                )
                                i_open("Java tutorial of Harry Sir")
                            elif "python" in query:
                                speak("Boss  Searching for Best python tutorial")
                                webbrowser.open(
                                    "https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg"
                                )
                                i_open("python tutorial of Harry Sir")
                            elif "dsa" in query:
                                speak(
                                    "Boss  Searching for Best Data Structure and Alogrithm tutorial"
                                )
                                webbrowser.open(
                                    "https://www.youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi"
                                )
                                i_open(
                                    "Data Structure and Algorithm  tutorial of Harry Sir"
                                )
                            elif "harry" in query:
                                speak("Ok boss")
                                webbrowser.open(
                                    "https://www.youtube.com/@CodeWithHarry"
                                )
                                i_open(
                                    "This is the youtube channel of one of the best coding teacher"
                                )
                            elif "software" in query:
                                speak("Serching for Software Engineering tutorial")
                                webbrowser.open(
                                    "https://www.youtube.com/playlist?list=PLxCzCOWd7aiEed7SKZBnC6ypFDWYLRvB2"
                                )
                                i_open(
                                    "One of the best tutorial of Software Engineering"
                                )
                            elif "open web development" in query:
                                speak(
                                    "Serching for one of the best web devlopment tutorial"
                                )
                                webbrowser.open(
                                    "https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg"
                                )
                                i_open("web development tutorial of Harry sir")

                            while True:  # Sixth loop
                                speak("Boss is you really looking for this ?")

                                us = takeComand().lower()
                                if "yes" in us:
                                    speak(
                                        "Ok boss, i will not disturb you. To activate me just say  'wake up Jarvis'."
                                    )
                                    break
                                elif "no" in us:
                                    speak(" Boss I am  really sorry")
                                    speak("Could you please see this,for me")
                                    break

                        elif "open amazon" in query or "op en shopping app" in query:
                            webbrowser.open("https://www.amazon.com//")
                            i_open("Amazon shopping application")

                        elif "open flipkart" in query:
                            webbrowser.open("https://www.flipkart.com//")
                            i_open("flipkart shopping application")

                        elif "other shopping application" in query:
                            webbrowser.open("https://www.meesho.com//")
                            i_open("meesho shopping application")

                        elif (
                            "turn off yourself" in query
                            or "i have to go" in query
                            or "by jarvis" in query
                        ):
                            if "turn off" in query:
                                speak("Ok boss take care. see you soon, ")
                                exit(0)
                            elif "have to go":
                                speak(
                                    "Sure boss. I think you have important work. all the best, see you soon"
                                )
                                exit(0)
                            elif "by" in query:
                                speak("take care boss. by")
                                exit(0)
                            elif "wake up jarvis" in query:
                                speak("Yes Boss, now I am  here")
                        elif not (query == "*jarvix*_8__97"):
                            # print(len(query))
                            if 0 < len(query) and len(query) <= 9:
                                speak(
                                    "Sorry boss, But i'm not program for this yet. If you have any other work for me, Just tell me boss"
                                )
                            elif len(query) > 10:
                                print("Sorry boss, but can't understand.")
                            else:
                                print("Did you said something ?")

        elif " exit" in firstCommand or "exit" in firstCommand:
            speak("Program exited\n")
            print("Program exited\n")
            exit(0)

        else:
            print("Unable to activate jarvis mode")
