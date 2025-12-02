import sys

class Dial:
    def __init__(self, size = 100, position = 50):
        self.size = size
        self.position = position

    def turn(self, instruction):
        direction = instruction[0]
        magnitude = int(instruction[1:])
        if direction == 'L':
            self.position -= magnitude
            self.position = self.position % self.size
        elif direction == 'R':
            self.position += magnitude
            self.position = self.position % self.size


if __name__ == '__main__':
    dial = Dial()
    zeroes = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            dial.turn(line)
            if dial.position == 0:
                zeroes += 1
    print(f"Dial landed on 0 {zeroes} times.")
