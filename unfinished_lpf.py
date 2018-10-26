import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


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
T = 		# number of seconds
n = 		# number of samples
t = 

# "Noisy data" which we want to recover 1.2 Hz signal from
data = 

# Filter data
y = 

plt.subplot(2,1,2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
plt.show()
