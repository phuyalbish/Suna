import openai
from gtts import gTTS
from secret_api import CHAT_APT


openai.api_key =CHAT_APT
model_engine = "text-davinci-003"

def askToChatGPT(transcriptedfile,transcripted_voice):
    with open(transcriptedfile) as f:
        prompt =f.read()
    
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text

    speech = gTTS(text=response,lang="en", slow=False, tld="com.au")
    speech.save(transcripted_voice)