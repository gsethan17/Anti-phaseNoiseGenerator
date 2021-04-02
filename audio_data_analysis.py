import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()
info = p.get_default_input_device_info()

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = info['defaultSampleRate']

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = int(RATE),
    input = True,
    output = True,
    frames_per_buffer = CHUNK
    )

fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))

while True :
    data = stream.read(CHUNK)

    # data convert from byte to int
    # length of read data is double of chunk.
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    data_int = np.array(data_int, dtype=np.int16) + 127  # dtype 'b' is integer 0 to 255, and '+127' is needed to set the center line
    data_int = data_int[::2]  # get the data every 2 step. skipping data.

    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()
