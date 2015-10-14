import pullprices as pp
df1 = pp.stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache('FB','2011-01-01','2015-07-17')
df2 = df1.dropna(subset=['Open'])
print df2

