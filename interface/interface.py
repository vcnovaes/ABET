from ast import literal_eval
from email.policy import default
from fileinput import filename
from locale import T_FMT
from os import listdir
import click

import tools.noise_reduction.applier as t_nr_app
from utils.colors import ENDC, BOLD, HEADER, UNDERLINE, YELLOWBG
from utils.colors import print_result


@click.command()
@click.option('--noise_reduction', default=[], help='Apply noise reduction')
@click.option('--noise_reduction_all', default=False, help='Apply noise reduction in all input directory')
@click.option('--input_directory', default='./input_audios', help='The directory audio input directory')
def options(noise_reduction, noise_reduction_all, input_directory):
    print(
        f'~~~ {HEADER}Welcome to ABET {ENDC}[ {BOLD}Audio Basic Editing Tool {ENDC}] ~~~')
    if (noise_reduction):
        print(f'{YELLOWBG}Applying Noise Reduction{ENDC}')
        input_value = literal_eval(noise_reduction)
        if input_value != []:
            result = t_nr_app.apply_over_filelist(input_value)
            print_result("NOISE REDUCED OUTPUT ", result)
        else:
            t_nr_app.apply_over_dir()
    if (noise_reduction_all):
        print(
            f'Applying {YELLOWBG}{BOLD}{UNDERLINE}Noise Reduction{ENDC}{ENDC} in {BOLD}ALL FILES{ENDC}{ENDC}')
        if input_directory[-1] != '/':
            input_directory += '/'
        result = t_nr_app.apply_over_filelist(
            listdir(input_directory), input_directory)
