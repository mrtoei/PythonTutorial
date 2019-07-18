# รู้จักกับทัพเพิล Tuple
# - สามารเก็บข้อมูลในปริมาณมาก
# - ใช้สำหรับเก็บข้อมูลที่มีค่าคงที่และไม่มีการเปลี่ยนแปลง
# - ไม่สามารถเพิ่ม หรือ ลบ Tuple ได้โดยตรง
# - ใช้สัญสักษณ์ () ในการประกาศตัวแปร
# - สมาชิกภายใน Tuple จะคั่นด้วย , (comma)
tup1 = (12,34.56)
tup2 = ('abc','xyz')
tup3 = (19,12.5,'Python',"Hello")
tup4 = (tup1,tup2,tup3)
tup5 = tup1+tup2
print(tup3)
print(tup3[2])
print(tup4)
print(tup5)

print(len(tup4))
print(tup4*2)
print('ab' in tup2)
print('abc' in tup2)
