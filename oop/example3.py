# SubClass และ Super Class
class ParentClass:
    name="Circle"
    size=400
    r=20
    def SayHello(self):
        print('Hello')
    def SayHi(self,fname,lname):
        print("Hi %s %s"%(fname,lname))
    def HIV(self):
        print("HIV")

class childClass(ParentClass):
    def SayObj(self):
        print("Start")


c1 = childClass()
c1.SayHello()
c1.SayHi('Arkkarachat','Siribout')
c1.SayObj()
c1.HIV()
print(c1.name)
