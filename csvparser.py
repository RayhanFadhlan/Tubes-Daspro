from globalvar import *
count = -2
with open('user.csv') as f:
    for line in f:
        semicoloncount = 0

        count+=1
        if(count == -1):
            continue
        else:
            for i in range (len (line)-1):
                if(line[i] != ';'):
                    if(semicoloncount == 0):
                        listuser[count]+= line[i]
                    elif(semicoloncount == 1):
                        listpassword[count]+= line[i]
                    elif(semicoloncount == 2):
                        listrole[count]+= line[i]
                if(line[i] == ';'):
                    semicoloncount+=1
        
