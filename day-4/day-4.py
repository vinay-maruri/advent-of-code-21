import numpy as np

with open("input.txt", "r") as file:
    f = file.readlines()
#the bingo numbers that get "called out" in the game are contained in the first line.
#invariant 1: how many numbers get called out at a time doesn't matter for this problem.
bingo_callouts = [int(x) for x in f[0].split(",")]
#part 1 wants the first winning board.
boards = []
#lines 2 to the end contain the individual bingo boards, that are each 5x5.
row = 2
while row < len(f):
    board_block = f[row:row+5]
    for i in range(5):
        boards.append([int(x) for x in board_block[i].rstrip("\n").split()])
    row += 6
#reshaping the boards in a 5x5 shape with the correct number of boards (using number of sublists in array and number of entries in each sublist)
boards = np.array(boards)
boards = boards.reshape(boards.shape[0] // boards.shape[1], 5, 5)

#the check_boards function checks each row and column to see if there is a winner
#input: mask is the boolean mask for each board
#output: the winning row/column number or -1 if no winner has been found.
def check_boards(mask, finished):
    for board_number in range(len(mask)):
        if board_number in finished:
            continue
        for row in range(5):
            for col in range(5):
                check_rows = np.prod(mask[board_number, :, col])
                check_cols = np.prod(mask[board_number, row, :])
                if check_rows:
                    return board_number, col 
                if check_cols:
                    return board_number, row 
    return -1,-1


#this function iterates over each number that gets called out, finds each place where the number exists on a board
#marks those indices as called out in the board's boolean mask, checks the marked boards for a winner
#and then computes necessary information to get the answer. 
# invariant 2: at least 5 numbers have to be called out for a winner, meaning we can reduce the amount of work slightly by only checking winners
# from number 5 and on. 
#create a boolean mask for each board that tracks which board entries have been called out
#last=True forces function to find all winning boards as intended by part 2, otherwise it will only find the first.
def find_winners(boards, bingo_callouts, last=False):
    boolean_mask = np.zeros_like(boards, dtype=bool)
    winner = False
    last_number = 0
    winning_board = None
    numbers_called = 0
    winning_boards = set()
    for number in bingo_callouts:
        numbers_called += 1
        if winner:
            break
        indices = np.argwhere(boards == number)
        for index in indices:
            boolean_mask[index[0], index[1], index[2]] = True
            if numbers_called >= 4:
                board_number, row_col = check_boards(boolean_mask, winning_boards)
                if board_number >= 0 and row_col >= 0:
                    last_number = number
                    winning_board = board_number
                    if not last:
                        winner = True
                        break 
                    else:
                       winning_boards.add(board_number)
                       if len(winning_boards) == boards.shape[0]:
                            winner = True
                            break
    return boolean_mask, winning_board, last_number

mask, winner, last_num = find_winners(boards, bingo_callouts)
#problem wants the sum of the unmarked numbers in the answer.
opp_mask = np.ones_like(mask).astype(bool) ^ mask
unmarked = np.sum(boards[winner, :, :] * opp_mask[winner, :, :])

print(last_num * unmarked)
#part 1 answer is 82440.

#part 2 wants the last winning board.#
mask, winner, last_num = find_winners(boards, bingo_callouts, last = True)
opp_mask = np.ones_like(mask).astype(bool) ^ mask
unmarked = np.sum(boards[winner, :, :] * opp_mask[winner, :, :])

print(last_num * unmarked)
#part 2 answer is 20774.