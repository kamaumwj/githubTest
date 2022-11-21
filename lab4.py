from pathlib import Path
import random

path = Path()

for file in path.glob("*"):
    print(file)


lst = [1,2,3,4,5,6]
random.shuffle(lst)
print(lst)

resp = [ i for i in range(10,151) if i % 35 ==0]
print(resp)

