
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import subprocess
import pylint
import wikipedia
import re
import os # to remove created audio files

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser

# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f"You: {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"app: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is app")
        else:
            speak("my name is app. what's your name?")

    if there_exists(["my name is","I am"]):
        person_name = voice_data.split()[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5: search google
    if there_exists(["search for","google","search in google","search"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        speak(f'Here is what I found for {search_term} on google')
        webbrowser.get().open(url)

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        speak(f'Here is what I found for {search_term} on youtube')
        webbrowser.get().open(url)
    
    # 7: open folders:
    
    # pictures
    if there_exists(['pictures folder']):
        pictures_path = 'C:\\Users\\mbmab\\Pictures'
        speak("Pictures folder is opened")
        os.startfile(pictures_path)
        
    # Downloads
    if there_exists(['downloads folder']):
        Downloads_path = 'C:\\Users\\mbmab\\Downloads'
        speak("Downloads folder is opened")
        os.startfile(Downloads_path)
        

    # Desktop
    if there_exists(['desktop folder']):
        Desktop_path = 'C:\\Users\\mbmab\\Desktop'
        speak("Desktop folder is opened")    
        os.startfile(Desktop_path)

    # Documents
    if there_exists(['documents folder']):
        Documents_path = 'C:\\Users\\mbmab\\Documents'
        speak("Documents folder is opened")
        os.startfile(Documents_path)

    # 8: open apps

    #chrome
    if there_exists(['chrome']):
        speak("Google Chrome is opened")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    # 9: Thanks
    if there_exists(["thanks", "thank"]):
        speak("you are welcome, I'm here to help you")
    
     # 10: Love
    if there_exists(["i love you", "i like you"]):
        loves = ["love you too", "me too, sweetie", "prove it"]
        love = loves[random.randint(0,len(loves)-1)]
        speak(love)

    # 11: miss
    if there_exists(["i miss you"]):
        speak("I miss you too...")

    # 12: bad words
    if there_exists(["shut up","fuck you", "fuck", "f***"]):
        speak("Sorry, I can not answer for these bad words")
        
    # 13: exit
    if there_exists(["exit", "quit", "goodbye","bye"]):
        speak("going offline")
        exit()


time.sleep(5)

person_obj = person()
while 1:
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond