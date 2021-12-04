filename = "input.txt"

#simple approach: just scan all of the inputs for horizontal and depth movers.
#problem statement: https://adventofcode.com/2021/day/2
#really just boils down to tracking the results based on inputs.

horizontal = 0
depth = 0
with open(filename, 'r') as file:
    lines = [line.strip() for line in file]
for line in lines:
    if line[0] == 'f':
        horizontal += int(line[-1])
    elif line[0] == 'u':
        depth -= int(line[-1])
    else:
        depth += int(line[-1])
print(horizontal * depth)
#part 1 result is 1714680

aim = 0
horizontal = 0
depth = 0

for line in lines:
    if line[0] == 'f':
        horizontal += int(line[-1])
        depth += (aim * int(line[-1]))
    elif line[0] == 'u':
        aim -= int(line[-1])
    else:
        aim += int(line[-1])
print(horizontal * depth)

#part 2 result is 1963088820