import sys

def area(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def contains(x1, y1, x2, y2, x3, y3):
    '''Return True if the rectangle formed by x1,y1 and x2,y2 contains x3,y3.'''
    if x3 > min(x1, x2) and x3 < max(x1, x2) \
       and y3 > min(y1, y2) and y3 < max(y1, y2):
        return True
    return False

def cuts(rect_x1, rect_y1, rect_x2, rect_y2, line_x1, line_y1, line_x2, line_y2):
    '''Return true if line segment cuts rectangle.'''
    if (min(line_x1, line_x2) >= max(rect_x1, rect_x2)) \
       or (max(line_x1, line_x2) <= min(rect_x1, rect_x2)) \
       or (min(line_y1, line_y2) >= max(rect_y1, rect_y2)) \
       or (max(line_y1, line_y2) <= min(rect_y1, rect_y2)):
        return False
    return True

def rectangle_segments(x1, y1, x2, y2):
    '''Return a list of line segments that make up the given rectangle.'''
    segments = []
    segments.append((x1, y1, x2, y1))
    segments.append((x2, y1, x2, y2))
    segments.append((x2, y2, x1, y2))
    segments.append((x1, y2, x1, y1))
    return(segments)

if __name__ == '__main__':
    coordinates = []
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            coordinates.append([int(coord) for coord in line.strip().split(',')])
    segments = []
    for i, coordinate in enumerate(coordinates):
        segments.append((coordinate[0], coordinate[1], coordinates[i-1][0], coordinates[i-1][1]))
    pairs = set()
    for a in coordinates:
        for b in coordinates:
            if a != b:
                pair = (a[0], a[1], b[0], b[1])
                pairs.add(pair)

    for pair in sorted(pairs, key=lambda p: area(*p), reverse=True):
        broken = False
        for coordinate in coordinates:
            if contains(*pair, *coordinate):
                #print(f"{pair} broken because it contains {coordinate}")
                broken = True
        for segment in segments:
            if cuts(*pair, *segment):
                #print(f"{pair} broken because it is cut by {segment}")
                broken = True
        if not broken:
            print(f"{pair} area = {area(*pair)}")
            break
