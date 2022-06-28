#str.format string literals example

name = "Birhane"
age = 24
weight = 55.88

print("Welcome {}, You Are {} and your Weight is {}".format(name,age,weight))

print("Welcome {0}, You Are {1} and your Weight is {2}".format(name,age,weight))

print("Welcome {0}, You Are {1} and your Weight is {2:.1f}".format(name,age,weight))

print("Welcome {0:20}, You Are {1:d} and your Weight is {2:.1f}".format(name,age,weight))

''' 20 character field---> 7 character
 name (Birhane) the other 13 character is *  '''
print("Welcome {:*^20s}".format(name)) 

for i in range(2 ,13):
    print("{:<6d} {:<6d} {:<6d}".format(i, i*i, i*i*i))