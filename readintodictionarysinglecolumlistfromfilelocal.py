import csv, sys
def Print(pathtofilelocal):
    #basepath, fname = os.path.split(pathtofilelocal)
    #print(basepath, fname)
    with open(pathtofilelocal, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            
def Dictionary(pathtofilelocal):
  d0={}
  #print("aaaaaaaa")
  singlecolumnlist = open(pathtofilelocal, 'r')
  for line in singlecolumnlist:
        ############################
        #k, v = line.split(',')
        ############################
        v = line
        v = v.strip()
        #  k, v = map(line.strip, line.split(','))
        
        d0[len(d0)] = v
  return d0
  
  
if __name__=='__main__':
    #my_dict
    my_dict=Dictionary(sys.argv[1])
    print(my_dict[sys.argv[2]])

