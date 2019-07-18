# การสร้างฟังก์ชั่น (Function)

# การประกาศ Function
# def showMessagse():
#     print('Arkkarachat Siribout'+' Mrtoeii')

# def showNumber():
#     for i in range(1,13):
#         print ("%d * %d = %d"%(2,i,(i*2)))
# def showInput(str):
#     print(str)

# การเรียกใช้งาน
# showMessagse()
# showNumber()
# showInput("Mrtoeii")
# showInput("I love Python")

# รูปแแบ 1 ไม่มีการส่งค่า
def showMessagse(istr):
    print(istr)
showMessagse("Mrtoeii")

# รูปแแบบ 2 รับค่าเข้าไปทำงาน
def showString(str):
    print(str)
showString('Arkkrachat')
showString('Java')

# รูปแแบบ 3 รับและคืนค่า
def mininum(num1,num2):
    minvalue = 0
    if(num1>num2):
        minvalue=num2
    elif(num1<num2):
        minvalue=num1
    else:
        minvalue=num1
    return minvalue
minArr = mininum(100,50)
minArr = mininum(10,10)
print("min: %d"%minArr)

# รูปแแบบ 4 รับค่าไม่จำกัด
def summation(v1,v2,v3):
    return v1+v2+v3
def summation2(*var):
    sumvalue = 0  
    for i in range(len(var)):
        sumvalue+=var[i]
    return sumvalue
result = summation2(10,20,30,60,90)
print("Result : ",result)