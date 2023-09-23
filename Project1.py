import pyttsx3

engine = pyttsx3.init()
engine.say("Hey gus,this is a text to   oh my goodness I am a robot")
engine.runAndWait()
engine.say("Firstly!!!   I wanna ask one Question which is ?" + "How are you?")
engine.runAndWait()
engine.stop()