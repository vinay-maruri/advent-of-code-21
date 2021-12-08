#part 1: asks for number of points in a grid where vertical/horizontal lines overlap twice or more.
#part 2: adds on diagonal lines.

#split the inputs, first on the arrow, then on commas.
with open("input.txt", "r") as file:
     f = file.readlines()
file.close()
lines = [c for c in [line.strip().split('->') for line in f]]
lines = [[c[0].split(','), c[1].split(',')] for c in lines]

#count points tracks points on the grid and counts the number of times they've been visited by a distinct line
#using a dictionary, where the key is a visited point, and the value is the number of times it's been visited.
#input: lines is a list of line endpoints, diagonal determines whether or not to include diagonal lines.
#returns: number of points that have been visited twice or more.
def count_points(lines, diagonal = False):
    point_dict = {}
    for line in lines:
        point_0 = (int(line[0][0]), int(line[0][1]))
        point_1 = (int(line[1][0]), int(line[1][1]))
        #vertical line case
        if point_0[0] == point_1[0]:
            step = 1 if point_1[1] > point_0[1] else -1
            for j in range(point_0[1], point_1[1]+step, step):
                if (point_0[0], j) in point_dict:
                    point_dict[(point_0[0], j)] += 1
                else:
                    point_dict[(point_0[0], j)] = 1
        #horizontal line case
        elif point_0[1] == point_1[1]:
            step = 1 if point_1[0] > point_0[0] else -1
            for j in range(point_0[0], point_1[0]+step, step):
                if (j, point_0[1]) in point_dict:
                    point_dict[(j, point_0[1])] += 1
                else:
                    point_dict[(j, point_0[1])] = 1
        #diagonal line case
        elif diagonal:
            x_move = 1 if point_0[0] < point_1[0] else -1
            y_move = 1 if point_0[1] < point_1[1] else -1
            x_dist = abs(point_0[0] - point_1[0])
            for i in range(x_dist+1):
                x = point_0[0] + i * x_move
                y = point_0[1] + i * y_move
                if (x,y) in point_dict:
                    point_dict[(x,y)] += 1
                else:
                    point_dict[(x,y)] = 1
    values = list(point_dict.values())
    return len([i for i in values if i >= 2])

print(count_points(lines, False))
#part 1 answer is 6397.
print(count_points(lines, True))
#part 2 answer is 22335.