##This is All about data hiding, encapuslation and Abstraction
class robot:
    def __init__(self, name=None):
        self.name = name
    def hello(self):
        if self.name:
            print("Hello my Name is {}".format(self.name))
        else:
            print("hello I have\'t name")
    def set_name(self, S_name):
        self.name = S_name
    def get_name(self):
        print("Name = {}".format(self.name))

machion = robot()
machion.hello()
S_machion = robot('Mama')
S_machion.hello()

S_machion.set_name("Birhane")
S_machion.get_name()
####Other Example about encapuslation#####
##Two underscore is Private
##one Protected
#none is public 
class number:
    def __init__(self, number):
        self.__num = number
    def get_num(self):
        return print("the number is: {}".format(self.__num))
    def set_num(self, number):
        self.__num = number

i = number(10)
i.get_num()
i.set_num(11)
i.get_num()