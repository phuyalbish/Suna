import openai
from gtts import gTTS
from playsound import playsound
import json
from datetime import date,datetime
import urllib.request
import re
currentDateAndTime = datetime.now()

from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/home')
def home():
    with open ("templates/data.json") as json_file:
        data = json.load(json_file)
    return render_template('home.html', datas = data)
    
    
  
@app.route('/voicerecord', methods=['POST'])
def voicerecord():
    if request.method == 'POST':
        x = request.form.to_dict()
        update_to_json(1,x["ques"])
        
        
        all_words = x["ques"].split()
        first_word= all_words[0]
        
        actual_music = x["ques"][5:]
        joint_music = actual_music.replace(" ", "+")
        print(joint_music)
        if first_word == "play":
            
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+joint_music)
            videos_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            video_list = []
            i=0
            j=0
            while i < 5:
                flag = 1
                for x in video_list:
                    if videos_ids[j] == x:
                        flag=0
                        break
                if flag == 1:
                    video_list.append(videos_ids[j])
                    i = i+1
                j += 1
            
            playsound("voice.wav")
            update_to_json_music(3,video_list)

        else:
            answer = askToChatGPT(x["ques"])
            print(answer)
            update_to_json(2,answer[2:])
        return render_template('home.html')
    
 




def askToChatGPT(transcriptedtext):
    
    
    CHAT_APT ="#Your OPENAI API here"
    
    openai.api_key =CHAT_APT
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = transcriptedtext,
        max_tokens = 1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    
    speech = gTTS(text=response,lang="en", slow=False, tld="com.au")
    speech.save("output.wav")
    
    playsound("output.wav")
    return response




def update_to_json(typeofmessage,msg):
    currentTime = currentDateAndTime.strftime("%H:%M")
    def write_json(data, filename="templates/data.json"):
        with open (filename, "w") as f:
            json.dump(data, f, indent=4)
            
    with open ("templates/data.json") as json_file:
        data = json.load(json_file)
        temp = data["datas"]
        y = {
            "type": typeofmessage,
            "message": msg,
            "date": str(date.today()),
            "time": str(currentTime)
            }
        
        temp.append(y)
    write_json(data)
    


def update_to_json_music(typeofmessage,msg_music):
    currentTime = currentDateAndTime.strftime("%H:%M")
    def write_json(data, filename="templates/data.json"):
        with open (filename, "w") as f:
            json.dump(data, f, indent=4)
            
    with open ("templates/data.json") as json_file:
        data = json.load(json_file)
        temp = data["datas"]
        y = {
            "type": typeofmessage,
            "message": msg_music,
            "date": str(date.today()),
            "time": str(currentTime)
            }
        
        temp.append(y)
    write_json(data)
    

if __name__ == "__main__":
    app.run(debug=True) 
