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

