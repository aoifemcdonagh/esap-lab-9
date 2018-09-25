import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def get_FFT(filename):
	fs, data = wavfile.read(filename)  #Read from wavfile
	FFT = np.fft.fft(data)  # Get FFT 

	return FFT, fs

# Move to psd_plot.py
def get_PSD(FFT, fs):
	N = len(FFT)  # Get length of FFT
	FFT = FFT[1:N/2+1]  # FFT should have symmetry around 0 b/c input waveform is real instead of complex
			    # therefore, only need first half b/c second half is a mirror of the first 
	psd = (1/(fs*N)) * (np.abs(FFT)**2)  # get abs value which is the magnitude (phase isn't needed here)
	psd[1:-1] = 2*psd[1:-1]  # Multiply by 2 to conserve total power
				 # Don't mult zero freq (DC) or nyquist freq because they don't occur twice
				 # i.e. there is symmetry around these points
	return psd
	

# yes_fs, yes_data = wavfile.read('yes.wav')  #Read from wavfile
# no_fs, no_data = wavfile.read('no.wav')  #Read from wavfile


yes_FFT, yes_fs = get_FFT('yes.wav')
plt.plot(yes_FFT[:len(yes_FFT)/2], 'g')
no_FFT, no_fs = get_FFT('no.wav')
plt.plot(no_FFT[:len(no_FFT)/2], 'r')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.show()

# From here to move to psd_plot.py
# yes_PSD = get_PSD(yes_FFT, yes_fs)
# no_PSD = get_PSD(no_PSD, no_fs)

# plt.plt(freq, 10*np.log10(yes_PSD), 'g')
# plt.show()


	


