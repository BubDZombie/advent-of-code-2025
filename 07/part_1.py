import sys

print(sys.path)
from board import Board

if __name__ == "__main__":
    board = Board(sys.argv[1])
    for row_num, row in enumerate(board.board):
        for col_num, col in enumerate(row):
            if board.get(row_num, col_num) == 'S':
                board.set(row_num + 1, col_num, '|')
            elif board.get(row_num, col_num) == '^' \
                 and board.get(row_num - 1, col_num) == '|':
                board.set(row_num, col_num - 1, '|')
                board.set(row_num, col_num + 1, '|')
            elif board.get(row_num - 1, col_num) == '|' \
                 and board.get(row_num, col_num) == '.':
                board.set(row_num, col_num, '|')
    print(board)
    count = 0
    for row_num, row in enumerate(board.board):
        for col_num, col in enumerate(row):
            if board.get(row_num, col_num) == '^' \
               and board.get(row_num - 1, col_num) == '|':
                count += 1
    print(count)
