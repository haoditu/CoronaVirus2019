import time
import json
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def catch_daily():
    """Get National Cumulative Confirmed and Dead Data"""
    
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)
    data = json.loads(requests.get(url=url).json()['data'])
    data.sort(key=lambda x:x['date'])
    
    date_list = list() # Date
    confirm_list = list() # Confirm
    suspect_list = list() # Suspect
    dead_list = list() # Dead
    cured_list = list() # Cured 
    for item in data:
        month, day = item['date'].split('/')
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        cured_list.append(int(item['heal']))
    
    return date_list, confirm_list, suspect_list, dead_list, cured_list



def plot_daily():
    """Plot National Cumulative Data"""
    
    date_list, confirm_list, suspect_list, dead_list, cured_list = catch_daily() # Get data
    
    plt.figure('2019-nCoV_StatsChart', facecolor='#f4f4f4', figsize=(10, 8))
    plt.title('2019-nCoV_StatsTrend', fontsize=20)
    
    plt.plot(date_list, confirm_list, label='Confirmed')
    plt.plot(date_list, suspect_list, label='Suspection')
    plt.plot(date_list, dead_list, label='Death')
    plt.plot(date_list, cured_list, label='Cured')
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # Formatting time axis
    plt.gcf().autofmt_xdate() # Optimize label（auto-Italicize）
    plt.grid(linestyle=':') # Display grid
    plt.legend(loc='best') # Display legend
    plt.savefig('2019-nCoV_StatsTrend.png') # Save image
    plt.show()

if __name__ == '__main__':
    plot_daily()