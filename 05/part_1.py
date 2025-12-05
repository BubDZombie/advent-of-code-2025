import re
import sys

class Range():
    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max


class Inventory():
    def __init__(self):
        self.ranges = []

    def __str__(self):
        output = ''
        for r in self.ranges:
            output += f"{r.min}-{r.max}\n"
        return(output)

    def add_range(self, _min, _max):
        expanded = False
        for r in self.ranges:
            if _min >= r.min and _max <= r.max:
                expanded = True
            elif _min <= r.min and _max >= r.min and _max <= r.max:
                r.min = _min
                expanded = True
            elif _max >= r.max and _min <= r.max and _min >= r.min:
                r.max = _max
                expanded = True
            elif _min <= r.min and _max >= r.max:
                r.min = _min
                r.max = _max
                expanded = True

            if expanded:
                break
        if not expanded:
            self.ranges.append(Range(_min, _max))

    def is_fresh(self, id):
        fresh = False
        for r in self.ranges:
            if id >= r.min and id <= r.max:
                fresh = True
                break
        return fresh


if __name__ == '__main__':
    inventory = Inventory()
    fresh_ingredients = 0
    fresh_ids = 0
    id_pairs = []
    ingredients = []
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            clean_line = line.strip()
            if re.match('\\d+-\\d+', clean_line):
                _min, _max = clean_line.split('-')
                id_pairs.append([int(_min), int(_max)])
            elif re.match('^\\d+$', clean_line):
                ingredients.append(int(clean_line))

    for _min, _max in sorted(id_pairs):
        inventory.add_range(_min, _max)

    for ingredient in ingredients:
        if inventory.is_fresh(ingredient):
            fresh_ingredients += 1

    for r in inventory.ranges:
        fresh_ids += r.max - r.min + 1

    print(inventory)
    print(f"{fresh_ids} fresh ids")
    print(f"{fresh_ingredients} fresh ingredients")
