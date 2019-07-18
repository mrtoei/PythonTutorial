# โปรแกรมหาผลรวม Loop ต่อเนื่อง

sumOgj = 0 #ตัวแปรเก็บค่าผลรวม
while(True):
    score = int(input('Input Number (Input < 0 is stop): '))
    sumOgj+=score
    if(score<0):
        break
print('Sum : %d'%sumOgj)