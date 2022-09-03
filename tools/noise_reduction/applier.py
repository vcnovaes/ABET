from email.mime import audio
from fileinput import filename
from genericpath import isdir
from utils.colors import UNDERLINE, WARNING, ENDC
from os import mkdir
from tools.noise_reduction.noise_reduction import remove_noise
from utils.utils import is_wav


def apply_over_dir():
    pass


def apply_over_filelist(filelist, input_dir=''):
    output_dir = './clean_audios/'
    result = []
    if (isdir(output_dir) == False):
        mkdir(output_dir)
    for audiofile in filelist:
        if not is_wav(audiofile):
            message = f'{WARNING}WARNING{ENDC}: NOT APPLYING NOISE REDUCTION IN AUDIO {UNDERLINE}' + \
                audiofile + f'{ENDC}!'
            print(message)
            continue
        result.append(remove_noise(
            input_dir + audiofile, output_dir + 'cls_' + audiofile[2::]))
    return result
