from numpy import loadtxt
file_name = "day-1-input.txt"

#problem setup: https://adventofcode.com/2021/day/1

#part 1:
#essentially, count the number of times that the next number in a sequence is larger than the previous number.

#load in inputs; numpy loadtxt converts a text file into an ndarray
lines = loadtxt(file_name, delimiter = '\r\n')

#use 2 pointers for comparison, one fast, one slow.
pointer_fast = 1
pointer_slow = 0

#store the result in counter variable.
counter = 0

#this works because true evaluates to 1 in python, false evaluates to zero.
while pointer_fast < lines.size:
    counter += lines[pointer_fast] > lines[pointer_slow]
    pointer_fast += 1
    pointer_slow += 1

print(counter)
#result for my input is 1184.

#runtime: O(n) because the code requires linear time to scan all inputs twice. Once to read in the text file input, and once to pass through the inputs to compute result.
#space: O(1) because the code requires constant space to run, only using a static amount of memory and no additional data structures.

#part 2: compare sums of a three-measurement sliding window.

#use 4 pointers to track each element in windows.
pointer_back = 0
pointer_middle1 = 1
pointer_middle2 = 2
pointer_front = 3
#store result in counter2.
counter2 = 0
while pointer_front < lines.size:
    counter2 += (lines[pointer_back] + lines[pointer_middle1] + lines[pointer_middle2]) < (lines[pointer_middle1] + lines[pointer_middle2] + lines[pointer_front])
    pointer_back += 1
    pointer_middle1 += 1
    pointer_middle2 += 1 
    pointer_front += 1

print(counter2)
#result for my input is 1158
#runtime: O(n) same explanation as part 1.
#space: O(1) same explanation as part 1.