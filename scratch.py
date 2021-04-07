from kornect.utilities import update_progress
import time

for i in range(100):
    update_progress(i/100.0)
    time.sleep(0.01)
