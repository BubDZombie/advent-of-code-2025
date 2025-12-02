import sys

class Dial:
    def __init__(self, size = 100, position = 50):
        self.size = size
        self.position = position

    def turn(self, instruction):
        direction = instruction[0]
        magnitude = int(instruction[1:])
        zeroes = 0
        if direction == 'L':
            adjustment = -1
        elif direction == 'R':
            adjustment = 1
        while magnitude > 0:
            self.position += adjustment
            if self.position == -1:
                self.position = 99
            elif self.position == 100:
                self.position = 0

            if self.position == 0:
                zeroes += 1

            magnitude -= 1
        return(zeroes)


if __name__ == '__main__':
    dial = Dial()
    zeroes = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            zeroes += dial.turn(line)
    print(f"Dial landed on 0 {zeroes} times.")
