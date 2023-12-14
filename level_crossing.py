import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# modify these parameters
RESOLUTION = 100000  # freq of clock tick in Hz
BIT_DEPTH = 8  # determines number of thresholds

SIG_MIN = -1.
SIG_MAX = 1.
PERIOD = 2. * np.pi
N_LEVELS = 2**BIT_DEPTH


def normalize(sig):
    return sig / (np.max(np.abs(sig)))


# arbitrary signal for testing
def f(x):
    return normalize(np.sin(x) + np.sin(x * 4.2))


def interp_audio_seg(data, n):
    res = np.arange(RESOLUTION)
    new_x = np.linspace(0., RESOLUTION, n)
    return interp1d(new_x, data, fill_value='extrapolate', kind='cubic')(res)


def interp_lvl_crossings(crossings):
    x = []
    y = []
    for arr, thresh in crossings:
        for crossing in arr:
            if (crossing not in x):
                x.append(crossing)
                y.append(thresh)
    res = np.arange(RESOLUTION)
    return interp1d(x, y, fill_value='extrapolate', kind='cubic')(res)


def zero_crossings(sig):
    return np.where(np.diff(np.sign(sig)))[0]


def lvl_crossings(sig):
    thresholds = np.linspace(SIG_MIN, SIG_MAX, N_LEVELS + 2)[1:-1]
    return [(zero_crossings(sig - thresholds[i]), v)
            for i, v in enumerate(thresholds)]


def lvl_crossings_with_error(sig):
    crossings = lvl_crossings(sig)

    # calculate RMS quantization error
    sum_of_squares = 0
    for arr, thresh in crossings:
        for crossing in arr:
            sum_of_squares += np.square(sig[crossing] - thresh)

    num_crossings = np.sum([len(arr) for arr, _ in crossings])
    rms_error = np.sqrt(sum_of_squares / num_crossings)
    return crossings, rms_error


def uniform_sample_error(sig):
    margin = 2. / N_LEVELS
    sum_of_squares = 0
    for v in sig:
        sum_of_squares += np.square(v % margin)
    return np.sqrt(sum_of_squares)


def plot_level_crossings(crossings):
    for arr, thresh in crossings:
        for crossing in arr:
            plt.plot(crossing, thresh, 'ro')


def plot_sig(sig, color=''):
    res = np.arange(RESOLUTION)
    plt.plot(res, sig, color)


if __name__ == "__main__":
    x = np.linspace(0., PERIOD * 2, RESOLUTION)
    sig = f(x)
    xings, err = lvl_crossings_with_error(sig)

    plot_sig(sig)
    plot_level_crossings(xings)
    plt.title(err)
    plt.show()
