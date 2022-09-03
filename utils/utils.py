from fileinput import filename
from os import listdir, mkdir
from soundfile import read
from librosa import load, power_to_db
from librosa.feature import melspectrogram
from librosa.display import specshow
from matplotlib.pyplot import savefig
from numpy import max
from pydub import AudioSegment
from pylab import axis, axes
from os.path import isdir


def get_audios(directory: str):

    return [
        read(file)
        for file in listdir(directory)
    ]


def convert_mp3_to_wav(input_file: str, output_file: str):
    sound = AudioSegment.from_mp3(input_file)
    sound.export(output_file, format='wav')


def generate_MEL_spectogram(audio_file: str, output_name: str):
    audio_data, sr = load(audio_file, sr=None, mono=True)
    melspec = melspectrogram(y=audio_data, sr=sr)
    axis('off')
    axes([0., 0., 1., 1.], frameon=False,
         xticks=[], yticks=[])  # remove white edges
    S = melspectrogram(y=audio_data, sr=sr)
    specshow(power_to_db(S, ref=max))
    savefig(output_name)
    pass


def get_file_extension(filename: str): return filename[len(filename) - 3:]
def is_wav(filename: str): return get_file_extension(filename) == 'wav'


def convert_dataset_to_wav(input_dir: str):
    output_path = './wav_input_files/'
    if (input_dir[-1] != '/'):
        input_dir += '/'
    if (not isdir(output_path)):
        mkdir(output_path)
    for file in listdir(input_dir):
        convert_mp3_to_wav(
            input_file=input_dir+file,
            output_file=output_path + file[:-3] + '.wav'
        )
