from kornect.utilities import update_progress
from kornect.plot import sns_cntplt_array

import time

'''
for i in range(100):
    update_progress(i/100.0)
    time.sleep(0.01)
'''
# sns_cntplt_array([1,2,2,3,3,4],chart_title='Random',export=True)
from kornect.data_collection import browser

browser = browser("https://www.google.com",headless=False)
browser.setup()
browser.fetch_landing_page()
time.sleep(10)
browser.close()