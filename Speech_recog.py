import speech_recognition
import pyttsx3


def speechRecognition():
    recognizer = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.3)
            print("Say Something:")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Me:{text}")
    except:
        text = "didn't you understand me?"
    return text        