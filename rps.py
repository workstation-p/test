import speech_recognition as sr
import pyttsx3
import webbrowser
import time

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def open_website(command):
    if "open google" in command:
        # Example: Open Google
        webbrowser.open("https://www.google.com")
        speak("opening google.")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("opening youtube.")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("opening facebook.")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("opening instagram. ")
    else:
        speak("I can only open Google, YouTube, and Facebook.")

def main():
    speak("Hello! I am your assistant. What would you like to do?")
    while True:
        command = listen()
        if command:
            open_website(command)
        time.sleep(1)
        

main()