class Player:
    def createName(self,name):
        self.name = name
    def displayName(self):
        print("Hello %s"%self.name)

obj1 = Player()
obj2 = Player()
obj3 = Player()
obj1.createName("Arkkarachat")
obj2.createName("Siribout")
obj3.createName("Mrtoeii")
obj1.displayName()
obj2.displayName()
obj3.displayName()