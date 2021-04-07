This library attempts to solve some of the most basic challenges with data science pipelines and analysis. Some of the most repeated functions have been extracted while some other useful tools have been added.

There are four different parts to the library that talks to specific needs while working with data.
1. Analysis
2. Pandas
3. Plot
4. Utils


### 1. Analysis

### 2. Pandas
**Rename Columns:** Pass the pandas dataframe, list of columns to be changed and list of new names to get the renamed pandas dataframe
```
from kornect.pd import rename_pd
df = rename_pd(df,[col1,col2,col3],[new_col1,new_col2,new_col3])
```

### 3. Plot
**Count Plot:** This will plot the frequency of elements in a list
```
from kornect.plot import sns_cntplt_array
sns_cntplt_array([1,2,2,3,3,4],chart_title='Random chart',export=False) 
```
![Count Plot Chart](examples/kornect_plot.png "Count Plot Output")

### 4. Utilities

**Update Progress:** This takes a float as an input and creates a beautiful progress bar and shows you the percentage. No added libraries just pure python implementation.
```
from kornect.utilities import update_progress
import time

for i in range(100):
    update_progress(i/100.0)
    time.sleep(0.01)
```



