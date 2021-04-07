from kornect.utilities import update_progress
import time, math

for i in range(0,100,1):
    update_progress(i/100.0)
    time.sleep(0.01)
