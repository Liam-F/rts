# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:36:43 2015

@author: jmalinchak
"""

# ##########
# Date setup
import datetime
today_date = datetime.date.today()

today_datetime = datetime.datetime.today()
print('today_date',today_date)

datedelta = datetime.timedelta(weeks=301)
longago_datetime = today_datetime - datedelta
longago_string = str(longago_datetime.date())
print('longago_string',longago_string)