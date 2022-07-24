class persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def desplay(self):
        print("My name is {0} i am {1} Years old.".format(self.name, self.age), end=" ")

class worker:
    def __init__(self, name, age, work):
        persons.__init__(self, name, age)
        self.work = work
    def desplay(self):
        persons.desplay(self)
        print("I am currently working on {}".format(self.work))

birhane = worker('Birhane', 23, 'web developement')
bbb = persons('Yeshi', 47)

members = [birhane, bbb]
for member in members:
    member.desplay()