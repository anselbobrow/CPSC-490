import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
import level_crossing as lc


def butter_lowpass_filter(data, cutoff, sample_rate):
    nyquist_rate = sample_rate / 2.
    b, a = butter(2, cutoff / nyquist_rate, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y


sample_rate, data = wavfile.read("audio/sheep.wav")
size = int(sample_rate)
sig = lc.normalize(data[0:size])

analog_sig = lc.interp_audio_seg(sig, size)
xings = lc.lvl_crossings(analog_sig)
interp_xings = lc.interp_lvl_crossings(xings)

x = np.arange(size)
y = butter_lowpass_filter(sig, 1000, sample_rate)
y_with_crossings = butter_lowpass_filter(interp_xings, 1000, sample_rate)
plt.plot(x, sig)
plt.plot(x, y, label="Uniform time")
plt.plot(x, y_with_crossings, label="Level-crossing")
plt.legend()
plt.title("Butterworth filter, level-crossing vs uniform")
plt.show()
