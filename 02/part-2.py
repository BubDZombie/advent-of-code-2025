import sys

def valid(num):
    num = str(num)
    for pattern_len in range(1, int(len(num) / 2) + 1):
        pattern = num[:pattern_len]
        mismatch = False
        for i in range(0, len(num), pattern_len):
            if num[i:i+pattern_len] != pattern:
                mismatch = True
                break
        if not mismatch:
            return False
    return True

if __name__ == '__main__':
    print(f"1: {valid(1)}")
    print(f"11: {valid(11)}")
    print(f"111: {valid(111)}")
    print(f"1111: {valid(1111)}")
    print(f"123123: {valid(123123)}")
    print(f"121212: {valid(121212)}")
    print(f"1234: {valid(1234)}")
    print(f"824824823: {valid(824824823)}")

    invalid_sum = 0
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            for _range in line.strip().split(','):
                start, end = _range.split('-')
                for i in range(int(start), int(end) + 1):
                    if not valid(i):
                        invalid_sum += i
    print(invalid_sum)
