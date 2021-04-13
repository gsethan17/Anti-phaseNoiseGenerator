import librosa.display
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np

class get_data :
    def __init__(self, path, frame_size = 1024, num_mu = 256):
        self.sr, self.wav = read(path)
        self.wav = np.array(self.wav, dtype=np.int16)
        self.frame_size = frame_size
        self.num_mu = num_mu
        self.total_data = np.zeros((len(self.wav), self.num_mu))
        self.x =
        self.y =

    def standardization(self, x, x_max=int(2 ** 16)):
        X_std = x / x_max
        return X_std

    def mu_law_companding(self, x, mu=256) :
        mu = mu - 1
        fx = np.sign(x) * np.log(1 + mu * np.abs(x)) / np.log(1 + mu)
        fx = np.floor((fx + 1)/2*mu + 0.5).astype(np.int8)
        return fx

    def one_hot(self, x, num=256):
        encoding = np.eye(num)[x]
        return encoding

    def encode(self):
        data = self.standardization(self.wav)
        data = self.mu_law_companding(data)
        self.total_data = self.one_hot(data)

    def split(self):

        return self.x, self.y


def draw_wave(y, sr = 44100) :
    plt.figure(figsize = (16, 6))
    librosa.display.waveplot(y=y, sr=sr)
    plt.show()

def draw_plot(y) :
    plt.figure(figsize=(16, 6))
    plt.plot(y)
    plt.show()


if __name__ == "__main__" :
    data = get_data("./data/sample/60kph.wav")
    data.encode()
    draw_plot(np.argmax(data.total_data, axis = 1))
    data.split()


    # wav = get_wave("./data/sample/60kph.wav")
    # wav_std = standardization(wav)
    # wav_com = mu_law_companding(wav_std)
    # draw_plot(wav_com[41000:41010])
    # print(wav_com[41000:41010])
    # x = one_hot(wav_com[41000:41010])
    # print(x[0][69])
    # print(x[2][68])
    # print(x.shape)
