with open("input.txt", 'r') as file:
    f = file.readlines()
file.close()

lfish = [int(c) for c in f[0].split(",")]

print(len(lfish))
#80 days in total.
#part 1 solution: brute force [this is a terribad algorithm..n! runtime]
days_elapsed = 0
new_fish_cnt = 0
while days_elapsed < 80:
    for elem in range(len(lfish)):
        if lfish[elem] == 0:
            lfish[elem] = 6
            new_fish_cnt += 1
        else:
            lfish[elem] = lfish[elem] - 1
    if new_fish_cnt > 0:
        for i in range(new_fish_cnt):
            lfish.append(8)
        new_fish_cnt = 0
    days_elapsed += 1

#print(len(lfish))

#part 2 solution: using dictionaries which is much faster.

start = lfish                                  
new = {}                                                              
for i in start:
    new[i] = new[i]+1 if i in new else 1
                                    
start = new
for day in range(256):
    new = {}
    for fish in start:
        timer = fish-1
        if timer == -1:
            new[8] = start[fish]
            new[6] = start[fish]+new[6] if 6 in new else start[fish]
        else:
            new[timer] = start[fish]+new[timer] if timer in new else start[fish]

    start = new

print(sum(start.values()))


