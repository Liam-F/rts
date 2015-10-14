import pandas
import pandas.io.data
import datetime
import urllib3
import csv

YAHOO_TODAY="http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sd1ohgl1vl1"

def get_quote_today(symbol):
    http = urllib3.PoolManager()
    r = http.request('GET', YAHOO_TODAY % symbol)
    #print(str(r.data))
#    response = r.data # urllib2.urlopen(YAHOO_TODAY % symbol)
    str(r.data).split
    reader = csv.reader(str(r.data), delimiter=",", quotechar='"')
   #print(reader)

    for row in reader:
        print(row)
        if row[0] == symbol:
            return row[0]
        

## main ##
symbol = "TSLA"

#history = pandas.io.data.DataReader(symbol, "yahoo", start="2014/1/1")
#print(history.tail(3))
#
#today = datetime.date.today()
#df = pandas.DataFrame(index=pandas.DatetimeIndex(start=today, end=today, freq="D"),
#                      columns=["Open", "High", "Low", "Close", "Volume", "Adj Close"],
#                      dtype=float)

rx = get_quote_today(symbol)
print(rx)
#df.ix[0] = map(float, row[2:])
#
#history = history.append(df)
#
#print("today is %s" % today)
#print(history.tail(2))