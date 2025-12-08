import copy
import sys

from board import Board

if __name__ == "__main__":
    board = Board(sys.argv[1])
    i = 0
    cell = board.get(0, i)
    while cell != 'S':
        i += 1
        cell = board.get(0, i)
    q = [(1, i)]
    counts = {}
    counts[(1, i)] = 1
    paths = 0
    target_row = len(board.board) - 1
    while len(q) > 0:
        row, col = q.pop(0)
        next_cell = board.get(row + 1, col)
        moves = []
        if next_cell == '.':
            moves.append((row + 1, col))
        elif next_cell == '^':
            moves.append((row + 1, col - 1))
            moves.append((row + 1, col + 1))
        else:
            paths += counts[(row, col)]
        for next_coords in moves:
            if next_coords not in counts:
                counts[next_coords] = 0
            counts[next_coords] += counts[(row, col)]
            if next_coords not in q:
                q.append(next_coords)
                row, col = next_coords
                board.set(row, col, '|')
                #print(board)
    print(paths)
