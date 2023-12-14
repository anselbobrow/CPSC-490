from scipy.io import wavfile
import matplotlib.pyplot as plt
import level_crossing as lc

TIME = .1
FILENAME = "audio/sheep.wav"

# read TIME seconds of audio samples from file
sample_rate, data = wavfile.read(FILENAME)
size = int(sample_rate * TIME)
# sampled_sig = lc.normalize(data)[0:size]
sampled_sig = lc.normalize(data[0:size])

# interpolate signal to get a cotinuous representation
sig = lc.interp_audio_seg(sampled_sig, size)

# generate level-crossing samples
xings = lc.lvl_crossings(sig)

# interpolate new signal from the generated samples
interp_y = lc.interp_lvl_crossings(xings)

lc.plot_level_crossings(xings)
# original signal vs reconstructed signal
lc.plot_sig(sig, 'g--')
lc.plot_sig(interp_y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
