with open("AoC_4_input.txt") as f:
    lines = f.readlines()

called_numbers = lines[0].split(",")
called_numbers = [int(x) for x in called_numbers]
boards = lines[1:]
boards = [x[:-1] for x in boards]
new_boards = []
for idx in range(len(boards)):
    if idx % 6 == 0:
        new_boards.append([])
        new_boards[idx//6].append(boards[idx+1])
        new_boards[idx//6].append(boards[idx+2])
        new_boards[idx//6].append(boards[idx+3])
        new_boards[idx//6].append(boards[idx+4])
        new_boards[idx//6].append(boards[idx+5])
boards = new_boards
for idx in range(len(boards)):
    for jdx in range(5):
        boards[idx][jdx] = boards[idx][jdx].split()
        boards[idx][jdx] = [int(x) for x in boards[idx][jdx]]

for board in boards:    
    print(board)

def is_winning_board(boards):
    winning_board_column = find_empty_columns(boards)
    winning_board_row = find_empty_rows(boards)
    if winning_board_column != None:
        return winning_board_column
    elif winning_board_row != None:
        return winning_board_row
    return None

def remove_bingo_input(boards, bingo_input):
    for board in boards:
        for row in range(5):
            for column in range(5):
                if board[row][column] == bingo_input:
                    board[row][column] = None

def find_empty_rows(boards):
    for board in boards:
        for row in board:
            for el in row:
                winning = True
                if el != None:
                    winning = False 
                    break
            if winning == True:
                return board
    return None

def find_empty_columns(boards):
    for board in boards: 
        for c in range(5): 
            winning = True
            for r in range(5): 
                if board[r][c] != None:
                    winning = False
                    break
            if winning == True:
                return board
    return None

def sum_remaining_nums(winning_board):
    summed_bingo = 0
    for row in winning_board:
        for col in row:
            if col != None: 
                summed_bingo += col
    return summed_bingo

def remove_winners(boards): 
    for board in boards: 
        for c in range(5): 
            winning = True
            for r in range(5): 
                if board[r][c] != None:
                    winning = False
                    break
            if winning == True:
                boards.remove(board)
                print("removed!_ column")
    for board in boards: 
        for row in board:
            for el in row:
                winning = True
                if el != None:
                    winning = False 
                    break
            if winning == True:
                boards.remove(board)
                print("removed!_ rw")

for bingo_input in called_numbers:
    #   remove the puzzle inputs from the puzzle boards in order
    remove_bingo_input(boards, bingo_input)
    #once there is a winning board
    if is_winning_board(boards) != None:
        winning_board = is_winning_board(boards)
        #sum the remaining numbers
        winning_sum = sum_remaining_nums(winning_board)
        #multiply that by the last input
        print(winning_sum * bingo_input)
        print(winning_sum)
        remove_winners(boards)