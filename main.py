
import sys
from api_communication import *
#upload

filename = sys.argv[1]


#transcribe



audio_url=upload(filename)
save_transcript(audio_url,filename)