from audioop import reverse


name = {"Birhane":1, "Biniyam":2, "Gemechis":3, "mahi":[1,2,3,4], "samri":[[1,2,3],[4,5,6]]}

print(name)
print(name["Biniyam"])
print(list(name))
print(sorted(name))
print(name.get("mahi")[3])
print(name.get("samri")[-1])
name2 = dict([("bekabil", 3), ("fitsum", 4)])
print(name2)

no = {i: i*2 for i in (2,4,9)}
print(no)

#retriving keys and value at the same time
#using items()
for k,v in name.items():
    print(k, v)
#using enumerate()
for k,v in enumerate(["bbbb","cccc","ddddd"]):
    print(k,v)

#two or more listed value
work = {"developer":1,"tester":2,"QA":3}

for n,w in zip(name ,work):
    print("my name is {} and i am {}".format(n,w))

num = [1,2,3,4,5]
num.reverse()

print(num)