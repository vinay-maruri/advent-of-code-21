with open("input.txt", "r") as file:
    f = file.readlines()
file.close()
lst = [int(c) for c in f[0].split(",")]

#part 1: least amount of fuel to horizontally align.
#O(n^2) brute force using a dictionary where the keys are fuel costs and values are the elements being aligned around.
costs = {}
for elem in range(len(lst)):
    sublst = lst[:elem] + lst[elem+1:]
    key = sum([abs(item - lst[elem]) for item in sublst])
    costs[key] = lst[elem]
print(min(costs))
#part 2: each move costs 1 more unit of fuel than the last.
#solution: use triangular numbers as the cost.
costs = {}
for elem in range(len(lst)):
    fuel_costs = []
    for item in lst:
        diff = abs(elem - item)
        fuel_costs.append((diff*(diff+1))/2)
    costs[sum(fuel_costs)] = elem 
print(min(costs))