import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import os
import pywhatkit
import webbrowser
import wikipedia
import random

eng = pyttsx3.init("sapi5")
voices = eng.getProperty("voices")
eng.setProperty("voice",voices[0].id)

def speak(audio):
    eng.say(audio)
    eng.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    print("My name is Novice AI Bot. How may I help you?")
    speak("My name is Novice AI Bot. How may I help you?")

def takeCommand():
    #It takes audio from mic as input and returns str as output.
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... :)")
        rec.pause_threshold = 1
        rec.energy_threshold = 200
        audio = rec.listen(source)
    
    try:
        print("Recognizing... ;)")
        query = rec.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
        
    except Exception as e:
        print("Say that again...")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for tasks execution.
        if "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak("According to Wikipedia")
            speak(result)
        elif "bye" in query:
            speak("Bye Bye sir! See you soon.")
            exit()
        elif "open youtube" in query:
            speak("Opening Youtube...")
            url = "https:\\www.youtube.com"
            webbrowser.open(url)
        elif "open google" in query:
            speak("Opening google...")
            url_2 ="https:\\www.google.com"
            webbrowser.open(url_2)
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The time is ", strTime)
            speak(f"The time is {strTime}")
        elif "my name" in query:
            speak("Your name is Parth Raheja. You are the one who created me. Thanks for that hahaha.")
        elif "name of my mother" in query:
            speak("The name of your mother is Nidhi Raheja. She is really sweet. but she is slightly overweight. Moti mumma hahahahahahahaha")
        elif "name of my father" in query:
            speak("The name of your father is Arun Raheja. He is a really smart person.")
        elif "send a whatsapp message" in query:
            speak("Okay sure. Enter the recipients's number")
            num_msg = str(input("Enter number: \n"))
            speak("Great! Now Write your message that you want to send. ")
            message = (input("Enter your message: \n"))
            speak(f"Alright! your message is {message} Sending message")
            pywhatkit.sendwhatmsg_instantly(num_msg, message,5, tab_close=False)
        elif "toss a coin" in query:
            speak("Sure. Tossing a coin.")
            num_toss = random.randint(1,2)
            if num_toss == 1:
                print("Heads")
                speak("The coin shows Heads.")
            else:
                print("Tails")
                speak("The coin shows Tails")
        elif "random number" in query:
            num_ran = random.randint(1,50)
            print("The random number is", num_ran)
            speak(f"The random number is {num_ran}")
    