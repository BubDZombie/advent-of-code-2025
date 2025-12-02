import sys

def valid(num):
    num = str(num)
    if len(num) % 2 != 0:
        return True
    half = int(len(num) / 2)
    if num[:half] == num[half:]:
        return False
    return True

if __name__ == '__main__':
    invalid_sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            for _range in line.strip().split(','):
                start, end = _range.split('-')
                for i in range(int(start), int(end) + 1):
                    if not valid(i):
                        invalid_sum += i
    print(invalid_sum)
