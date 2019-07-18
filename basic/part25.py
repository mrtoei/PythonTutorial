# แสดงแม่สูตรคูณ
while(True):
    number=int(input('Input Number (press -1 to stop): '))
    if(number<=0):
        break
    for i in range(1,12+1):
        print("%d * %d = %d"%(number,i,(number*i)))
    print('-------------------------------')