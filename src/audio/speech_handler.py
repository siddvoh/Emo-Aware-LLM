import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import time

def speak(text):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("output.mp3")
        audio = AudioSegment.from_mp3("output.mp3")
        play(audio)
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
        time.sleep(1)
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("output_retry.mp3")
        audio = AudioSegment.from_mp3("output_retry.mp3")
        play(audio)

recognizer = sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        speak("Could not request results; check your network connection.")
        return None