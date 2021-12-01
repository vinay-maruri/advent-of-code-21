from numpy import loadtxt
file_name = "day-1-input.txt"

#problem setup: https://adventofcode.com/2021/day/1
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