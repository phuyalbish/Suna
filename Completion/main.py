from gtts import gTTS
from playsound import playsound
from record_voice import recordVoice
from translate_to_text import *
from ask_to_chatgpt import askToChatGPT


recorded_sound_filename = "sounds/input.wav"
transcriptedfile = "sounds/transcriptedtext.txt"
transcripted_voice = "sounds/output.wav"
language = "en"



recordVoice()
audio_url=upload(recorded_sound_filename)
save_transcript(audio_url,transcriptedfile)
askToChatGPT(transcriptedfile,transcripted_voice)


playsound(transcripted_voice)
