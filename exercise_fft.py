import numpy as np

# Sampling rate(Hz)
sr = 20
print(1/sr)
time_vec = np.arange(0, 10, 1/sr)
# print(time_vec)
sig1 = np.sin(2*np.pi*time_vec)
print(sig1[:21])
print(np.round(sig1[:21],2))