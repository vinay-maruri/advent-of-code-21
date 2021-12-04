#invariant 1: all inputs have the same number of digits.
#invariant 2: we can compute both gamma and epsilon rates at the same time since they just rely on most/least common bit.
from numpy import loadtxt

#create two string variables to hold the binary string
gamma_bit_string = ''
epsilon_bit_string = ''
#these two variables will store the counts of the bits in each position of inputs
counter1 = 0
counter2 = 0

with open("input.txt", 'r') as file:
    inputs = [line.strip() for line in file]
#using invariant 1, we know that the inputs have same fixed number of digits. hence we have only finite number of positions to check.
length = len(inputs[0])

position = 0

#first, check the counts of each bit in each position
#then assign the most/least common bit to the binary strings
while position < length:
    for input in inputs:
        if input[position] == '1':
            counter1 += 1
        else:
            counter2 += 1
    if counter1 > counter2:
        gamma_bit_string += '1'
        epsilon_bit_string += '0'
    else:
        gamma_bit_string += '0'
        epsilon_bit_string += '1'
    counter1 = 0
    counter2 = 0
    position += 1

#convert the binary strings to decimal and compute the final result.
result = int(gamma_bit_string, base = 2) * int(epsilon_bit_string, base = 2)
print(result)
#answer for part 1 is 845186.