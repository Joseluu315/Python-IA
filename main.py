import speech_recognition as sr

listener = sr.Recognizer()
with sr.Microphone() as micro:
    print("¿Que necesitas?")
    sounds = listener.listen(micro)
    text = listener.recognize_google(sounds, language="es_ES")
    if print(text) == "Hola":
        print("Hola,¿como te llamas?")
        input(sounds)
        if sounds == "Antonio":
            print("Hola Antonio")
