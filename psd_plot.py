from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs/2
time = np.arange(N)/fs
x = amp*np.sin(2*np.pi*freq*time)
# Uncomment the following line to add noise to signal
# x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

ps = np.abs(np.fft.fft(x))**2

time_step = 1 / 30
freqs = np.fft.fftfreq(x.size, time_step)
idx = np.argsort(freqs)

plt.plot(freqs[idx], ps[idx])
