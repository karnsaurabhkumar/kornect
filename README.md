This library attempts to solve some of the most basic challenges with data science pipelines and analysis. Some of the most repeated functions have been extracted while some other useful tools have been added.

There are four different parts to the library that talks to specific needs while working with data.
1. Analysis
2. Pandas
3. Plot
4. Utils


### 1. Analysis

### 2. Pandas

### 3. Plot

### 4. Utils

**Update Progress:** This takes a float as an input and creates a beautiful progress bar and shows you the percentage. No added libraries just pure python implementation.
```
from kornect.utilities import update_progress
import time

for i in range(100):
    update_progress(i/100.0)
    time.sleep(0.01)

```


