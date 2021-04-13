import librosa
import os
from utils import *

data_path = os.path.join(os.getcwd(), 'data', 'sample')
print(os.listdir(data_path))
path = os.path.join(data_path, os.listdir(data_path)[1])

y, sr = librosa.load(path)

print(y[10000:10100])
print(sr)

# draw_wave(y[10000:10100], sr)
draw_plot(y[10000:20000])