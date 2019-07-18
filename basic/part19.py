# การใช้งานสั่ง While

# โปรแกรมหาผลรวมของตัวเลข 4 จำนวน
count = 0 #นับจำนวนรอบ
sumOgj = 0 #ตัวแปรเก็บค่าผลรวม
while(count>=0):
    score = int(input('Input Number %d: '%(count+1)))
    sumOgj+=score
    count+=1
    if(count==4):
        break
print('Sum : %d'%sumOgj)