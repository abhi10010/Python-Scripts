import pyttsx3

def TextToSpeech(file_name = "TheRoadNotTaken.txt"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') # getting details of all the voices available
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    
    engine.setProperty('voice', voices[0].id) # using a male voice
    engine.setProperty('rate', 175) # reducing the rate to 175 from 200(default)

    file = open(file_name, "r")

    for sentence in file:
        engine.say(sentence)

    engine.runAndWait()

TextToSpeech()
