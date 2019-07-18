# การใช้งานคำสั่ง And Or

# ใช้ And
# email = input('Input Your Email: ')
# if('@' in email and '.com' in email):
#     print('ป้อน Email ถูกต้อง')
# else:
#     print('Input Email New!!')

# ใช้ Or
status = input('Input Your Status: ')
if(status=="Admin" or status=='User'):
    print('Status : ' +status)
else:
    print('Input New!!')