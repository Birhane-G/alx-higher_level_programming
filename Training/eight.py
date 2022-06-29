from turtle import end_fill


for i in range(97, 123):
    chara = chr(i)
    print(f"{chara}", end="")

print("\n")

for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    print(chr(i), end="")

print("\n")

for i in range(98):
    val = hex(i)
    print(f"{i} = {val} ")

print("\n")

for i in range(100):
    print(f"{i:02d}",  end="\n" if i == 99 else ", ")

print("\n")

for i in range(100):
    for j in range(i +1, 10):
        print(f"{i}{j}", end="\n" if i == 8 and j == 9 else ", ")