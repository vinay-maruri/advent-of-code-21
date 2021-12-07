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

#part 2: we want to find the number that has the most common bits by position, as well as the number that has the least common bit in position
#naturally this seems like a problem for recursion.
#base case: if there's only 1 element left in the list, stop.

#The destroy function removes elements from list in-place based on a marked list of elements to remove.
#inputs: lst is a list of binary strings, marked is a list of booleans representing elements designated for removal.
#returns: a list of binary strings with destroyed elements removed.
def destroy(lst, marked):
    lst = [lst[idx] for idx in range(len(lst)) if not marked[idx]]
    return lst

#The find_common_bit function finds the most/least common bit in a given position from a list of binary strings
#inputs: least is a boolean indicating if we want to find most or least common, lst is the list of binary strings, pos is the position in string we're inspecting
#returns: the most/least common bit in a given position.
def find_common_bit(least, lst, pos):
    count0 = 0
    count1 = 0
    for item in lst:
        if item[pos] == '1':
            count1 += 1
        else:
            count0 += 1
    value = '1'
    if count0 == count1:
        least = not least
        value = str(int(least))
    elif least:
        value = '0' if count1 > count0 else '1'
    else:
        value = '0' if count1 < count0 else '1'
    print(f'zero count is {count0} and one count is {count1}. Element kept is {value} because least is {least}.')
    return value

#The search function recurses through a list of binary strings to return the oxygen generator rating or co2 scrubber rating
#inputs: pos is the position in string we're inspecting, lst is the list of binary strings, and least is an boolean directing whether this is most or least common.
#returns: the rating after recursion completes.
def search(pos, lst, least):
    if len(lst) == 1:
        return lst
    marked_to_destroy = []
    common_bit = find_common_bit(least, lst, pos)
    for item in lst:
        if item[pos] != common_bit:
            marked_to_destroy.append(True)
        else:
            marked_to_destroy.append(False)
    new_lst = destroy(lst, marked_to_destroy)
    return search(pos+1, new_lst, least)

co2_rating = search(0, inputs, True)
oxygen_rating = search(0, inputs, False)
print(int(co2_rating[0], base=2) * int(oxygen_rating[0], base=2))
#part 2 result is 4636702