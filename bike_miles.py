# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
from datetime import datetime
import os
import pandas as pd
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np
import matplotlib.dates as mdates

# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(11, 4)})




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
'3-19-2020':12.6


 }

for key in miles:
   
    dt = datetime.strptime(key, '%m-%d-%Y')
    doy = datetime.timetuple(dt)[7]     
    m = miles[key]
    #print(doy,m)
    print(dt,m)


try:
    os.listdir('/usr')
    base_dir = '/data'
except:
    base_dir = 'C:/data'


# process_files = False
# src_dir = os.path.join(base_dir,'outages')

# fileList = os.listdir(src_dir)
# outFile = os.path.join(base_dir,'outages4.txt')


D = None
# D = pd.read_csv(outFile, header=0, index_col=['time'],parse_dates=True,names=['time', 'county', 'cwa', 'tracked', 'outages'])
# D['ratio'] = (D.outages/D.tracked) * 100
# D['log'] = np.log10(D.outages)

# F = D.replace([np.inf, -np.inf], 0)
# # Jul 20,2019 = 201
# # Sep 11,2019 = 254
# # Nov. 25, 2019 = 329
# # Nov 30, 2019 = 334 ... 334-338
# #E = F[(F.index.dayofyear > 329) & (F.index.dayofyear <334)]
# E = F[(F.index.dayofyear > 253) & (F.index.dayofyear < 257)]
# df_e = E.resample('H').sum()
# df_e_outages = df_e['outages']

# GRR = E[E.cwa == 'grr']
# df_grr = GRR.resample('H').sum()
# df_grr_outages = df_grr['outages']

# DTX = E[E.cwa == 'dtx']
# df_dtx = DTX.resample('H').sum()
# df_dtx_outages = df_dtx['outages']

# APX= E[E.cwa == 'apx']
# df_apx = APX.resample('H').sum()
# df_apx_outages = df_apx['outages']

# IWX= E[E.cwa == 'iwx']
# df_iwx = IWX.resample('H').sum()
# df_iwx_outages = df_iwx['outages']

# fig, ax = plt.subplots(nrows = 1, ncols = 1)
# ax.plot(df_dtx_outages,color='b',linewidth=1,label='DTX')
# ax.plot(df_grr_outages,color='r',linewidth=1.75,label='GRR')
# #ax.plot(df_apx_outages,color='g',label='APX')
# #ax.plot(df_iwx_outages,color='m',label='IWX')
# ax.plot(df_e_outages,color='black', linewidth=2.5,ls='--',label='ALL')
# ax.legend()
# plt.ylabel('Outages')
# myFmt = mdates.DateFormatter('%Y-%m-%d\n%H UTC')
# myFmt2 = mdates.DateFormatter('%H UTC')
# ax.xaxis.set_major_formatter(myFmt)
# ax.xaxis.grid(True, which='minor')
# ax.xaxis.set_minor_formatter(myFmt2)
# plt.title('Consumers Outages')

# image_dst_path = 'C:\data\outages-20190911.png'
# plt.savefig(image_dst_path,format='png')
# plt.show()
# plt.close()
