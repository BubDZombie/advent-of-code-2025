import sys

def neighbors(rolls, row, col):
    neighbor_list = []
    for r in [row, row - 1, row + 1]:
        for c in [col, col - 1, col + 1]:
            if r != row or c != col:
                neighbor_list.append(rolls[r][c])
    return neighbor_list

if __name__ == "__main__":
    rolls = []
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            row = [' ']
            for char in line.strip():
                row.append(char)
            row.append(' ')
            rolls.append(row)
    width = len(rolls[0])
    rolls.insert(0, [' '] * width)
    rolls.append([' '] * width)

    count = 0
    removed = True
    while removed:
        to_remove = []
        removed = False
        for row_num, row in enumerate(rolls):
            for col_num, cell in enumerate(row):
                if cell == '@':
                    neighbor_rolls = len([neighbor for neighbor in neighbors(rolls, row_num, col_num) if neighbor == '@'])
                    if neighbor_rolls < 4:
                        print(f"{row_num}, {col_num}")
                        to_remove.append([row_num, col_num])
                        removed = True

        for row, col in to_remove:
            rolls[row][col] = ' '
            count += 1
    print(count)
