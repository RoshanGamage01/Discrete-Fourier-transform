from dft import *
import numpy as np
import matplotlib.pyplot as plt
import wave
from util import *

audio = wave.open("audio_signal/picture_music.wav", 'r')
sample_rate = audio.getframerate()
audio_data = np.frombuffer(audio.readframes(-1), dtype=np.int16)
audio.close()

dft_result = dft(audio_data, sample_rate)

# PLOT THE FREQUANCY SPECTRUM
max_freq = len(audio_data) // 2
frequencies = np.arange(max_freq) / max_freq * sample_rate # fk = (k / N) * sample rate
amplitudes = np.zeros(max_freq)

for k in range(max_freq):
    magnitude = np.abs(dft_result['dft_coefficients'][k])
    amplitudes[k] = magnitude / max_freq

plt.figure(figsize=(10, 8))
plt.plot(frequencies, amplitudes, 'b')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum of Audio Signal')
plt.show()

# INVERSE FOURIER TRANSFORM
idft_result = idft(dft_result['dft_coefficients'], len(audio_data))
save_as_audio_file(idft_result.real, sample_rate, 'idft_output.wav')
