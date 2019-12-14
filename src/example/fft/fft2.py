# import matplotlib.pyplot as plt
# from scipy.io import wavfile as wave
# from scipy.io import _wav2array
# from scipy.fftpack import fft
# import numpy as np

# rate, data = wav.read('C:/Users/kimshinkeon/Desktop/peachpitch/src/example/fft/test.wav')
# fft_out = fft(data)

# plt.plot(data, np.abs(fft_out))
# plt.show()

# wav = wave.open('C:/Users/kimshinkeon/Desktop/peachpitch/src/example/fft/test.wav')
# rate = wav.getframerate()
# nchannels = wav.getnchannels()
# sampwidth = wav.getsampwidth()
# nframes = wav.getnframes()
# data = wav.readframes(nframes)
# wav.close()
# array = _wav2array(nchannels, sampwidth, data)
# print(rate, sampwidth, array )

import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import sounddevice as sd

# 3-가
samplerate, data = sio.wavfile.read('C:/Users/kimshinkeon/Desktop/peachpitch/src/example/fft/test.wav')

times = np.arange(len(data))/float(samplerate)

sd.play(data, samplerate)

plt.fill_between(times, data)
plt.xlim(times[0], times[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.show()