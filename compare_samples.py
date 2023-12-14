from scipy.io import wavfile
import level_crossing as lc

TIME = 1.
FILENAMES = ["audio/metronome.wav", "audio/sheep.wav", "audio/sine.wav"]

for fname in FILENAMES:
    # read TIME seconds of audio samples from file
    sample_rate, data = wavfile.read(fname)
    size = int(sample_rate * TIME)
    sampled_sig = lc.normalize(data[0:size])

    # interpolate signal to get a cotinuous representation
    sig = lc.interp_audio_seg(sampled_sig, size)

    # generate level-crossing samples
    xings, err = lc.lvl_crossings_with_error(sig)
    # err = lc.uniform_sample_error(sig)
    num_samples = sum([len(a) for a, _ in xings])

    # print(f"{fname} | {err:.6}")
    print(f"{fname} | {num_samples}")
