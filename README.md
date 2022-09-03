# ABET ( Audio Basic Editing Tool) 
## What is ABET? 

The main goal about ABET is to wrapper some common editing scripts that are necessary in audio research. 
## Installation
- It's necessary to have installed `Python 3.x` and `pip3` in you machine
- First you need to install the dependencies, to do that you can just run:
    ```bash
        cd ABET
        pip install -r requirements.txt
    ```
- The you are ready to run ABET! 
## Basic Usage
- You can execute ABET just running:
    - if you are using linux:
        ```
        python3 abet.py
        ```
    - if you are using windows:

        ```
        py abet.py
        ```
- To see available options you can just type: 
    ```
    python3 abet.py --help
    ```

## Current Features:
- **Noise Reducer**
    - How to use:
        - You just need the add the flag `--noise_reduction="[list of input files]"` or `--noise_reduce_all=True`
## Future Features:
- Audio Difference Score - Based in spectogram 
    - The main idea is to have a value indicating the difference between two audios based in they MEL spectogram difference
- VISQOL and other metrics
- Audio Concat
- Self Duplicate Audio Extension
- Spectogram Generator
#### Authors: 
- **Vinicius Novaes** (vini2novaes@gmail.com / vcn2@cin.ufpe.br)