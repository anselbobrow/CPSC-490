from scipy.io import wavfile
import level_crossing as lc
import matplotlib.pyplot as plt
import numpy as np
#
# sample_rate, data = wavfile.read("audio/sheep.wav")
# size = int(sample_rate)
# sampled_sig = lc.normalize(data[0:size])
#
# sig = lc.interp_audio_seg(sampled_sig, size)
#
# xings, err = lc.lvl_crossings_with_error(sig)
#
# print(err)
#
x_values = np.arange(4)
y1_values = [0.1391718088305171, 0.1340380337313888, 0.1341109435465007, 0.1340997842032969]
y2_values = [0.23281247649448122, 0.24303587098079826, 0.1341109435465007, 0.02273627542004199]

# Plot the first array (sin(x))
plt.plot(x_values, y1_values, label='Bit-depth', color='blue', linestyle='-')

# Plot the second array (cos(x))
plt.plot(x_values,
         y2_values,
         label='Time resolution',
         color='red',
         linestyle='-')

# Add labels and a legend
plt.xlabel('Precision')
plt.ylabel('RMS Error')
plt.title('Increasing precision of amplitude vs time')
plt.legend()

# Display the plot
plt.show()
