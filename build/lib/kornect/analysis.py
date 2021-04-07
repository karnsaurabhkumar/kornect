import time, sys
import pandas as pd


# update_progress() : Displays or updates a console progress bar
# Accepts a float between 0 and 1. Any int will be converted to a float.
# A value under 0 represents a 'halt'.
# A value at 1 or bigger represents 100%

def update_progress(progress):
    barLength = 10  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength * progress))
    text = "\rPercent Completion: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block), progress * 100,
                                                         status)
    sys.stdout.write(text)
    sys.stdout.flush()
    return 1


def append_df2csv(f_path, data):
    import os
    if not os.path.isfile(f_path):
        pd.DataFrame().to_csv(f_path)
    assert os.path.isfile(f_path), 'Please enter a valid file name'
    assert type(data) == pd.core.frame.DataFrame, 'Only dataframes are allowed'
    data.to_csv(f_path, mode='a', header=False, index=False)
    return 1

