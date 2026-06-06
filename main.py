import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
import numpy as np
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

def record_audio(duration=2, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(audio.tobytes(), fs, 2)


if __name__ == "__main__":
    speak("Initialising Assistant....")

    while True:
        print("Recognizing.....")
        try:
            audio = record_audio(duration=2)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yaa")
                audio = record_audio(duration=5)
                command = recognizer.recognize_google(audio)

                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))