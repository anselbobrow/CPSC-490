import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import level_crossing as lc


def interp_sig(crossings):
    x = []
    y = []
    for arr, thresh in crossings:
        for crossing in arr:
            if (crossing not in x):
                x.append(crossing)
                y.append(thresh)
    return interp1d(x, y, fill_value='extrapolate', kind='cubic')


if __name__ == "__main__":
    x = np.linspace(0., lc.PERIOD * 2, lc.RESOLUTION)
    sig = lc.f(x)
    xings = lc.lvl_crossings(sig)

    samples = np.arange(lc.RESOLUTION)
    interp_y = interp_sig(xings)(samples)
    # plot original signal and interpolated signal
    plt.plot(samples, sig, 'r', samples, interp_y, '-')
    lc.plot_level_crossings(xings)
    plt.show()
