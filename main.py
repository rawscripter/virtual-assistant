import webbrowser
from math import factorial
import random
import os
import playsound
import time
from time import ctime
from time import strftime
import speech_recognition as sr
from gtts import gTTS
import subprocess
r = sr.Recognizer()
# record audio


def raw_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    randomNumber = random.randint(0, 1999999)
    audio_file = 'audio-' + str(randomNumber) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def record_audio():
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source, duration=2)
        # r.energy_threshold()
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except:
            print("sorry, could not recognise")
        return voice_data


def calculate_from_voice_data(voice_data):
    inputString = voice_data
    numbers = []
    mathOps = ['+', '-', '/']
    for word in inputString.split():
        if word.isdigit():
            numbers.append(word)
        if word in mathOps:
            numbers.append(word)
    # convert array to string
    numbersStringList = ''.join(str(e) for e in numbers)
    result = str(eval(numbersStringList))
    raw_speak(result)


def respond(voice_data):
    print(voice_data)

    if('hi' in voice_data):
        raw_speak("Hello")
        return

    if('open Firefox' in voice_data):
        print('opening')
        subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
        return

    if('open Chrome' in voice_data):
        subprocess.call(
            ['C:\Program Files\Google\Chrome Dev\Application\chrome.exe'])

    if('open Google Chrome' in voice_data):
        subprocess.call(
            ['C:\Program Files\Google\Chrome Dev\Application\chrome.exe'])

    if('open Google' in voice_data):
        webbrowser.open('https://www.google.com')

    if('open YouTube' in voice_data):
        webbrowser.open('https://www.youtube.com')

    if ('how are you' in voice_data):
        raw_speak("I am fine and you?")
        return

    if ('what is your name' in voice_data):
        raw_speak("My name is raw")
        return

    if ('do something' in voice_data):
        raw_speak("what can i do for you")
        return

    if ('what time is it' in voice_data):
        string = strftime("%I %M %p")
        raw_speak(string)
        return

    if ('what is' in voice_data):
        calculate_from_voice_data(voice_data)

    if ('calculate' in voice_data):
        calculate_from_voice_data(voice_data)

    if ('exit' in voice_data):
        raw_speak('bye')
        exit()


time.sleep(1)
print("listening...")
while 1:
    voice_data = record_audio()
    respond(voice_data)
