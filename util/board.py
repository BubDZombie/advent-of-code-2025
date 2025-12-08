class Board():
    def __init__(self, input_path):
        self.board = []
        with open(input_path) as file_handle:
            for line in file_handle:
                l = []
                for char in line.strip():
                    l.append(char)
                self.board.append(l)

    def __str__(self):
        output = ''
        for line in self.board:
            output += f"{''.join(line)}\n"
        return(output)

    def get(self, row, col):
        if row < 0 or col < 0:
            return None
        try:
            return self.board[row][col]
        except:
            return None

    def set(self, row, col, char):
        if row < 0 or col < 0:
            return False
        try:
            self.board[row][col] = char
            return True
        except Exception as e:
            print(e)
            return False

if __name__ == '__main__':
    board = Board('input-test.txt')
    assert board.get(0, 7) == 'S'
    assert board.get(0, 0) == '.'
    assert board.get(100, 100) is None
    assert board.get(-1, -1) is None
    board.set(6, 7, '*')
    assert board.get(6, 7) == '*'
    board.set(-1, -1, '#')
    for row in board.board:
        for cell in row:
            assert cell != '#'
