import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'record.wav'

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format = FORMAT,
        channels = CHANNELS,
        rate = RATE, 
        input = True,
        frames_per_buffer = CHUNK)
print("recording...")

frames = []

for i in range(0, int(RATE * RECORD_SECONDS / CHUNK)) :
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()
audio.terminate()
print("Stop recording")

# save the recording
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
