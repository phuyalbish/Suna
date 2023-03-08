import wave
obj = wave.open("sounds/star.wav","rb")



print("Channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of Frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()

print(t_audio)
frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))


obj.close()

obj_new = wave.open("sounds/star_new.wav","wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(22050.0)
obj_new.writeframes(frames)   
obj.close()