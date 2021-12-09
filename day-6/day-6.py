with open("input.txt", 'r') as file:
    f = file.readlines()
file.close()

#create the initial list of laternfish.
lfish = [int(c) for c in f[0].split(",")]


#modular solution now that I got the split solution.
#idea: this solution merely tracks fish as they shift between timer bins using a dictionary
#that way the data structure doesn't expand exponentially to an unreasonable size as it would
#with a list.
#inputs: fish_lst is the initial list of lanternfish, days is the number of days to simulate
#output: returns a dictionary representing the amount of fish in each timer bin.
def modular_solution(fish_lst, days):
    init = fish_lst                                 
    new = {}                                                              
    for i in init:
        new[i] = new[i]+1 if i in new else 1                                   
    counts = new
    for _ in range(days):
        new = {}
        for fish in counts:
            timer = fish-1
            if timer == -1:
                new[8] = counts[fish]
                new[6] = counts[fish]+new[6] if 6 in new else counts[fish]
            else:
                new[timer] = counts[fish]+new[timer] if timer in new else counts[fish]
        counts = new
    return counts
#part 1 solution
part_1 = modular_solution(lfish, 80)
#part 2 solution
part_2 = modular_solution(lfish, 256) 
print(sum(part_1.values()))
print(sum(part_2.values()))


