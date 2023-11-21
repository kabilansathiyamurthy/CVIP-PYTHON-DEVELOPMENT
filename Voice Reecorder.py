#for Voice recording,  we need to take the sounds as input. So we are using these packages
import sounddevice
from scipy.io.wavfile import write

#Sampling Recording , for high Quality i am using 44100 Frames Per Sencond
fs= 44100

#Getting the duration of Recording
second =  int(input("Enter time duration in seconds: "))
#After the time over the recording automatically starts to save.
#Started Recording
print("Recording.....n")

#Process
#Here the process begines , The fs refers to the FPS.
#The Channels refers to the Output number of Output needed Like Mono , Stereo (Left & Right) , etc
record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 2 )
sounddevice.wait()
write("out.wav",fs,record_voice)

#Completed
print("Finished.....nPlease check your output file")