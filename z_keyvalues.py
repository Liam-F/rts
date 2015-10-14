import csv, sys
def Print(pathtofile):
    #basepath, fname = os.path.split(pathtofile)
    #print(basepath, fname)
    with open(pathtofile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            
def Dictionary(pathtofile):
  symbols_dict={}
  #print("aaaaaaaa")
  list_of_symbols = open(pathtofile, 'r')
  for line in list_of_symbols:
        ############################
        k, v = line.split(',')
        ############################
        v = v.strip()
        #  k, v = map(line.strip, line.split(','))
        
        symbols_dict[k] = v
  return symbols_dict
  
  
if __name__=='__main__':
    #my_dict
    my_dict=Dictionary(sys.argv[1])
    print(my_dict[sys.argv[2]])

