from gtts import gTTS
from playsound import playsound
from record_voice import recordVoice
from translate_to_text import *
from ask_to_chatgpt import askToChatGPT


recorded_sound_filename = "sounds/input.wav"
transcriptedfile = "sounds/transcriptedtext.txt"
chat_voice = "sounds/output_voice.wav"
chat_text= "sounds/output_text.txt"
language = "en"



recordVoice()
audio_url=upload(recorded_sound_filename)
save_transcript(audio_url,transcriptedfile)
askToChatGPT(transcriptedfile,chat_voice,chat_text)


playsound(chat_voice)
