# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from datetime import datetime
import os
import pandas as pd
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt
#import seaborn as sns
#import numpy as np
#import matplotlib.dates as mdates

import matplotlib.gridspec as gridspec

fig2 = plt.figure(constrained_layout=False)
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig2)

f2_ax2 = fig2.add_subplot(spec2[1, 0])
f2_ax1 = fig2.add_subplot(spec2[0, 0],sharex=f2_ax2)



# Updated: 9/12/2019 2:01:29 AM GMT
test_file = 'C:/data/outages/MIoutages201907201810.html'
miles = {'1-12-2020':9.6,
'1-23-2020':4.9,
'1-31-2020':12.3,
'2-1-2020':5.0,
'2-3-2020':12.7,
'2-6-2020':12.8,
'2-9-2020':10.3,
'2-15-2020':5.7,
'2-16-2020':5.7,
'2-22-2020':10.0,
'3-15-2020':6.3,
'3-16-2020':9.7,
'3-17-2020':8.3,
'3-19-2020':12.6,
'3-21-2020':12.2,
'3-25-2020':11.6,
'4-2-2020':7.0,
'4-3-2020':5.3,
'4-5-2020':7.1,
'4-8-2020':10.5,
'4-11-2020':13.8,

 }

bike_array = []

for key in miles:
    dt = datetime.strptime(key, '%m-%d-%Y')
    doy = datetime.timetuple(dt)[7]     
    days_left = 366 - doy
    m = miles[key]   
    #print(doy,m)
    print(dt,m)

    this = (dt,doy,days_left,m)
    bike_array.append(this)


try:
    os.listdir('/usr')
    base_dir = '/data'
except:
    base_dir = 'C:/data'

df = None
df = pd.DataFrame(bike_array,columns=['date','day of year', 'days left', 'miles'])
df.set_index('date',inplace=True)



#fig,ax = plt.plot()
ts = df['miles']
ts= ts.cumsum()
f2_ax1.plot(ts)
df['miles_left'] = 1000 - ts
df['mpd_left'] = df['miles_left']/df['days left']
dl = df['mpd_left']
#ts.plot()
f2_ax2.plot(dl)



