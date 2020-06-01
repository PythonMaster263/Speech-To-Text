import speech_recognition as sr
import pyautogui

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak to Write...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')


    except Exception as e:
        # print(e)

        print("Say that again Please...")
        return "None"
    return query

if __name__ == "__main__":

    while True:
        query = takeCommand().lower()
        pyautogui.write(query)

