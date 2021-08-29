import os  # communicate with the os 
from gtts import gTTS
from playsound import playsound
#from tempfile import TemporaryFile
language = "en-uk" #speaking language
for i in range(100):
    audio = "speech.mp3" 
    x = input("Enter the text: \n")
    sp = gTTS(text = x, lang = language,slow = False)
    sp.save(audio) # saving audio 
    playsound(audio) #playing the saved audio file 
    os.remove(audio)  # everytime removing the audio file for fresh file 
