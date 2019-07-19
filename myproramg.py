def showMenu():
    menu=['สูตรคูณ','หาค่า Min และ Max']
    count=1
    for i in range(len(menu)):
        print("{0}.->{1}".format(count,menu[i]))
        count+=1
def multiplication():
    while(True):
        num1 = int(input("สูตรคูณแม่ (press 0 to exit menu):"))
        if(num1<=0):
            showMenu()
        num2 = int(input("จำนวนคูณ (press 0 to exit menu):"))
        if(num2<=0):
            showMenu()
        if(num1!=0 and num2!=0):
            for i in range(1,num2+1):
                print('%d * %d = %d'%(num1,i,(num1*i)))
            print('.....................................')
while(True):
    showMenu()
    inputMenu = int(input('Input menu (press 0 to exit): '))
    if(inputMenu<=0):
        break
    elif(inputMenu==1):
        multiplication()
        
        

