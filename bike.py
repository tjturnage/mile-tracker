# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:29:51 2020

@author: thomas.turnage
"""


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
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
# import matplotlib.gridspec as gridspec


fig, axes = plt.subplots(nrows=2, ncols=1, sharex='col', sharey=False,
                               gridspec_kw={'height_ratios': [1, 1]},
                               figsize=(10, 4))
fig.set_tight_layout({'rect': [0, 0, 1, 0.95], 'pad': 1.5, 'h_pad': 1.5})
plt.setp(axes, title='1000 mile biking goal for 2020')
plt.setp(axes[0], title='Accumulated Miles - Actual (Blue) and Average Required (Orange)')
plt.setp(axes[1], title='Miles Per Day Required for Rest of Year - Actual (Blue) and Average (Orange) ')
fig.suptitle('1000 Miles Biking Goal For 2020', size=18)




test_file = 'C:/data/outages/MIoutages201907201810.html'
miles = {'1-1-2020':0.0,
'1-12-2020':9.6,
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
'4-14-2020':6.3,
'4-18-2020':6.3,
'4-19-2020':9.7,
'4-22-2020':16.7,
'4-24-2020':16.5,
'4-25-2020':13.9,
'4-26-2020':12.5,
'4-28-2020':15.6,
'5-1-2020':16.3,
'5-2-2020':10.5,
'5-5-2020':9.6,
'5-6-2020':17.1,
'5-8-2020':10.9,
'5-9-2020':11.1,
'5-12-2020':10.4,
'5-13-2020':11.8,
'5-16-2020':11.1,
'5-20-2020':8.9,
'5-21-2020':12.7,
'5-24-2020':13.1,
'5-26-2020':10.8,
 }

bike_array = []

for key in miles:
    dt = datetime.strptime(key, '%m-%d-%Y')
    doy = datetime.timetuple(dt)[7]     
    #slope = 1000/366
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
df = pd.DataFrame(bike_array,columns=['date', 'day of year', 'days left', 'miles'])
df.set_index('date',inplace=True)
df['slope'] = 1000/366
df['pace'] = df['day of year'] * df['slope']

#fig,ax = plt.plot()
tm = df['miles']
total_miles = tm.cumsum()
df['miles_left'] = 1000 - total_miles
df['mpd_left'] = df['miles_left']/df['days left']
print(df['mpd_left'])
axes[0].plot(total_miles)
axes[0].plot(df['pace'])
axes[0].yaxis.set_major_locator(ticker.MultipleLocator(50))
axes[0].grid(True)


axes[1].plot(df['mpd_left'])
axes[1].plot(df['slope'])
axes[1].yaxis.set_major_locator(ticker.MultipleLocator(0.1))
#set ticks every week
axes[1].xaxis.set_major_locator(mdates.WeekdayLocator())
#set major ticks format
axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.grid(True)

