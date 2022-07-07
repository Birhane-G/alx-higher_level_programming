
from re import A
from tkinter.font import names


mat = [[1,2,3], [0,9,8], [5,6,7]]

arrange = [[row[i] for row in mat] for i in range(3)]

print(mat)
print(arrange)

innn = []
for i in range(3):
    innn.append([row[i] for row in mat])
print(innn)

x = list(zip(*mat))
print(x)

#sets
x = set("i want to learn python programming language and i want to be dpython developer")
y = set("my name is Birhane Gebrial")
print(x)
print(y)
print(x - y) #print letter in only x 
print(x | y)  #print letter in only x or only y or both
print(x & y)  #print letters in both x and y
print(x ^ y)   #print letters not in both x and y

# membership testing 
names = "birhane", "biniyam", "bekable"
print("birhane" in names) #True 
