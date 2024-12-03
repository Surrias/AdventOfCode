input = open("Day2\Input.txt")
data = []
for line in input:
    data.append([int(num) for num in line.split()])

#Check if a line is safe
def is_safe(p):
    return (all(1 <= p[i+1] - p[i] <= 3 for i in range(len(p) - 1)) or all(1 <= p[i] - p[i+1] <= 3 for i in range(len(p) - 1)))
safe_count = 0
for line in data:
    if is_safe(line):
        safe_count += 1
print(safe_count)

damp_count = 0
for line in data:
    if is_safe(line) or any(is_safe(line[:i] + line[i+1:]) for i in range(len(line))):
        damp_count += 1
print(damp_count)