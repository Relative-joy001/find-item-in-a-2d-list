def fill_in_numbers(board):

    height = len(board)
    width = len(board[0])

    for row in range(height):
        for items in range(width):
            if board[row][items] == "B":
                continue

            bombs = 0
            for row_item in [row - 1, row, row + 1]:
                for item_items in [items - 1, items, items + 1]:
                    if row_item == row and item_items == items:
                        continue
                    if 0 < row_item < height and 0 < item_items < width:
                        if board[row_item][item_items] == "B":
                            bombs += 1
                            board[row][items] = bombs

    return board
            



print(fill_in_numbers([[0, 0, 0, 0], [0, "B", 0, 0], [0, 0, 0, "B"], [0, 0, 0, 0]]))