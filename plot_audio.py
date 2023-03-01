import wave
import matplotlib.pyplot as plt
import numpy as np

#reasding wav file in binary mode
obj = wave.open("Rashika.wav","rb")

#reading all parameters
sample_freq = obj.getframerate()
n_sample = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

#calulate the length of the signal in seconds
t_audio = n_sample / sample_freq
print(t_audio)

#creating numpy array
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

#object for the xaxis 
times = np.linspace(0,t_audio, num=n_sample)

#creating a figure to plot 
plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time(s)")
plt.xlim(0,t_audio)
plt.show()