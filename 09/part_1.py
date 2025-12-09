import sys

def area(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

if __name__ == '__main__':
    coordinates = []
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            coordinates.append([int(coord) for coord in line.strip().split(',')])
    pairs = set()
    for a in coordinates:
        for b in coordinates:
            pair = (a[0], a[1], b[0], b[1])
            pairs.add(pair)

    print(max([area(*pair) for pair in pairs]))
