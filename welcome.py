import pyttsx3
import datetime
import pyaudio
import wikipedia
import speech_recognition as sr


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
 engine.say(audio)
 
 
def wishMe():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
  speak("Good morning")
  print("Good morning")
  
 elif hour>=12 and hour<18:
  speak("Good afternoon")
  print("Good afternoon")
 else:
  speak("Good evening")
  print("Good evening")
 speak("Hi! My name is Zee! How can I help you!")
 print("Hi! My name is Zee! How can I help you!")
 
def takeCommand():
 '''
 doc string
 it takes microphone input from user and returns string output
 '''

 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Listening. . .")
  r.pause_threshold = 1
  audio = r.listen(source)

 try:
  print("Recognizing. . .")
  query = r.recognize_google(audio, Language='en-in')
 # print(f"User said: , {query}\n")
  
 except Exception as e:
  #print(e)
  
  print("Say that again please. . .")
  return "None"
 return query 
 
if __name__ == "__main__":
 #speak("Priyanka is a good girl")
 wishMe()
 #takeCommand()
 #while True:
  #query = takeCommand().lower()
 
 
 engine.runAndWait()