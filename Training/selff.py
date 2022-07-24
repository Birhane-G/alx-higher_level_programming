class sum:
####__init__ authomaticaly store when an object created
    def __init__(self, first, second):
        self.num1 = first
        self.num2 = second
    def desplay(self):
        print("sum: ", self.num1 + self.num2 )

add = sum(10,10)
addnext = sum(20,20)

add.desplay()
addnext.desplay()
add.desplay()
######################################
#with out self keyword
class sub:
    def sub(self, first, second):
        self.num1 = first
        self.num2 = second
    def desplay(self):
        print("sub: ", self.num1 - self.num2)

subst = sub()
subst.sub(10,5)
subst.desplay()
############################