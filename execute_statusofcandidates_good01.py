# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:32:16 2015

@author: jmalinchak
"""

import config
# Parameters
showresults = 0
mystatusofcandidatesfolder = config.mystatusofcandidatesfolder

# ##########
# Date setup
import datetime
today_datetime = datetime.datetime.today()
today_datestringforcsv = today_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')
import time
millis = int(round(time.time() * 1000))
today_datestringforfilename = today_datetime.strftime('%Y-%m-%d %H.%M.%S ') + str(millis)
yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
twodaysago_date = datetime.date.fromordinal(yesterday_date.toordinal()-1)

def optiontype(optionsymbol):
    import mytools
    ot = mytools.get_from_optionsymbol().optiontype(optionsymbol)
    return ot

def strike(optionsymbol):
    import mytools
    rstrike = mytools.get_from_optionsymbol().strike(optionsymbol)
    return rstrike

def make_strikelegsstring(openshortopenlongoptsym):
    #make_strikelegsstring('SPY150717C00212500-SPY150717C00213500-SPY150717P00206000-SPY150717P00205000')
    import mytools
    #openshortopenlongoptsym = 'SPY150717C00212500-SPY150717C00213500-SPY150717P00206000-SPY150717P00205000'
    optionsymbol_list = openshortopenlongoptsym.split('-')
    print(optionsymbol_list)
    strikelegsstring = ''
    for optionsymbol in optionsymbol_list:
        #print strikeleg
        strikeleg = mytools.get_from_optionsymbol().strike(optionsymbol)
        strikelegsstring = strikelegsstring + str(strikeleg) +'-'
    if len(strikelegsstring ) > 0:
        strikelegsstring = strikelegsstring[:-1]
    return strikelegsstring

import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def path_base(path):
    head, tail = ntpath.split(path)
    return head or ntpath.basename(head)    
#def getdictitem(thedict,key):

import config
import os
import pandas as pd
#import datetime
import numpy as np

myselectedcandidatesfolder = config.myselectedcandidatesfolder #'C:\\Batches\\rts\\output\\condor\\selected'
print('myselectedcandidatesfolder: ' + myselectedcandidatesfolder)
#filepathnames_list = []
#for filename in os.listdir(myselectedcandidatesfolder):
#    if filename.endswith(".csv") and filename.startswith('selectedcandidate'): 
#        #print(filename)
#        filepathnames_list.append(filename)
#        continue
#    else:
#        continue
#print(myselectedcandidatesfolder)
filepathnames_list = []
for (dirpath, dirnames, filenames) in os.walk(myselectedcandidatesfolder):
    #print dirpath, dirnames, filenames
    #for dirname in dirnames:
    for filename in filenames:
        if filename.endswith('.csv'): 
            fullpath = os.sep.join([dirpath, filename])
            #print(os.sep.join([dirpath, filename]))
            date_in_filename = datetime.datetime.strptime(filename.split()[1],'%Y-%m-%d').date()
            #print date_in_filename,yesterday_date ,date_in_filename>=yesterday_date
            if date_in_filename >= twodaysago_date: #yesterday_date:
                print(fullpath)
                filepathnames_list.append(fullpath)

import pandas.io.data as pdata

import pullprices as pp
#print(df_optionpricescurrent)

dict_of_df_optionpricescurrent = {}
dict_of_df_stockpricecurrent = {}
dict_empty = {}
#pp.stock()
for filepathname in filepathnames_list:    
    filename = path_leaf(filepathname)
    #today_datetime = datetime.datetime.today()
    print('+++ +++++++++++++++++++++++++')
    print('+++ Doing ' + filepathname + '...')
    symbol = filename.split(' ')[2].upper().replace('.CSV','')
    expirationdate_string = filename.split(' ')[1]
    
    df_optionpricescurrent = dict_of_df_optionpricescurrent.get(symbol+'|'+expirationdate_string,dict_empty)
    if len(df_optionpricescurrent) == 0:        
        #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ got df_optionpricescurrent - -',symbol+'|'+expirationdate_string)
        df_optionpricescurrent = pp.options_to_dataframe(symbol,expirationdate_string,0)
        df_optionpricescurrent['optiontype'] = df_optionpricescurrent['optionsymbol'].to_frame(name='optionsymbol').applymap(optiontype)  
        dict_of_df_optionpricescurrent[symbol+'|'+expirationdate_string] = df_optionpricescurrent 
        dummy = 0
    else:
        #print('>>>>>>>>>>>>>>>>>>>> already have df_optionpricescurrent - -',symbol+'|'+expirationdate_string)
        dummy = 0
        #continue
        
    # If the size of dataframe still = 0, then there are no prices, you should break the loop
    if len(df_optionpricescurrent) == 0:
        print('No option prices found at all for ' + symbol + ' exp. ' + expirationdate_string)
        dummy = 0
    else:
        df_stockpricecurrent = dict_of_df_stockpricecurrent.get(symbol,dict_empty)
        if len(df_stockpricecurrent) == 0:
            #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ got df_stockpricecurrent here')
            df_stockpricecurrent = pdata.get_quote_yahoo(symbol)
            dict_of_df_stockpricecurrent[symbol] = df_stockpricecurrent
        else:
            dummy = 0
            #continue
            #if showresults == 1:
            #print('>>>>>>>>>>>>>>>>>>>> already have df_stockpricecurrent - '+symbol)
    
        stockpricelast = df_stockpricecurrent['last'].iloc[0]
        stockpricetime = df_stockpricecurrent['time'].iloc[0]
        
        #print('symbol: '+symbol)
        #if showresults == 1:
        #    print('stockpricelast',stockpricelast)
        #filepathname = os.path.join(myselectedcandidatesfolder,filename)
        #print(filepathname)
        df_00 = pd.read_csv(filepathname)
        df_00['captureopen'] = df_00.sbid - df_00.bask
        df_00['stattime'] = today_datestringforcsv #today_datetime.strftime('%Y-%m-%d %H:%M') 
        df_00['statsp'] = float(stockpricelast)
        df_00['statcloseshortask'] = float('Nan')
        df_00['statcloselongbid'] = float('Nan')
        df_00['openshortopenlongoptsym'] = df_00['openshortoptsym']+'-'+df_00['openlongoptsym']
        #print(df_optionpricescurrent[(df_optionpricescurrent.strike == '250.00') & (df_optionpricescurrent.optiontype =='P')])
        
        #df_00['statcloselongbid'] = df.groupby('word').apply(lambda x: x.sum())
        #print df['Line']
        
        for index, row in df_00.iterrows():
            
            #print(df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['osym'])].bid.iloc[0])
            #if showresults == 1:
                #print(row['openshortoptsym'],'askprice to close open short',df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openshortoptsym'])].ask.iloc[0])
                #print(row['openlongoptsym'],'bidprice to close open long',df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openlongoptsym'])].bid.iloc[0])
            
            #df_00.statcloseshortask[df_00.openshortoptsym==row['openshortoptsym']] = df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openshortoptsym'])].ask.iloc[0]
            #df_00.statcloselongbid[df_00.openlongoptsym==row['openlongoptsym']] = df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openlongoptsym'])].bid.iloc[0]
            
            ##################################################
            #how to set value of a cell in pandas dataframe...
            #df.set_value('side', 'top', value)
            #print('should be 1',np.where(df_00['openshortoptsym']=='SPY150724P00202500')[0][0])
            
            #df_00.set_value(np.where(df_00['openshortoptsym']==row['openshortoptsym'])[0][0], 'statcloseshortask', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openshortoptsym'])].ask.iloc[0])
            #df_00.set_value(np.where(df_00['openlongoptsym']==row['openlongoptsym'])[0][0], 'statcloselongbid', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openlongoptsym'])].bid.iloc[0])
    
            # This kind of works...
    #        df_00.set_value(np.where(df_00['openshortoptsym']==row['openshortoptsym'])[0][0], 'statcloseshortask', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openshortoptsym'])].ask.iloc[0])
    #        df_00.set_value(np.where(df_00['openlongoptsym']==row['openlongoptsym'])[0][0], 'statcloselongbid', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openlongoptsym'])].bid.iloc[0])
    
            #df_00.set_value(np.where(df_00['openshortoptsym']==row['openshortoptsym'])[0][0], 'statcloseshortask', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openshortoptsym'])].ask.iloc[0])
            #df_00.set_value(np.where(df_00['openlongoptsym']==row['openlongoptsym'])[0][0], 'statcloselongbid', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openlongoptsym'])].bid.iloc[0])
            if any(df_optionpricescurrent.optionsymbol == row['openshortoptsym']):
                df_00.set_value(index, 'statcloseshortask', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openshortoptsym'])].ask.iloc[0])
            if any(df_optionpricescurrent.optionsymbol == row['openlongoptsym']):
                df_00.set_value(index, 'statcloselongbid', df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == row['openlongoptsym'])].bid.iloc[0])
                
        df_00['captureclose'] = df_00.statcloselongbid - df_00.statcloseshortask
        df_00['netcapture'] = df_00.captureopen + df_00.captureclose
        
        #df_01_open = df_00.groupby(['currdate'])[['captureopen']].sum()
        #df_01_open.reset_index()
        
        #df_01 = df_00.groupby(['currdate'], as_index=False)['captureopen'].sum()['captureclose'].sum()['stattime'].min()
        #df.groupby("dummy").agg({"returns": [np.mean, np.sum]})
        
        #print df_00
        
        df_01a = df_00.groupby('currdate')['openshortopenlongoptsym'].apply(lambda x: "%s" % '-'.join(x))
        df_01b = df_00.groupby('currdate', as_index=True).agg({'stattime':[np.min],'captureopen': [np.sum],'captureclose': [np.sum],'stkp': [np.min],'statsp': [np.min]})
        
        df_01 = pd.concat([df_01a,df_01b], axis=1) # 
        #df_01_close = df_00.groupby(['currdate'], as_index=False)['captureclose'].sum()
        #df_01_stattime = df_00.groupby(['currdate'], as_index=False)['stattime'].min()
    
        #print(df_01_open)
        #print(df_01_close)
        #df_01 = df_01_open['currdate']
        #df_01 = pd.concat([df_01,df_01_stattime['stattime']], axis=1) # 
        #df_01 = pd.concat([df_01,df_01_open['captureopen']], axis=1)
        #df_01 = pd.concat([df_01,df_01_close['captureclose']], axis=1)
        
        #df_01 = pd.concat([df_01_open['currdate'], df_01], axis=1)
        #df_01 = df_01_open.join(df_01_close)    
        #print(df_optionpricescurrent)    
        
        df_01.reset_index()
        #print(df_01)
        
        #print(list(df_01.columns.values))
        
        df_ana_00 = df_01.rename(columns={'openshortopenlongoptsym': 'openshortopenlongoptsym', ('stkp', 'amin'): 'openstkp',('stattime', 'amin') : 'stattime',('captureopen', 'sum'): 'captureopen',('captureclose', 'sum'): 'captureclose',('statsp', 'amin') :'statstkp'})        
        df_ana_00['opendate'] = pd.to_datetime(df_ana_00.index)
        
            
        df_ana_00a = df_ana_00.groupby('openshortopenlongoptsym', as_index=True).agg({'opendate':[np.min]})
        #print df_ana_00a
        #df_ana_01 = df_ana_00.groupby("openshortopenlongoptsym").opendate.min()
        #df_ = pd.DataFrame(index=index, columns=columns)
        columns = ['opendate','openstkp','captureopen']
        df_ana_01= pd.DataFrame(index=df_ana_00a.index, columns=columns)
        for index_df_ana_00a,row_df_ana_00a in df_ana_00a.iterrows():
            openshortopenlongoptsym = index_df_ana_00a
            opendate = row_df_ana_00a[0]
            #print openshortopenlongoptsym,opendate
            df_ana_01.set_value(openshortopenlongoptsym,'opendate',opendate)
    
        #print(df_ana_00)
        #print '--------------------------------------------------------------'
        #print df_ana_01
        
        for index_df_ana_01,row_df_ana_01 in df_ana_01.iterrows():
            #df_initialopen = df_ana_00[(df_ana_00['openshortopenlongoptsym'] == index_df_ana_01)]
            openshortopenlongoptsym = index_df_ana_01
            opendate = pd.to_datetime(row_df_ana_01['opendate'])
            df_initialopen = df_ana_00[(df_ana_00['openshortopenlongoptsym'] == index_df_ana_01) & ( pd.to_datetime(df_ana_00['opendate']) == pd.to_datetime(row_df_ana_01['opendate']) )]
            #df_ana_01.set_value(openshortopenlongoptsym,'opendate',df_initialopen['opendate'])
            df_ana_01.set_value(openshortopenlongoptsym,'openstkp',df_initialopen['openstkp'])
            df_ana_01.set_value(openshortopenlongoptsym,'captureopen',df_initialopen['captureopen'])
            #
        #print df_ana_01['openstkp']
            #print df_initialopen
        
        #print(list(df_ana_01.columns.values))
        for index_01, row_01 in df_ana_01.iterrows():    
            openshortopenlongoptsym = index_01
            strikelegsstring = make_strikelegsstring(openshortopenlongoptsym)
            #print 'length of strikeleg items', len(strikelegsstring.split('-')) 
            if not len(strikelegsstring.split('-')) == 4:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('The four legs of condor were not established for ' + openshortopenlongoptsym)                
            else:
                opendate = row_01['opendate']
        #        print '----------------------'
        #        print openshortopenlongoptsym
        #        print '----------------------'
        
                df_selectedcandidates = df_ana_00[df_ana_00['openshortopenlongoptsym'] == openshortopenlongoptsym]
                #print df_selectedcandidates
                #print df_selectedcandidates
                
                columns = ['stattime','strikeleg1','strikeleg2','strikeleg3','strikeleg4','openstkp','statstkp','captureopen','captureclose','capturenet']
                index = df_selectedcandidates['opendate']
                df_statusofcandidates = pd.DataFrame(index=index, columns=columns)
                for index_02,row_02 in df_selectedcandidates.iterrows():
                    #print filename
                    #print strikelegsstring
                    df_iter = df_selectedcandidates[(df_selectedcandidates['opendate'] == row_02['opendate'])]    
                    df_statusofcandidates.set_value(row_02['opendate'],'strikeleg1',strikelegsstring.split('-')[0])
                    df_statusofcandidates.set_value(row_02['opendate'],'strikeleg2',strikelegsstring.split('-')[1])
                    df_statusofcandidates.set_value(row_02['opendate'],'strikeleg3',strikelegsstring.split('-')[2])
                    df_statusofcandidates.set_value(row_02['opendate'],'strikeleg4',strikelegsstring.split('-')[3])
                    df_statusofcandidates.set_value(row_02['opendate'],'openstkp',row_02['openstkp'])
                    df_statusofcandidates.set_value(row_02['opendate'],'captureopen',row_02['captureopen'])
                    df_statusofcandidates.set_value(row_02['opendate'],'stattime',str(row_02['stattime']).replace('  ',' '))
                    df_statusofcandidates.set_value(row_02['opendate'],'statstkp',row_02['statstkp'])
                    df_statusofcandidates.set_value(row_02['opendate'],'captureclose',row_02['captureclose'])
                    df_statusofcandidates.set_value(row_02['opendate'],'capturenet',round(float(row_02['captureopen'])+float(row_02['captureclose']),2))
                
                df_statusofcandidates_sorted = df_statusofcandidates.sort()
                #df_ana_01= pd.DataFrame(index=df_ana_00a.index, columns=columns)
        
                #print df_statusofcandidates
                #print 'opendate',opendate
                # ##############################
                # Print 
                print('opendate',opendate)
                opendate_datestringforfilename = opendate.strftime('%Y-%m-%d#%H.%M.%S.%f')
                #print 'opendate_datestringforfilename',opendate_datestringforfilename
                
                import mytools
                mygeneral = mytools.general()
                
                #strikelegsstring = make_strikelegsstring(openshortopenlongoptsym)
                filepath_to_statusofcandidates = os.path.join(mystatusofcandidatesfolder,symbol,'statusofcandidates ' + expirationdate_string + ' ' + symbol+'.csv')
                print('creating file/path:',filepath_to_statusofcandidates)
                mygeneral.make_sure_path_exists(path_base(filepath_to_statusofcandidates))
                #print '----------------------'
                #print filepath_to_statusofcandidates
                #print '----------------------'
                if os.path.isfile(filepath_to_statusofcandidates) != True:
                    df_statusofcandidates_sorted.to_csv(filepath_to_statusofcandidates,columns=('stattime','strikeleg1','strikeleg2','strikeleg3','strikeleg4','openstkp','statstkp','captureopen','captureclose','capturenet'))
                    
                elif len(df_ana_01) > 0:
                    #df_fromcsv = pd.read_csv(filepath_to_statusofcandidates, index_col=0)
                    existingcsvfile = open(filepath_to_statusofcandidates, 'a') # Open file as append mode
                    df_statusofcandidates_sorted.to_csv(existingcsvfile, header = False)
                    existingcsvfile.close()
                else:
                    print('nothing done, no data in df_ana_01.......................')
             ##############################
            
            
    #        for index_02, row_02 in df_statusofcandidates.iterrows():    
    #            #print 'statstkp',row_02['statstkp']
    #            #print row_02
    #            #df.set_value('C', 'x', 10)
    #            #a = index_02
    #            #print a
    ##            print '+++++++++++++++++++++'
    ##            print openshortopenlongoptsym
    ##            print '+++++++++++++++++++++'
    ##            ####################################
    #            #df_ana_01.set_value(openshortopenlongoptsym,'opentime',pd.to_datetime(index_02))
    #            
    #            df_ana_01.set_value(openshortopenlongoptsym,'openstkp',row_02['openstkp'])
    #            df_ana_01.set_value(openshortopenlongoptsym,'stattime',row_02['stattime'])
    #            df_ana_01.set_value(openshortopenlongoptsym,'captureopen',row_02['captureopen'])
    #            df_ana_01.set_value(openshortopenlongoptsym,'captureclose',row_02['captureclose'])
    #            df_ana_01.set_value(openshortopenlongoptsym,'statstkp',row_02['statstkp'])
    ##            ####################################
    
    
    
                
            #df_ana_02 = df_ana_01.rename(columns={('opendate', 'amin'): 'opendate', ('openstkp', ''): 'openstkp',('stattime', '') : 'stattime',('captureopen', ''): 'captureopen',('captureclose', ''): 'captureclose',('statsp', '') :'statstkp'})        
            #print df_ana_01
            #print(list(df_selectedcandidates.columns.values))
    
    
    
        #df_ana_02 = df_ana_01.rename(columns={('opendate', 'amin'): 'opendate'})        
        #print df_ana_02
    #    
        #for index_df_ana_01, row_df_ana_01 in df_ana_01.iterrows():    
        #    print index_df_ana_01,row_df_ana_01['openshortopenlongoptsym']
    
    
    #    # ##############################
    #    # Print 
    #    import mytools
    #    mygeneral = mytools.general()
    #    mygeneral.make_sure_path_exists(mystatusofcandidatesfolder)
    #    filepath_to_statusofcandidates = os.path.join(mystatusofcandidatesfolder,'statusofcandidates ' + expirationdate_string + ' ' + symbol+' ' + today_datestringforfilename + '.csv')
    #    if os.path.isfile(filepath_to_statusofcandidates) != True:
    #        df_ana_00.to_csv(filepath_to_statusofcandidates,columns=('openshortopenlongoptsym', 'openstkp','stattime','captureopen','captureclose','statstkp'))
    #        
    #    elif len(df_ana_00) > 0:
    #        #df_fromcsv = pd.read_csv(filepath_to_statusofcandidates, index_col=0)
    #        existingcsvfile = open(filepath_to_statusofcandidates, 'a') # Open file as append mode
    #        df_ana_00.to_csv(existingcsvfile, header = False)
    #        existingcsvfile.close()
