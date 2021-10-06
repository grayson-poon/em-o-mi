import pyaudio
import wave
# from array import array
# from struct import pack

def record(outputFile):
  chunk = 1024 # size of file in bytes
  sample_format = pyaudio.paInt16 # format and bit depth are the same, using 16 or 24 bits per sample
  num_channels = 1 # stereo channel (1 = monochannel) NUM CHANNELS HAS TO BE 1 FOR MAC
  fs = 44100 # sampling freq. = cycles/sec
  record_seconds = 5 # record audio for 5 sec

  p = pyaudio.PyAudio() # creates a pyaudio instance
  print("*recording")

  # open stream object as input
  stream = p.open(format = sample_format,
                  channels = num_channels,
                  rate = fs,
                  input=True,
                  frames_per_buffer=chunk)
  
  frames = []

  for i in range(0, int(fs / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

  
  # stop/close stream
  stream.stop_stream()
  stream.close()
  p.terminate()

  print("*done recoring")

  # save recorded data as WAV file
  wf = wave.open(outputFile, 'wb')
  wf.setnchannels(num_channels)
  wf.setsampwidth(p.get_sample_size(sample_format))
  wf.setframerate(fs)
  wf.writeframes(b''.join(frames))
  wf.close()

record('output2.wav') # store recording with name 'output1.wav'