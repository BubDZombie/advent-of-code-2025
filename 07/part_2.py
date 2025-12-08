import copy
import sys

from board import Board

if __name__ == "__main__":
    board = Board(sys.argv[1])
    q = []
    q.append((board, 0, 0))
    paths = 0
    while len(q) > 0:
        board, starting_row, starting_col = q.pop(0)
        print(board)
        for row_num in range(starting_row, len(board.board)):
            for col_num in range(starting_col, len(board.board[0])):
                cell = board.board[row_num][col_num]
                if cell == 'S':
                    board.set(row_num + 1, col_num, '|')
                elif cell == '.' and board.get(row_num - 1, col_num) == '|':
                    board.set(row_num, col_num, '|')
                    if row_num == len(board.board) - 1:
                        paths += 1
                elif cell == '^' and board.get(row_num - 1, col_num) == '|':
                    lefty = copy.deepcopy(board)
                    lefty.set(row_num, col_num - 1, '|')
                    q.insert(0, (lefty, row_num + 1, col_num - 1))
                    righty = copy.deepcopy(board)
                    righty.set(row_num, col_num + 1, '|')
                    q.insert(0, (righty, row_num + 1, col_num + 1))
                    print(f"row {row_num + 1}, queue length {len(q)}")
    print(paths)
