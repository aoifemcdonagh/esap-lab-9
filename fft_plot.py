import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def get_FFT(filename):
	fs, data = wavfile.read(filename)  #Read from wavfile
	FFT = np.fft.fft(data)  # Get FFT 

	return FFT, fs

def get_PSD(FFT, fs):
	N = len(FFT)  # Get length of FFT
	FFT = FFT(1:N/2+1)  # Only need half 
	psd = (1/(fs*N)) * (np.abs(FFT)**2)
		
	

yes_FFT, fs = get_FFT('yes.wav')
plt.plot(yes_FFT[:len(yes_FFT)/2], 'g')
no_FFT, fs = get_FFT('no.wav')
plt.plot(no_FFT[:len(no_FFT)/2], 'r')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.show()

yes_PSD = get_PSD(yes_FFT, fs)



