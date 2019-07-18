# ตัวแปรประเภท List

# List
listNumber = [2.5,4.00,3.89,2.00] #เก็บข้อมูลชนิดเดียวกัน
listCustom = ["Mrtoeii","Arkkarachat",27,161,85]

# การเข้าถึง List
print(listNumber[0])
print(listCustom[1])

listObj = [listNumber,listCustom]
print(listObj)
print(listObj[0])
print(listNumber[:4])
print(listNumber[2:])
print(listNumber[1:3])