
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""

# ##########
# Parameters
symbol = 'QQQ'
mycomparesym = '^VIX'
expirationdate_string = '2015-07-10'
daysbackmid = 0
myspreadindollars = 1
mycumprobthreshold = 80 #Percent in whole number 80 = 80%
mycumprob_to_sell_price_lowrange = 0
mycumprob_to_sell_price_highrange = 95
numberofweekstolookback = 300
RollingNumberOfPeriods = 120
showresults = 0



ThreshholdAbove = 0.0001 #Percent change above
ThreshholdBelow = -0.0001  #Percent change below
myoutputfolder = 'C:\\Batches\\MyPython\\active\\output'
#myoutputfolder = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\New Folder\\output'



# ##########
# Date setup
import datetime

today_datetime = datetime.datetime.today()
use_date = datetime.date.today()


while True :
    today_date = use_date
    expire_date = datetime.datetime.strptime(expirationdate_string,'%Y-%m-%d').date()
    if today_date != expire_date:
        break
    use_date = today_date - datetime.timedelta(hours=24)

print use_date