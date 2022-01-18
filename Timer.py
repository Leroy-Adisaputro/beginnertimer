import time 
from posixpath import supports_unicode_filenames
import speech_recognition as sr
import pyttsx3

t = int(input("Enter the time in seconds:\n"))

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

while t:
    min = t // 60
    sec = t % 60
    timer = '{:02d}:{:02d}'.format(min, sec)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

print("Time is out!")
talk("Time is out!")
