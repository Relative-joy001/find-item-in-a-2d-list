def find_bombs(board):
    bomb_list  = []

    for row in range(len(board)):
        for item in range(len(board[row])):
            if board[row][item] == "B":
                bomb_list.append([row, item])
    return bomb_list





board = [
    [ 0,  1, "B", 2 ],
    [ 1,  "B",  2, "B"],
    ["B", 1,  1,  1 ],
    [ 1,  "B",  "B",  0 ],
]
print(find_bombs(board))