import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

def butter_lowpass(cutoff, fs, order=5):
	nyq = 0.5 * fs
	normal_cutoff = cutoff / nyq
	b, a = butter(order, normal_cutoff, btype='low', analog=False)
	return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
	b, a = butter_lowpass(cutoff, fs, order=order)
	y = lfilter(b, a, data)
	return y

# Filter specs
order = 6
fs = 30.0
cutoff = 3.667

# Getting filter coefficients 
b,a = butter_lowpass(cutoff, fs, order)

# Plot frequency response
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass filter freq response")
plt.xlabel('Frequency [Hz]')
plt.grid()

# Make up a signal to be filtered
T = 5.0		# number of seconds
n = int(T*fs)	# number of samples
t = np.linspace(0, T, n, endpoint=False)

# "Noisy data" which we want to recover 1.2 Hz signal from
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filter data
y = butter_lowpass_filter(data, cutoff, fs, order)

plt.subplot(2,1,2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
plt.show()
