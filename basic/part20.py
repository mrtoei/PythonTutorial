# โปรแกรมหาผลรวม
userCount = int(input('Input Count : '))
print('Count : %d'%userCount)
count=0 #นับจำนวนรอบ
sumOgj = 0 #ตัวแปรเก็บค่าผลรวม
while(True):
    score = int(input('Input Number %d: '%(count+1)))
    sumOgj+=score
    count+=1
    if(count==userCount):
        break


print('Sum : %d'%sumOgj)