# การเพิ่มสมาชิก List ด้วย Loop
product=[]
while(True):
    stock = input('Product (press exit to stop): ')
    if(stock=='exit'):
        break
    product.append(stock)
print(product)