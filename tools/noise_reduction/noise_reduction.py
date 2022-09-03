from scipy.io import wavfile
import noisereduce as nr
from soundfile import read
import noisereduce as nr


def stationary_noise_remover(input_audio, output_name):
    data, rate = read(input_audio)
    clear_audio = nr.reduce_noise(
        y=data,
        sr=rate,
    )
    wavfile.write(
        output_name,
        rate,
        clear_audio
    )
    return output_name


def remove_noise(input_file, output_file, stationary=True):
    if stationary:
        return stationary_noise_remover(input_file, output_file)
