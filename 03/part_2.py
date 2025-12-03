import sys

def find_joltage(rating):
    window_left = 0
    num_trailing = 11
    output = ''
    while len(output) < 12:
        window = rating[window_left:len(rating) - num_trailing]
        big = max([digit for digit in window])
        big_index = window.index(big)
        window_left += big_index + 1
        output += big
        num_trailing -= 1
    return int(output)

if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            joltage = find_joltage(line.strip())
            print(f"{line.strip()} {joltage}")
            sum += joltage
    print(sum)
