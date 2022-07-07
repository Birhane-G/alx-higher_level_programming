from collections import deque

name = deque(['birhane', 'biniyam', 'gemechis', 'fitsum', 'bekabl'])
name.append("betty")
name.append("mahi")

name.popleft()

print(name)