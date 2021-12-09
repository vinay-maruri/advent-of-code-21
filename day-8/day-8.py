with open("input.txt", 'r') as file:
    f = file.readlines()
file.close()
lines = [f[z] for z in range(len(f))]
lines = [c.strip().split(" | ") for c in lines]

part_1 = [sublist[1].split(" ") for sublist in lines]

cnt = 0
for lst in part_1:
    for item in lst:
        if len(item) in [2, 4, 3, 7]:
            cnt += 1
print(cnt)
#part 1 answer is 369.