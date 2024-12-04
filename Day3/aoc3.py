import re

def main():
    with open(r"C:\Users\zoe.little\OneDrive - Broadstreet Properties Ltd\Documents\AoC24\Advent3.txt") as f:
        input = f.read()
    print(sum_multis(find_multi(strip_disabled(input))))

def strip_disabled(text) -> str:
    return re.sub("don\'t\(\)[\s\S]*?do\(\)", "", text)

def find_multi(text) -> list[str]:
    return re.findall("mul\(\d+,\d+\)", text)

def sum_multis(pairs):
    sum = 0
    for pair in pairs:
        set = re.findall("\d+", pair)
        sum += (int(set[0]) * int(set[1]))
    return sum
main()
