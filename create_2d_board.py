import random

def create_board(height, width):
    board = []

    for item in range(height):
        item_row = []

        for item in range(width):
            item_row.append(0)
        board.append(item_row)
    return board


# add item randomly to board

def add_bombs(board, number_of_bombs):
    height = len(board)
    width = len(board[0])

    bombs = 0

    while bombs < number_of_bombs:

        row = random.randint(0, height - 1)
        col = random.randint(0, width - 1)
        if board[row][col] != "B":
            board[row][col] = "B"
            bombs += 1 


board = create_board(3, 3)
add_bombs(board, 3) 
print(board)       