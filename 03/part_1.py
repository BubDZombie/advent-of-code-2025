import sys

def find_joltage(rating):
    big = max([digit for digit in rating])
    big_index = rating.index(big)
    window_left = big_index + 1
    window_right = len(rating)
    if window_left == len(rating):
        window_left = 0
        window_right = big_index
    small = max([digit for digit in rating[window_left:window_right]])
    small_index = rating[window_left:window_right].index(small) + window_left
    if big_index < small_index:
        return int(f"{big}{small}")
    else:
        return int(f"{small}{big}")

if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            joltage = find_joltage(line.strip())
            print(f"{line.strip()} {joltage}")
            sum += joltage
    print(sum)
