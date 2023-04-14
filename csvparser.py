from globalvar import *
# def csvparse():
#     count = -2
#     with open('user.csv') as f:
#         for line in f:
#             semicoloncount = 0

#             count+=1
#             if(count == -1):
#                 continue
#             else:
#                 for i in range (len (line)-1):
#                     if(line[i] != ';'):
#                         if(semicoloncount == 0):
#                             listuser[count]+= line[i]
#                         elif(semicoloncount == 1):
#                             listpassword[count]+= line[i]
#                         elif(semicoloncount == 2):
#                             listrole[count]+= line[i]
#                     if(line[i] == ';'):
#                         semicoloncount+=1
def splitmanual(line):
    count = 0
    for i in range(len(line)):
        if(line[i] == ';'):
            count+=1
    arr = ['' for i in range (count+1)]
    temp = ''
    count = 0
    for i in range (len (line)):
        if(line[i] == ';'):
            arr[count] = temp
            count+=1
            temp = ''
        else:
            temp+=line[i]
    arr[count] = temp
    return arr


def csvparse():
    with open('user.csv') as f:
        jml = -1
        for line in f:
            if(jml==-1):
                jml+=1

            arr = splitmanual(line)
            listuser[jml] = arr[0]
            listpassword[jml] = arr[1]
            listrole[jml] = stripmanual(arr[2])
            jml+=1
        
def stripmanual(line):
    temp = ''
    for i in range (len (line)):
        if(line[i] != '\n'):
            temp+=line[i]
    return temp