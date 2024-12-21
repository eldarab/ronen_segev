import pandas as pd
from Demos.EvtSubscribe_pull import events
from scipy.io import wavfile
import os


def read_wav(exp_num,file_path):
    fs, y = wavfile.read("file_path")
    return y
def read_file(experiment_number,file_name):
    events = pd.read_csv(f"f./results/{experiment_number}.{file_name}", names=["marker", "time"], skiprows=2)

    return events


def bs_only():
    for experiment_number in os.listdir("./results"):
        for file_name in os.listdir(f"./results/{experiment_number}.bs"):
            events = read_file(file_name)



# לפרק לפוקנציות
# התאוששות - ביקורת
# התאוששות מחקר
# גרף של התנועה של הקצב לב לאורך זמן? אחד של ביקורת ואחד של מחקר

def main():

    


if __name__ == '__main__':
    main()