import re

with open("Day3\Input.txt",'r') as f:
    input = f.read()

multi = re.findall("mul\(\d+,\d+\)", input)

sum = 0
for pair in multi:
    set = re.findall("\d+", pair)
    sum += (int(set[0]) * int(set[1]))
print(sum)