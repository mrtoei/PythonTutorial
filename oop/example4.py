# Multiple Parent Class
class Dad:
    gender = "male"
    def SayHello(self):
        print('Hello')
    def SayHi(self,fname,lname):
        print("Hi %s %s"%(fname,lname))
class Mom:
    sex="female"
    def SayNo(self):
        print('OK')

class child(Dad,Mom):
    def SayObj(self):
        print("Start")
c1 = child()
c1.SayNo()
c1.SayHello()
c1.SayHi("Arkkrachat",'Mrtoeii ')

