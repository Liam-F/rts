import sys

def make_sure_path_exists(path):
    import errno
    import os
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise




def stock(symbol):
    """ 
    gets last traded price from google for given security
    """        
    import pandas.io.data as pd 
    
    df = pd.get_quote_yahoo(symbol)
    #print(df)
    
    cols = ['PE', 'change_pct', 'last', 'short_ratio', 'time']
    result = pd.DataFrame(df, columns=cols)
    return result.iloc[0]['last']
def options_pd(symbol,expirationdate):
    
def options(symbol,expirationdate,pathtoexportfile):
    import lxml.html
    import calendar
    #import os

    #################################
    try:
        print("pullprices: trying")

        #total = len(sys.argv)
        #cmdargs = str(sys.argv)
        #print ("The total numbers of args passed to the script: %d " % total)
        #print ("Args list: %s " % cmdargs)
        # Pharsing args one by one 
        #print ("Script name: %s" % str(sys.argv[0]))

        #import inspect
        from datetime import datetime            
    
        #root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\data"
        root = pathtoexportfile
        #print ("Root: %s" % root)
        print ("Symbol: %s" % str(symbol))
        print ("Expiration: %s" % str(expirationdate))
        
        s_symbol  = str(symbol)
        d_expiration  = str(expirationdate)
    
        dt      = datetime.strptime(d_expiration, '%Y-%m-%d')
        ym      = calendar.timegm(dt.utctimetuple())
        url     = 'http://finance.yahoo.com/q/op?s=%s&date=%s' % (s_symbol, ym,)
        doc     = lxml.html.parse(url)
        table   = doc.xpath('//table[@class="details-table quote-table Fz-m"]/tbody/tr')
        
        rows    = []        
        for tr in table:
            d = [td.text_content().strip().replace(',','') for td in tr.xpath('./td')]
            rows.append(d)
        
        import csv
        
        length = len(rows[0])
        
        import datetime
        i = datetime.datetime.now()
        
        #print ("Current date & time = %s" % i)
        #print ("Date and time in ISO format = %s" % i.isoformat() )
        
        dateString = i.strftime('%Y%m%d%H%M%S')
        
        make_sure_path_exists(root)
        
        output = root + "\Options " + s_symbol + ' ' + d_expiration + ' ' + dateString + '.csv'
        #output = "Options " + s_symbol + ' ' + d_expiration + '.csv'
        
        print ('Output File: ' + output)
        
        with open(output, 'w') as test_file:
            csv_writer = csv.writer(test_file, lineterminator = '\n')
            for y in range(length):
                csv_writer.writerow([x[y] for x in rows])
                
    #################################
    except Exception as e:
        print("pullprices: There was a problem with this one......................................................X")
        print("pullprices: ",str(e))
    else:
        print("pullprices: Success")
    finally:
        print("pullprices: Finally")
    #################################
if __name__=='__main__':
    options(sys.argv[1],sys.argv[2],sys.argv[3])