with open("input.txt", 'r') as file:
    f = file.readlines()
file.close()
lines = [f[z] for z in range(len(f))]
lines = [c.strip().split(" | ") for c in lines]

part_1 = [sublist[1].split(" ") for sublist in lines]

#simply count the number of strings of length 2, 3, 4, or 7.
cnt = 0
idxs = [2, 4, 3, 7]
for lst in part_1:
    for item in lst:
        if len(item) in idxs:
            cnt += 1
print(cnt)
#part 1 answer is 369.

#part 2

#first split each line into the inputs and outputs
#then pattern match using the following invariants:
#1, 4, 7, 8 can be identified by string length alone.
#9 is a length 6 pattern that has 4&7 in it
#3 is a length 5 pattern that contains 1 in it
#2 is a length 5 pattern that 9 doesn't contain
#5 is a length 5 pattern that can be identified by the disjoint set of 1 and 4.
#6 is a length 6 pattern that contains both 5 and 9
#0 is a length 6 pattern that contains 1&7 but not 4
#this seems natural to use sets here.

sum_of_numbers = 0
for line in f:
    if f == '':
        continue
    inputs, outputs = line.strip().split('|')
    patterns, signals = inputs.split(), outputs.split()
    #dictionary that maps all 10 numbers to patterns [as a set]
    mapping = {}
    #first loop maps known patterns by length
    for pattern in patterns:
        l = len(pattern)
        p = set(pattern)
        #case 1, length 2 pattern which is 1
        if l == 2:
            mapping[1] = p
        #case 2, length 3 pattern which is 7
        elif l == 3:
            mapping[7] = p
        #case 3, length 4 pattern which is 4
        elif l == 4:
            mapping[4] = p
        #case 4, length 7 pattern which is 8
        elif l == 7:
            mapping[8] = p 
    #second loop uses results of first loop to build out rest of mappings.
    #complication: need to use only patterns for 1, 4, 7, and 8 to guarantee a solution
    #and avoid a key error.
    for pattern in patterns:
        l = len(pattern)
        p = set(pattern)    
        #length 6 cases
        if l == 6:
            if(mapping[4] | mapping[7]).issubset(p):
                mapping[9] = p 
            elif(mapping[1] | mapping[7]).issubset(p) and not mapping[4].issubset(p):
                mapping[0] = p 
            else:
                mapping[6] = p
        #length 5 cases
        elif l == 5: 
            if(mapping[4] - mapping[1]).issubset(p):
                mapping[5] = p 
            elif mapping[1].issubset(p):
                mapping[3] = p
            else:
                mapping[2] = p
    decoder = {"".join(sorted(list(v))):k for k,v in mapping.items()}
    sum_of_numbers += int("".join([str(decoder["".join(sorted(v))]) for v in signals]))  
print(sum_of_numbers)       
#part 2 answer: 1031553.