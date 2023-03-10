

from gtts import gTTS
from playsound import playsound
# from record_voice import recordVoice
# from translate_to_text import *
from ask_to_chatgpt import askToChatGPT
from Speech_recog import speechRecognition

recorded_sound_filename = "sounds/input.wav"
transcriptedfile = "sounds/transcriptedtext.txt"
chat_voice = "sounds/output_voice.wav"
chat_text= "sounds/output_text.txt"
language = "en"



# recordVoice()
# audio_url=upload(recorded_sound_filename)
# save_transcript(audio_url,transcriptedfile)

transcriptedtext = speechRecognition()
askToChatGPT(transcriptedtext,chat_voice,chat_text)
playsound(chat_voice)

with open(transcriptedfile, "w") as f:
            f.write(transcriptedtext)

