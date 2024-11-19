import create_2d_board
import fill_in_num


board = create_2d_board.create_board(4, 4)
create_2d_board.add_bombs(board, 4)
fill_in_num.fill_in_numbers(board)
print(board)